from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import UserSerializer

User = get_user_model()


class UserList(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.using('scorbot').all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.using('scorbot').all()
    serializer_class = UserSerializer
