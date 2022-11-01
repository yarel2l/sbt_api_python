from django import forms
from django.utils.translation import gettext_lazy as _
from django_select2.forms import Select2Widget
from oauth2_provider.models import get_application_model

OauthApplication = get_application_model()


class OauthApplicationForm(forms.ModelForm):

    class Meta:
        model = OauthApplication
        fields = (
            "name",
            "client_id",
            "client_secret",
            "client_type",
            "authorization_grant_type",
            "redirect_uris",
            # "algorithm",
        )
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "client_id": forms.TextInput(attrs={"class": "form-control"}),
            "client_secret": forms.TextInput(attrs={"class": "form-control"}),
            "client_type": Select2Widget,
            "authorization_grant_type": Select2Widget,
            "redirect_uris": forms.Textarea(attrs={"class": "form-control"}),
            # "algorithm": Select2Widget(attrs={"class": "form-control"}),
        }
        labels = {
            "name": _("Name"),
            "client_id": _("Client ID"),
            "client_secret": _("Client Secret"),
            "client_type": _("Client Type"),
            "authorization_grant_type": _("Authorization Grant Type"),
            "redirect_uris": _("Redirect URIs"),
            # "algorithm": _("Algorithm"),
        }
        help_texts = {
            "name": _("Name of the application"),
            "client_id": _("Client ID of the application"),
            "client_secret": _("Hashed on Save. Copy it now if this is a new secret."),
            "client_type": _("Client Type of the application"),
            "authorization_grant_type": _("Authorization Grant Type of the application"),
            "redirect_uris": _("Allowed URIs list, space separated"),
            # "algorithm": _("Algorithm of the application"),
        }