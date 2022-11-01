import re

from django.db.models import Q
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework import exceptions, permissions, status, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
# from rest_framework_simplejwt.authentication import JWTAuthentication

from divisions.api.serializers import DivisionDetailsSerializer, DivisionSerializer
from divisions.models import ScorbotDivision
from teams.api.serializers import TeamInfoNewSerializer, TeamInfoNewDetailsSerializer
from teams.models import TeamInfoNew
from v1.permissions import CustomDjangoModelPermissions
from ..filters import TournamentFilter
from ..models import (
    Tournament
)
from .serializers import (
    TournamentSerializer, TournamentCreateSerializer,
)


@extend_schema(description="Manage Scorbot tournaments", methods=["get", "post", "put", "patch"])
class ManageTournamentsView(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                            mixins.CreateModelMixin,
                            # mixins.UpdateModelMixin,
                            GenericViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, CustomDjangoModelPermissions]
    serializer_class = TournamentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TournamentFilter
    lookup_field = 'tournament_number'
    lookup_url_kwarg = 'tournament_number'

    def get_queryset(self):
        return Tournament.objects.using('scorbot').order_by("-tournament_number", "name")

    def get_object(self):
        pattern = re.compile(r"^[0-9]+")  # check if tournament_number is a number
        if not pattern.match(self.kwargs.get(self.lookup_url_kwarg)):
            raise exceptions.ValidationError({"tournament_number_invalid": _("Tournament number must be an integer")})
        try:
            tournament = Tournament.objects.using('scorbot').get(
                tournament_number=self.kwargs['tournament_number']
            )
        except Tournament.DoesNotExist:
            raise ValidationError({"tournament_not_found": _("Tournament not found")}, code=status.HTTP_404_NOT_FOUND)

        return tournament

    def get_serializer_class(self):
        if self.action == "create":
            return TournamentCreateSerializer
        if self.action == "tournament_divisions" and self.request.method == "GET":
            return DivisionSerializer
        if self.action == "tournament_division" and self.request.method == "GET":
            return DivisionDetailsSerializer
        if self.action == "tournament_teams" and self.request.method == "GET":
            return TeamInfoNewSerializer
        if self.action == "tournament_team" and self.request.method == "GET":
            return TeamInfoNewDetailsSerializer
        return self.serializer_class

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    @extend_schema(description="Get a tournament information")
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            "error": False,
            "message": _("Tournament '#{} - {}' information").format(instance.tournament_number, instance.name),
            "results": serializer.data
        }, status=status.HTTP_200_OK)

    @extend_schema(description="Create a new tournament")
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_tournament = serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response({
            "error": False,
            "message": _("Tournament '#{} - {}' created successfully").format(new_tournament.tournament_number,
                                                                              new_tournament.name),
            "results": self.serializer_class(new_tournament).data
        }, status=status.HTTP_201_CREATED, headers=headers)

    @extend_schema(description="Get all divisions for a tournament")
    @action(detail=True, methods=["get"], url_path="division")
    def tournament_divisions(self, request, *args, **kwargs):
        tournament = self.get_object()
        serializer = self.get_serializer(tournament.divisions.all(), many=True)
        return Response({
            "error": False,
            "message": _("Divisions for Tournament '#{} - {}' successfully").format(
                tournament.tournament_number, tournament.name),
            "results": serializer.data
        }, status=status.HTTP_200_OK)

    @extend_schema(description="Get a division for a tournament")
    @action(detail=True, methods=["get"], url_path="division/(?P<division_id>[0-9]+)")
    def tournament_division(self, request, division_id, **kwargs):
        tournament = self.get_object()
        if hasattr(tournament, "divisions"):
            divisions = tournament.divisions.all()
            if divisions:
                try:
                    division = divisions.get(id=division_id)
                    if division:
                        serializer = self.get_serializer(division)
                        return Response({
                            "error": False,
                            "message": _("Division for Tournament '#{} - {}' successfully").format(
                                tournament.tournament_number, tournament.name),
                            "results": serializer.data
                        }, status=status.HTTP_200_OK)
                except ScorbotDivision.DoesNotExist:
                    raise ValidationError(
                        {"division_not_found": _("Division not found for Tournament '#{} - {}'").format(
                            tournament.tournament_number, tournament.name)},
                        code=status.HTTP_404_NOT_FOUND)

        else:
            return Response({
                "error": True,
                "message": _("There are no divisions registered for the Tournament '{}'").format(tournament.name)
            }, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(description="Get all teams for a tournament")
    @action(detail=True, methods=["get"], url_path="team")
    def tournament_teams(self, request, *args, **kwargs):
        tournament = self.get_object()
        serializer = self.get_serializer(tournament.tournament_teams_info.all(), many=True)
        return Response({
            "error": False,
            "message": _("Tournament '#{} - {}' teams").format(tournament.tournament_number, tournament.name),
            "results": serializer.data
        }, status=status.HTTP_200_OK)

    @extend_schema(description="Get a team for a tournament")
    @action(detail=True, methods=["get"], url_path="team/(?P<team_id>[0-9]+)")
    def tournament_team(self, request, team_id, **kwargs):
        tournament = self.get_object()
        if hasattr(tournament, "tournament_teams_info"):
            teams = tournament.tournament_teams_info.all()
            if teams:
                try:
                    team = teams.get(teaminfoid=team_id)
                    if team:
                        serializer = self.get_serializer(team)
                        return Response({
                            "error": False,
                            "message": _("Team for Tournament '#{} - {}' successfully").format(
                                tournament.tournament_number, tournament.name),
                            "results": serializer.data
                        }, status=status.HTTP_200_OK)
                except TeamInfoNew.DoesNotExist:
                    raise ValidationError(
                        {"team_not_found": _("Team not found for Tournament '#{} - {}'").format(
                            tournament.tournament_number, tournament.name)},
                        code=status.HTTP_404_NOT_FOUND)

        else:
            return Response({
                "error": True,
                "message": _("There are no teams registered for the Tournament '#{} - {}'").format(
                    tournament.tournament_number, tournament.name)
            }, status=status.HTTP_404_NOT_FOUND)

    # @action(detail=True, methods=["post"], url_path="team")
    # def register_teams(self, request, *args, **kwargs):
    #     tournament = self.get_object()
    #     if int(tournament.status.statusid) != int(7):
    #         raise exceptions.ValidationError(
    #             {"error": True, "message": _("Tournament is not open for registration")}
    #         )
    #     return Response({
    #         "error": False,
    #         "message": _("Team registered for Tournament {} successfully").format(tournament.name),
    #         "results": {}
    #     })