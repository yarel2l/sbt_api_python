import os

from allauth.account.signals import user_signed_up
from allauth.utils import generate_unique_username
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver, Signal
from rest_framework.authtoken.models import Token

user_verified = Signal()
User = get_user_model()


@receiver(pre_save, sender=User)
def prepare_candidate_username(sender, instance, **kwargs):
    if not instance.username or instance.username is None:
        instance.username = generate_unique_username(
            [
                instance.first_name,
                instance.last_name,
                instance.email,
            ]
        )
        instance.save()


@receiver(post_save, sender=User)
def update_user_perms(sender, instance, created, **kwargs):
    if created:
        # Register user token for api connections
        if not hasattr(instance, "auth_token"):
            Token.objects.create(user=instance)

        # Register user permissions
        perms = Permission.objects.filter(codename__icontains="change_user")
        for perm in perms:
            instance.user_permissions.add(perm)

        for user_group in instance.groups.all():
            for group_permission in user_group.permissions.all():
                instance.user_permissions.add(group_permission)


@receiver(user_signed_up)
def manage_registered_users_permissions(sender, request, user, **kwargs):
    if not hasattr(user, "auth_token"):
        Token.objects.create(user=user)

    perms = Permission.objects.filter(
        Q(codename__icontains="change_user")
    )
    for perm in perms:
        user.user_permissions.add(perm)
