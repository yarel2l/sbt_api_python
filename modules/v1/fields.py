import time
from datetime import datetime

from django.utils import timezone
from rest_framework import serializers


class TimestampField(serializers.Field):
    def to_internal_value(self, data):
        return datetime.fromtimestamp(data, tz=timezone.now().tzinfo)

    def to_representation(self, value):
        return float(time.mktime(value.timetuple()))