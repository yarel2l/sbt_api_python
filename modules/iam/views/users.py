import logging

from allauth.account.adapter import get_adapter
from allauth.utils import build_absolute_uri
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.forms import PasswordChangeForm, AdminPasswordChangeForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import Group, Permission
from django.core.exceptions import PermissionDenied
from django.db.models import Q

from django.http import JsonResponse, HttpResponseNotAllowed, Http404
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from allauth.account.models import EmailAddress
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from django.views.generic.base import View
from django_filters.views import FilterView
from django_short_url.views import get_surl
from django_tables2 import SingleTableMixin, RequestConfig
from django_tables2.export import ExportMixin

from ..filters import UserFilter
from ..forms import UserCreateForm, UserEditForm, UserPermissionsForm, UserDeactivationForm, ProfileForm
from ..tables import UserTable
from ..utils import generate_random_password, get_shorter_url_login

logger = logging.getLogger(__name__)
User = get_user_model()


@login_required
def change_user_language_view(request):
    user_language = request.GET.get("language")
    user = request.user
    if user.is_authenticated:
        user.preferred_language = user_language
        user.save()
        messages.success(request, _(f"The site language has now been changed to {user_language}"))
        translation.activate(user_language)

    messages.error(request, _("We're sorry, the site language could not be changed!"))
    current_url = request.META.get("HTTP_REFERER", None)
    return redirect(current_url)


class ManageUsersView(PermissionRequiredMixin, LoginRequiredMixin, ExportMixin, SingleTableMixin, FilterView):
    permission_required = "iam.view_user"
    template_name = "iam/users/manage.html"
    model = User
    table_class = UserTable
    exclude_columns = ("selection", "actions")
    filterset_class = UserFilter
    paginate_by = 25
    strict = False

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return User.objects.all()

        elif self.request.user.has_perm("iam.view_user"):
            return User.objects.exclude(Q(is_superuser=True) | Q(is_staff=True))
        return User.objects.none()

    def get_context_data(self, **kwargs):
        context = super(ManageUsersView, self).get_context_data(**kwargs)
        context["title"] = _("User Accounts")
        # if self.tenant:
        #     context["table_top"] = True
        #     context["tenant"] = self.tenant

        return context


class UserCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = "iam.add_user"
    model = User
    form_class = UserCreateForm
    template_name = "iam/users/form.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user.is_superuser or self.request.user.is_staff:
            kwargs["groups"] = Group.objects.order_by("name")
        else:
            kwargs["groups"] = self.request.user.groups.order_by("name")

        kwargs["request"] = self.request

        return kwargs

    def form_valid(self, form):

        user = form.save()
        user_pwd = generate_random_password(user)
        user.save()
        EmailAddress.objects.create(user=user, email=user.email, verified=True, primary=True)

        if form.cleaned_data.get("send_email"):
            login_url = get_shorter_url_login(self.request)
            site_name = settings.SITE_NAME
            template_name = 'iam/users/email/created_account'

            context = {
                "email": user.email,
                "password": user_pwd,
                "fullname": user.get_full_name(),
                "login_url": login_url,
                "site_name": site_name,
                "domain": self.request.get_host(),
            }

            try:
                get_adapter().send_mail(
                    template_name,
                    user.email,
                    context)

            except Exception as e:
                logger.error("Error sending email: %s" % e)

        messages.success(self.request, _("New User registered successfully!"))
        return redirect(user.get_profile_url())

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context["title"] = _("New User Account")

        return context


