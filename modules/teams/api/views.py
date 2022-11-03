from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
# from rest_framework_simplejwt.authentication import JWTAuthentication

from ..filters import TeamCoachFilter
from ..models import TeamCoach, TeamInfoNew
from .serializers import TeamCoachSerializer, TeamInfoNewSerializer


@extend_schema(description="List all teams", methods=["get"])
class TeamsListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TeamInfoNewSerializer
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_class = TeamCoachFilter

    def get_queryset(self):
        return TeamInfoNew.objects.using('scorbot').order_by("-updatedate", "teamname")
