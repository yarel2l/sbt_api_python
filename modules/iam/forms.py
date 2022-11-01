from allauth.account.models import EmailAddress, EmailConfirmation
from django.utils.translation import gettext_lazy as _
from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm
from django.contrib.auth import get_user_model
from django import forms
from django_select2.forms import ModelSelect2Widget, Select2Widget

from timezone_field import TimeZoneFormField

from . import app_settings


from .widgets import TabularPermissionsWidget

User = get_user_model()


class MyCustomLoginForm(LoginForm):

    def login(self, *args, **kwargs):

        # Add your own processing here.

        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)


class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=50, label=_("First Name"), required=True)
    last_name = forms.CharField(max_length=50, label=_("Last Name"), required=True)
    email = forms.EmailField(max_length=180, required=True, label=_("Email Address"))

    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.
        # Save your user
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # You must return the original result.
        return user


class MyCustomResetPasswordForm(ResetPasswordForm):

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a string containing the email address supplied
        email_address = super().save(request)

        # Add your own processing here.

        # Ensure you return the original result
        return email_address


class UserCreateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label=_("First Name"), required=True)
    last_name = forms.CharField(max_length=50, label=_("Last Name"), required=True)
    email = forms.EmailField(max_length=180, label=_("Email"), required=True)
    send_email = forms.BooleanField(label=_("Send Email Notification"), required=False)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "website",
            "email",
            "groups",
            "send_email",
        )

    def __init__(self, **kwargs):
        request = kwargs.pop("request", None)
        groups = kwargs.pop("groups", None)
        super().__init__(**kwargs)

        if groups:
            self.fields["groups"].queryset = groups
        else:
            del self.fields["groups"]


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "website",
            "email",
        )


class UserDeactivationForm(forms.ModelForm):
    deactivate = forms.BooleanField(label=_("I confirm my account deactivation"),
                                    widget=forms.CheckboxInput(attrs={"enabled": False}))

    class Meta:
        model = User
        fields = (
            "deactivate",
        )

    # def __init__(self, **kwargs):
    #     user = kwargs.pop("user", None)
    #     super().__init__(**kwargs)


class UserPermissionsForm(forms.ModelForm):
    # groups = forms.ModelMultipleChoiceField(queryset=Group.objects.order_by("name"), required=False, label=_("Roles"))

    def __init__(self, **kwargs):
        # groups = kwargs.pop("groups", None)
        permissions = kwargs.pop("user_permissions", None)
        super().__init__(**kwargs)
        # if groups:
        #     self.fields["groups"].queryset = groups

        if permissions:
            self.fields["user_permissions"].queryset = permissions
            self.fields["user_permissions"].widget = TabularPermissionsWidget(
                verbose_name=_("Permissions"), is_stacked=True, permissions_list=permissions
            )

    class Meta:
        model = User
        fields = (
            "is_superuser",
            "is_staff",
            # "groups",
            "user_permissions",
        )


class EmailAddressForm(forms.ModelForm):

    user = forms.ModelChoiceField(
        queryset=User.objects.filter(is_active=True),
        label=u"User Accounts",
        widget=ModelSelect2Widget(
            model=User,
            search_fields=["first_name__icontains", "last_name__icontains", "email__icontains",
                           "mobile__icontains", "username__icontains"],
            max_results=500,
            attrs={
                'data-minimum-input-length': 0
            },
        ),
    )

    class Meta:
        model = EmailAddress
        fields = ("user", "email", "primary", "verified")


class EmailConfirmationForm(forms.ModelForm):

    email_address = forms.ModelChoiceField(
        queryset=EmailAddress.objects.filter(verified=False),
        label=u"Email Address",
        widget=ModelSelect2Widget(
            model=EmailAddress,
            search_fields=["user__first_name__icontains", "user__last_name__icontains", "email__icontains",
                           "user__mobile__icontains", "user__username__icontains", "user__email__icontains"],
            max_results=500,
            attrs={
                'data-minimum-input-length': 0
            },
        ),
    )
    send_email = forms.BooleanField(label=_("Send Email Notification"), required=False,
                                    help_text=_("Send a message to the selected email with the new link so that the owner can verify their data"))

    def save(self, commit=False):
        """
        There is nothing to save
        """
        pass

    class Meta:
        model = EmailConfirmation
        fields = ("email_address", "send_email")


class ProfileForm(forms.ModelForm):
    timezone = TimeZoneFormField(choices_display='WITH_GMT_OFFSET', widget=Select2Widget())

    class Meta:
        model = User
        fields = (
            "preferred_language",
            "timezone",
        )
        widgets = {
            "preferred_language": Select2Widget,
        }


class ProfileSettingForm(forms.ModelForm):
    timezone = TimeZoneFormField(choices_display='WITH_GMT_OFFSET', widget=Select2Widget)

    class Meta:
        model = User
        fields = ("timezone",)


class ProfileSettingModalForm(forms.ModelForm):
    timezone_input = TimeZoneFormField(
        label=_("Timezone"),
        widget=Select2Widget(attrs={
            "data-dropdown-parent": "#timezone_modal"
        })
        )

    class Meta:
        model = User
        fields = ("timezone_input",)