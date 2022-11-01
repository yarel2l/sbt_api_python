from django.utils.translation import gettext_lazy as _
import copy

from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly


class CustomDjangoModelPermissions(DjangoModelPermissionsOrAnonReadOnly):
    message = {"permission_denied": _("You do not have permission to perform this action.")}

    def __init__(self, *args, **kwargs):
        self.perms_map = copy.deepcopy(self.perms_map)
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
        
            
