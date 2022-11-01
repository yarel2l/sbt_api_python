from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("userid", "username", "email", "name", "textingphone", "utype", "active", "creationdate", "lastupdate")