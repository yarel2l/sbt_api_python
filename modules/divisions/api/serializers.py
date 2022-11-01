from rest_framework import serializers

from core.api.serializers import GradesSerializer
from ..models import (
    ScorbotDivision
)


class DivisionSerializer(serializers.ModelSerializer):
    grade = GradesSerializer(read_only=True)

    class Meta:
        model = ScorbotDivision
        fields = ["id", "name", "divisiontype", "gender", "grade"]
        # exclude = ["tournamentid", "sporttype", "updatedate", "updateuser",
        #            "perpooldesc", "gppdesc", "bracketsdesc",
        #            "maincolor", "altcolor", "hometextcolor", "visitortextcolor"]


class DivisionDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScorbotDivision
        exclude = ["tournamentid"] #, "sporttype", "updatedate", "updateuser",
                   # "perpooldesc", "gppdesc", "bracketsdesc",
                   # "maincolor", "altcolor", "hometextcolor", "visitortextcolor"]