import re

from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django_gravatar.helpers import get_gravatar_url
from model_utils.fields import UrlsafeTokenField
from model_utils.models import TimeStampedModel
from timezone_field import TimeZoneField

from .managers import UserInheritanceManager


class UserProfile(models.Model):
    website = models.URLField(verbose_name=_("Website"))
    timezone = TimeZoneField(verbose_name=_("Timezone"), default=settings.TIME_ZONE,
                             null=True, blank=True)
    preferred_language = models.CharField(
        verbose_name=_("Language"), max_length=20,
        choices=settings.LANGUAGES, default=settings.LANGUAGES[0][0]
    )

    class Meta:
        abstract = True


class User(AbstractUser, UserProfile):
    uid = UrlsafeTokenField(verbose_name=_("UID"), unique=True)

    objects = UserInheritanceManager()

    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        elif self.username:
            return self.username
        return self.email

    @property
    def avatar_url(self):
        return get_gravatar_url(str(self.email), size=45)

    def show_email(self):
        if not self.email:
            return "*@*.***"
        else:
            output = re.split(r"[@.]", self.email)
            return f"{output[0][:1]}***@{output[1]}.{output[2]}"

    # ======================================================

    # Manage User urls
    def get_edit_url(self):
        return reverse_lazy("account_information", kwargs={"uid": self.uid})

    def get_permissions_url(self):
        return reverse_lazy("account_permissions", kwargs={"uid": self.uid})

    def get_absolute_url(self):
        return reverse_lazy("account_information", kwargs={"uid": self.uid})

    def get_password_change_url(self):
        return reverse_lazy("password_change_view", kwargs={"uid": self.uid})

    def get_deactivate_account_url(self):
        return reverse_lazy("account_deactivate_view", kwargs={"uid": self.uid})

    def get_delete_url(self):
        return reverse_lazy("account_delete", kwargs={"uid": self.uid})

    def get_profile_url(self):
        return reverse_lazy("account_profile", kwargs={"uid": self.uid})
