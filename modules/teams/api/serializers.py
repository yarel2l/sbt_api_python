from rest_framework import serializers

from divisions.api.serializers import DivisionSerializer
from pools.api.serializers import PoolsSerializer
from ..models import TeamInfoNew, TeamCoach, Registrations, TeamsCoachTournament


class TeamCoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamCoach
        fields = ["id", "gradeid", "gender", "teamname",
                  "coachname", "coachphone", "coachemail",
                  "city", "stateid", "createdt", "updatedt",
                  "ranktype", "mergedwith", "yboa_id"]


class TeamInfoNewSerializer(serializers.ModelSerializer):
    teamid = TeamCoachSerializer(read_only=True, allow_null=True)
    divisionid = DivisionSerializer(read_only=True)
    poolid = PoolsSerializer(read_only=True)

    class Meta:
        model = TeamInfoNew
        fields = ["teaminfoid", "teamid", "teamname", "coachname", "coachphone", "divisionid", "poolid", "finals"]


class TeamInfoNewDetailsSerializer(serializers.ModelSerializer):
    # teamid = TeamSerializer(read_only=True)
    divisionid = DivisionSerializer(read_only=True)
    poolid = PoolsSerializer(read_only=True)

    class Meta:
        model = TeamInfoNew
        fields = ["teaminfoid", "teamname", "teamtxtid", "coachname", "coachphone", "divisionid", "poolid", "finals",
                  "updatedate", "updateuser", "ranking"]


class RegistrationsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Registrations
        fields = (
            'id',
            'teamid',
            'playingup',
            'updatedate',
            'updateuser',
        )


class TeamsCoachTournamentSerializer(serializers.ModelSerializer):
    teamtxtid = RegistrationsSerializers(read_only=True)

    class Meta:
        model = TeamsCoachTournament
        fields = ["id", "teamscoachid", "teamtxtid", "createdt"]