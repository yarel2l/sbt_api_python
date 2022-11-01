from django.utils.translation import gettext_lazy as _
from django.conf import settings


SITE_NAME = getattr(settings, "SITE_NAME", "SCORBOT API")
COPYRIGHT_TEXT = getattr(settings, "COPYRIGHT_TEXT", _("All rights reserved"))
POWERED_BY = getattr(settings, "POWERED_BY", _("Powered by SCORBOT"))
