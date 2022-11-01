from rest_framework import serializers

from ..models import ScorbotUser


class ScorbotUserSerializer(serializers.ModelSerializer):
    usermembership = serializers.SerializerMethodField()

    class Meta:
        model = ScorbotUser
        fields = ["userid", "name", "username", "email", "textingphone", "utype", "usermembership", "creationdate"]

    def get_usermembership(self, obj):
        if obj.usermembership:
            return obj.usermembership.name
        return None