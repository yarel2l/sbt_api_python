from django_filters import rest_framework as filters
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
# from rest_framework_simplejwt.authentication import JWTAuthentication

from ..models import (
    ScorbotState
)
from .serializers import (
    StateSerializer
)


class StatesListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = ScorbotState.objects.using('scorbot').order_by('state')
    serializer_class = StateSerializer
