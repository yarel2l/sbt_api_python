from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='has_role')
def has_role(user, role_pk):
    group = Group.objects.get(pk=role_pk)
    return True if group in user.groups.all() else False


@register.filter(name='has_roles')
def has_groups(user, role_list_pk):
    group = Group.objects.get(pk_in=role_list_pk)
    return True if group in user.groups.all() else False