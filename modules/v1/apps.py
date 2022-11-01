from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TournamentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'v1'
    verbose_name = _("Scorbot API v1")
