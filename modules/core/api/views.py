from django_filters import rest_framework as filters
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
# from rest_framework_simplejwt.authentication import JWTAuthentication

from ..models import (
    ScorbotTimezone,
    ScorbotGrade,
    ScorbotStatus,
    ScorbotEventType,
)
from .serializers import (
    TimezoneSerializer,
    GradesSerializer,
    StatusSerializer,
    EventTypeSerializer,
)


class TimezoneListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = ScorbotTimezone.objects.using('scorbot').order_by("code")
    serializer_class = TimezoneSerializer


class GradesListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = ScorbotGrade.objects.using('scorbot').order_by("id")
    serializer_class = GradesSerializer


class StatusListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = ScorbotStatus.objects.using('scorbot').order_by('ranking')
    serializer_class = StatusSerializer


class EventTypeListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = ScorbotEventType.objects.using('scorbot').all()
    serializer_class = EventTypeSerializer



