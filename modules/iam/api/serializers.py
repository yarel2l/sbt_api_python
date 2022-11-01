from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from timezone_field.rest_framework import TimeZoneSerializerField

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    display_name = serializers.SerializerMethodField()
    display_initials_name = serializers.SerializerMethodField()
    timezone = TimeZoneSerializerField()

    class Meta:
        model = User
        fields = (
            "id",
            "uid",
            "display_name",
            "display_initials_name",
            "first_name",
            "last_name",
            "username",
            "email",
            "timezone",
            "preferred_language",
            "avatar_url",
            "date_joined",
            "last_login",
        )
        read_only_fields = (
            "id",
            "uid",
            "date_joined",
            "last_login",
            "email",
            "username",
            "display_name",
            "display_initials_name",
            "avatar_url",
        )
        depth = 1

    def get_display_name(self, obj):
        return obj.__str__()

    def get_display_initials_name(self, obj):
        init = ""
        if obj.first_name:
            init += obj.first_name[:1].upper()
        if obj.last_name:
            init += obj.last_name[:1].upper()
        else:
            init += obj.username[:2]
        return init


class UserDeactivationSerializer(serializers.Serializer):
    uid = serializers.CharField(required=True, help_text=_("Enter a valid User uid field"))