from django.conf import settings

from . import app_settings


def global_params(request):

    context = {
        'SITE_NAME': app_settings.SITE_NAME,
        'COPYRIGHT_TEXT': app_settings.COPYRIGHT_TEXT,
        'POWERED_BY': app_settings.POWERED_BY,
        "sentry_dsn": settings.RAVEN_CONFIG.get("dsn") if hasattr(settings, 'RAVEN_CONFIG') and settings.RAVEN_CONFIG else "localhost"}

    return context
