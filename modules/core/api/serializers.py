from rest_framework import serializers

from ..models import (
    ScorbotTimezone,
    ScorbotGrade,
    ScorbotStatus,
    ScorbotModule,
    ScorbotTime,
    ScorbotEventType,
)


class TimezoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScorbotTimezone
        fields = ['code', 'descrip']


class GradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScorbotGrade
        fields = ['id', 'gradenbr', 'grade']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScorbotStatus
        fields = ["statusid", "statusdesc", "details"]

    # def to_representation(self, instance):
    #     return "{}-{}".format(instance.statusid, instance.statusdesc)


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScorbotModule
        fields = "__all__"


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScorbotTime
        fields = "__all__"


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScorbotEventType
        fields = ["id", "descr"]