class AccountInformationView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = "iam.change_user"
    model = User
    form_class = UserEditForm
    template_name = "iam/users/account_information.html"
    slug_field = "uid"
    slug_url_kwarg = "uid"

    def get_object(self, **kwargs):
        if self.request.user.is_superuser or self.request.user.is_staff:
            try:
                self.object = User.objects.get(uid=self.kwargs["uid"])
            except User.DoesNotExist:
                raise Http404
        elif self.request.user.has_perm("iam.change_user"):
            try:
                self.object = User.objects.get(
                    Q(id=self.request.user.pk),
                    uid=self.kwargs["uid"])
            except User.DoesNotExist:
                raise PermissionDenied

        else:
            raise PermissionDenied

        return super().get_object()

    def form_valid(self, form):
        if form.has_changed():
            object = form.save()
            messages.success(self.request, _(f"Account Information updated for User {object.__str__()}"))
        return redirect(reverse_lazy("account_information", kwargs={"uid": self.get_object().uid}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Account Information")
        context["user"] = self.get_object()

        # Table implementation with filter in Views
        # user_devices = self.get_object().devices.all()
        # from devices.filters import DevicesFilter
        # filter = DevicesFilter(self.request.GET, user_devices)
        # from devices.tables import UserDevicesTable
        # table_user_devices = UserDevicesTable(filter.qs)
        # RequestConfig(self.request, paginate={"per_page": 10}).configure(table_user_devices)
        # context["table"] = table_user_devices
        # context["filter"] = filter

        # from locations.forms import SearchAddressForm
        # context["address_form"] = SearchAddressForm
        context["addresses"] = None #self.request.user.addresses

        return context


class CustomPasswordChangeView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = "iam.change_user"
    model = User
    form_class = PasswordChangeForm
    template_name = "iam/users/password.html"
    slug_field = "uid"
    slug_url_kwarg = "uid"

    def get_object(self, **kwargs):
        if self.request.user.is_superuser or self.request.user.is_staff:
            try:
                self.object = User.objects.get(uid=self.kwargs["uid"])
            except User.DoesNotExist:
                raise Http404
        elif self.request.user.has_perm("iam.change_user"):
            try:
                self.object = User.objects.get(
                    Q(id=self.request.user.pk),
                    uid=self.kwargs["uid"])
            except User.DoesNotExist:
                raise PermissionDenied

        else:
            raise PermissionDenied

        return super().get_object()

    def get_form_class(self):
        return PasswordChangeForm if self.get_object() == self.request.user else AdminPasswordChangeForm

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return (
            form_class(self.get_object())
            if self.request.method == "GET"
            else form_class(self.get_object(), self.request.POST)
        )

    def form_valid(self, form):
        if form.has_changed():
            object = form.save()
            messages.success(self.request, _(f"Account Password updated for User {object.__str__()}"))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.get_object()
        context["title"] = _("Change Password")

        return context


class DeactivateAccountView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = "iam.change_user"
    model = User
    form_class = UserDeactivationForm
    template_name = "iam/users/deactivation.html"
    slug_field = "uid"
    slug_url_kwarg = "uid"

    def get_object(self, **kwargs):
        if self.request.user.is_superuser or self.request.user.is_staff:
            try:
                self.object = User.objects.get(uid=self.kwargs["uid"])
            except User.DoesNotExist:
                raise Http404
        elif self.request.user.has_perm("iam.change_user"):
            try:
                self.object = User.objects.get(
                    Q(id=self.request.user.pk),
                    uid=self.kwargs["uid"])
            except User.DoesNotExist:
                raise PermissionDenied

        else:
            raise PermissionDenied

        return super().get_object()

    def form_valid(self, form):
        if form.has_changed():
            account = form.save(commit=False)
            if form.cleaned_data.get("deactivate"):
                account.is_active = False
            account.save()
            # TODO: Process inactive accounts
            messages.success(self.request, _(f"Account deactivation completed!"))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.get_object()
        context["title"] = _("Deactivate Account")

        return context


class UserPermissionsView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = "auth.change_permission"
    model = User
    form_class = UserPermissionsForm
    template_name = "iam/users/permissions.html"
    slug_field = "uid"
    slug_url_kwarg = "uid"

    def get_object(self, **kwargs):
        if self.request.user.is_superuser or self.request.user.is_staff:
            try:
                self.object = User.objects.get(uid=self.kwargs["uid"])
            except User.DoesNotExist:
                raise Http404
        elif self.request.user.has_perm("auth.change_permission"):
            # try:
            #     self.object = User.objects.get(Q(username=self.request.user.username) | Q(created_by=self.request.user),
            #                                    uid=self.kwargs["uid"])
            try:
                self.object = User.objects.get(
                    Q(id=self.request.user.pk),
                    uid=self.kwargs["uid"])
            except User.DoesNotExist:
                raise PermissionDenied

        return super().get_object()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user.is_superuser or self.request.user.is_staff:
            # kwargs["groups"] = Group.objects.order_by("name")
            kwargs["user_permissions"] = Permission.objects.all()
        else:
            # kwargs["groups"] = self.request.user.groups.order_by("name")
            kwargs["user_permissions"] = self.request.user.user_permissions.all()

        return kwargs

    def form_valid(self, form):
        if form.has_changed():
            object = form.save()
            # object.groups.set(form.cleaned_data["groups", None])
            #
            # for user_group in object.groups.all():
            #     for group_permission in user_group.permissions.all():
            #         object.user_permissions.add(group_permission)

            messages.success(self.request, _(f"Permissions updated for User {object.__str__()}"))
        return redirect(reverse_lazy("account_permissions", kwargs={"uid": self.get_object().uid}))

    def get_context_data(self, **kwargs):
        context = super(UserPermissionsView, self).get_context_data(**kwargs)
        context["user"] = self.get_object()
        context["title"] = _("Roles & Permissions")
        return context

    def get_success_url(self):
        return reverse_lazy("account_permissions", kwargs=self.kwargs)


class AccountProfileSettingsView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = "iam.change_user"
    model = User
    form_class = ProfileForm
    template_name = "iam/profile/general_profile.html"
    slug_field = "uid"
    slug_url_kwarg = "uid"

    def get_object(self, **kwargs):
        if self.request.user.is_superuser or self.request.user.is_staff:
            try:
                self.object = User.objects.get(uid=self.kwargs["uid"])
            except User.DoesNotExist:
                raise Http404
        elif self.request.user.has_perm("iam.change_user"):
            try:
                self.object = User.objects.get(
                    id=self.request.user.pk,
                    uid=self.kwargs["uid"])
            except User.DoesNotExist:
                raise PermissionDenied
        else:
            raise PermissionDenied

        return super().get_object()

    def get_form(self, form_class=None):
        if self.request.method == "POST":
            return ProfileForm(self.request.POST, instance=self.get_object())
        return ProfileForm(instance=self.get_object())

    def form_valid(self, form):
        object = form.save()
        messages.success(self.request, _(f"Profile updated for User {object.__str__()}"))
        return redirect(self.get_object().get_profile_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Profile Settings")
        context["user"] = self.get_object()
        context["form_deactivation"] = UserDeactivationForm(instance=self.get_object())

        return context


@permission_required("iam.delete_user")
def delete_user_account_view(request, uid):
    if request.user.has_perm("iam.delete_user"):
        if request.method == "DELETE":
            user = get_object_or_404(User, uid=uid)
            user.delete()
            return JsonResponse({"uid": user.uid, "redirect_to": reverse_lazy("users_list")})
        return HttpResponseNotAllowed(["DELETE"])
    else:
        return JsonResponse({"uid": None})


class BulkDeleteAccountsView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = "iam.delete_user"

    def post(self, *args, **kwargs):
        selection = self.request.POST.getlist("selection[]")

        if len(selection) > 0:

            objects = User.objects.filter(pk__in=selection)
            objects.delete()
            messages.success(self.request, _("User Accounts selected removed successfully"))

        else:
            messages.info(self.request, _("No User Accounts selected"))
        return redirect(reverse_lazy("users_list"))

