import pytz
from django.conf import settings
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin


class TimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        tzname = settings.TIME_ZONE

        if request.user.is_authenticated and request.user.timezone:
            tzname = str(request.user.timezone)

        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()