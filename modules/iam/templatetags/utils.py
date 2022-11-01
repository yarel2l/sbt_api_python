from django.conf import settings
from rest_framework.reverse import reverse_lazy
from sekizai.context import SekizaiContext

from ..forms import ProfileSettingModalForm


def get_profile_timezone_form_context(context, user=None):
    if not user:
        request = context['request']
        user = getattr(request, 'user', None)

    data = {
        'timezone_form': ProfileSettingModalForm,
        'request': context['request'],
    }

    return data


def get_profile_scripts_context(context, user=None):
    if not user:
        request = context['request']
        user = getattr(request, 'user', None)

    data = {
        'utz': user.timezone if user.is_authenticated else settings.TIME_ZONE,
        'upd_tz_endpoint': reverse_lazy('rest_user_details'),
        'user': user,
        'request': context['request']
    }

    return SekizaiContext(data)