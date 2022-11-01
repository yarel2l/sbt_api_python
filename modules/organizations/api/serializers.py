from rest_framework import serializers

from users.api.serializers import ScorbotUserSerializer
from users.models import ScorbotUser
from ..models import (
    ScorbotOrganization,
    ScorbotSMSPhone
)


class SMSPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScorbotSMSPhone
        fields = ["smsid", "smsphone", "effectiveyear"]


class OrganizationsSerializer(serializers.ModelSerializer):
    state = serializers.SerializerMethodField()

    class Meta:
        model = ScorbotOrganization
        fields = ["id", "name", "shortname", "city", "state"]

    def get_state(self, obj):
        if obj.state:
            return obj.state.state
        return None


class OrganizationDetailsSerializer(serializers.ModelSerializer):
    director = serializers.SerializerMethodField()
    # smsphones = SMSPhoneSerializer(many=True, read_only=True)
    state = serializers.SerializerMethodField()

    class Meta:
        model = ScorbotOrganization
        fields = ["id", "name", "shortname", "city", "state",
                  "contactname", "contactphone", "contactemail", "director",
                  "createdt", "updatedt", "tiebreakingurl"] #, "smsphones"]

    def get_director(self, obj):
        try:
            user = ScorbotUser.objects.using("scorbot").get(userid=obj.director)
            return ScorbotUserSerializer(user).data
        except ScorbotUser.DoesNotExist:
            return None

    def get_state(self, obj):
        if obj.state:
            return str(obj.state.state)
        return None