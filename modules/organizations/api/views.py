from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _
from rest_framework import generics, permissions, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
# from rest_framework_simplejwt.authentication import JWTAuthentication

from ..filters import ScorbotSMSPhoneFilter
from ..models import (
    ScorbotOrganization, ScorbotSMSPhone
)
from .serializers import (
    OrganizationsSerializer, SMSPhoneSerializer
)


class OrganizationsView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = ScorbotOrganization.objects.using('scorbot').all()
    serializer_class = OrganizationsSerializer

    def get_queryset(self):
        return ScorbotOrganization.objects.using('scorbot').all()

    def get_object(self):
        try:
            org = ScorbotOrganization.objects.using('scorbot').get(
                pk=self.kwargs['pk']
            )
        except ScorbotOrganization.DoesNotExist:
            raise ValidationError({"not_found": _("Organization not found")},
                                  code=status.HTTP_404_NOT_FOUND)

        return org

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            "error": False,
            "message": _(f"Organization '{instance}' details"),
            "results": serializer.data
        })


class SMSPhoneListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = ScorbotSMSPhone.objects.using('scorbot').all()
    serializer_class = SMSPhoneSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ScorbotSMSPhoneFilter