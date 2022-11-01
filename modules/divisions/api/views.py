from django_filters import rest_framework as filters
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
# from rest_framework_simplejwt.authentication import JWTAuthentication

from v1.permissions import CustomDjangoModelPermissions
from ..filters import ScorbotDivisionFilter
from ..models import (
    ScorbotDivision
)
from .serializers import (
    DivisionSerializer
)


class DivisionsListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, CustomDjangoModelPermissions]
    queryset = ScorbotDivision.objects.using('scorbot').all()
    serializer_class = DivisionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ScorbotDivisionFilter