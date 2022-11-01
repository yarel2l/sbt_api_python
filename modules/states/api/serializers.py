from rest_framework import serializers

from ..models import ScorbotState


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScorbotState
        fields = "__all__"