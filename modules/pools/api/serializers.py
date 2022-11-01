from rest_framework import serializers

from ..models import Pool, PoolStandings


class PoolStandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoolStandings
        exclude = ["credits", "debits", "pointstie2", "coin"]


class PoolsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pool
        fields = ["id", "poolname"]