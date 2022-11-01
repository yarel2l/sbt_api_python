from rest_framework import serializers

from divisions.api.serializers import DivisionSerializer
from pools.api.serializers import PoolsSerializer
from ..models import Team, TeamInfoNew


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["teamid", "teamname", "gender", "gradeid"]


class TeamInfoNewSerializer(serializers.ModelSerializer):
    # teamid = TeamSerializer(read_only=True)
    divisionid = DivisionSerializer(read_only=True)
    poolid = PoolsSerializer(read_only=True)

    class Meta:
        model = TeamInfoNew
        fields = ["teaminfoid", "teamname", "coachname", "coachphone", "divisionid", "poolid", "finals"]


class TeamInfoNewDetailsSerializer(serializers.ModelSerializer):
    # teamid = TeamSerializer(read_only=True)
    divisionid = DivisionSerializer(read_only=True)
    poolid = PoolsSerializer(read_only=True)

    class Meta:
        model = TeamInfoNew
        fields = ["teaminfoid", "teamname", "teamtxtid", "coachname", "coachphone", "divisionid", "poolid", "finals",
                  "updatedate", "updateuser", "ranking"]