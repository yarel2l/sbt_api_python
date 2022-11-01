from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import Group, GroupAdmin as DjGroupAdmin, UserAdmin as DjUserAdmin, UserAdmin
from django.contrib.auth.models import Permission
from django.core.exceptions import ImproperlyConfigured

from . import app_settings
from .widgets import TabularPermissionsWidget

User = get_user_model()


class CustomUserAdmin(UserAdmin, admin.ModelAdmin):
    list_display = ("email", "timezone", "preferred_language", "is_active")
    add_fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name',
                       'email', 'password1', 'password2')}
         ),
    )


admin.site.register(User, CustomUserAdmin)


class UserTabularPermissionsMixin(object):
    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        field = super(UserTabularPermissionsMixin, self).formfield_for_manytomany(db_field, request, **kwargs)
        if db_field.name == 'user_permissions':
            field.widget = TabularPermissionsWidget(db_field.verbose_name, db_field.name in self.filter_vertical)
            field.help_text = ''
        return field


class GroupTabularPermissionsMixin(object):
    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        field = super(GroupTabularPermissionsMixin, self).formfield_for_manytomany(db_field, request, **kwargs)
        if db_field.name == 'permissions':
            field.widget = TabularPermissionsWidget(db_field.verbose_name, db_field.name in self.filter_vertical,
                                                    'permissions')
            field.help_text = ''
        return field


try:
    UserAdminModel = admin.site._registry[User].__class__
except:
    UserAdminModel = DjUserAdmin

try:
    GroupAdminModel = admin.site._registry[Group].__class__
except:
    GroupAdminModel = DjGroupAdmin


class TabularPermissionsUserAdmin(UserTabularPermissionsMixin, UserAdminModel):
    pass


class TabularPermissionsGroupAdmin(GroupTabularPermissionsMixin, GroupAdminModel):
    pass


if app_settings.AUTO_IMPLEMENT:
    try:
        admin.site.unregister(User)
        admin.site.register(User, TabularPermissionsUserAdmin)
        admin.site.unregister(Group)
        admin.site.register(Group, TabularPermissionsGroupAdmin)

    except:
        raise ImproperlyConfigured('Please make sure that django.contrib.auth '
                                   'comes before accounting in INSTALLED_APPS')


class PermissionAdmin(admin.ModelAdmin):
    list_display = ["id", "content_type", "name", "codename"]


admin.site.register(Permission, PermissionAdmin)