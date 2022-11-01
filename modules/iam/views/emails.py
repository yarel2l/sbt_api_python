import logging
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from django.http import JsonResponse, HttpResponseNotAllowed
from django.utils.translation import gettext_lazy as _
from allauth.account.models import EmailAddress, EmailConfirmation
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic.base import View
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from django_tables2.export import ExportMixin

from ..filters import EmailAddressFilter, EmailAddressConfirmationFilter
from ..forms import EmailAddressForm, EmailConfirmationForm
from ..tables import EmailAddressTable, EmailAddressConfirmationTable

User = get_user_model()


class ManageEmailsView(PermissionRequiredMixin, LoginRequiredMixin, ExportMixin, SingleTableMixin, FilterView):
    permission_required = "account.view_emailaddress"
    model = EmailAddress
    template_name = "iam/emails/manage.html"
    table_class = EmailAddressTable
    exclude_columns = ("selection", "actions")
    filterset_class = EmailAddressFilter
    paginate_by = 25
    strict = False

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return EmailAddress.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        context = super(ManageEmailsView, self).get_context_data(**kwargs)
        context["title"] = _("Email Address")

        return context


class EmailAddressCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = "account.add_emailaddress"
    model = EmailAddress
    form_class = EmailAddressForm
    template_name = "iam/emails/form.html"

    def form_invalid(self, form):
        messages.error(
            self.request, _("Sorry, an error has occurred. Please, check your form data: " + str(form.errors))
        )
        return super(EmailAddressCreateView, self).form_invalid(form)

    def form_valid(self, form):
        object = form.save()
        messages.success(self.request, _(f"Email Address {object.email} registered for User {object.user.__str__()}"))
        return redirect(reverse_lazy("emails"))

    def get_context_data(self, **kwargs):
        context = super(EmailAddressCreateView, self).get_context_data(**kwargs)
        context["title"] = _("Email Address")
        context["scenario"] = "create"

        return context


class EmailAddressUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = "account.change_emailaddress"
    model = EmailAddress
    form_class = EmailAddressForm
    template_name = "iam/emails/form.html"

    def form_invalid(self, form):
        messages.error(
            self.request, _("Sorry, an error has occurred. Please, check your form data: " + str(form.errors))
        )
        return super(EmailAddressUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        object = form.save()
        messages.success(self.request, _(f"Email Address updated: {object.email}"))
        return redirect(reverse_lazy("emails"))

    def get_context_data(self, **kwargs):
        context = super(EmailAddressUpdateView, self).get_context_data(**kwargs)
        context["title"] = _("Email Address")
        context["scenario"] = "edit"

        return context


@permission_required("account.delete_emailaddress")
def delete_email_address(request, pk):
    object = get_object_or_404(EmailAddress, pk=pk)
    if request.user.has_perm("account.delete_emailaddress"):
        if request.method == "POST":
            object.delete()
            messages.success(request, _(f"Email Address {object.email} for User {object.user} deleted!"))
            return JsonResponse({"key": object.pk, "redirect_to": reverse_lazy("emails")})
        return HttpResponseNotAllowed(["POST"])
    else:
        return JsonResponse({"pk": None})


class BulkDeleteEmailAddressView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = "account.delete_emailaddress"

    def post(self, *args, **kwargs):
        selection = self.request.POST.getlist("selection[]")

        if len(selection) > 0:

            objects = EmailAddress.objects.filter(pk__in=selection)
            objects.delete()
            messages.success(self.request, _(f"{len(selection)} Email Address deleted successfully"))

        else:
            messages.info(self.request, _("No Email Address selected"))
        return redirect(reverse_lazy("emails"))


class ManageEmailsConfirmationView(PermissionRequiredMixin, LoginRequiredMixin, ExportMixin, SingleTableMixin, FilterView):
    permission_required = "account.view_emailconfirmation"
    model = EmailConfirmation
    template_name = "iam/email_confirmation/manage.html"
    table_class = EmailAddressConfirmationTable
    exclude_columns = ("selection", "actions")
    filterset_class = EmailAddressConfirmationFilter
    paginate_by = 25
    strict = False

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return EmailConfirmation.objects.all().order_by("-created")

    def get_context_data(self, **kwargs):
        context = super(ManageEmailsConfirmationView, self).get_context_data(**kwargs)
        context["title"] = _("Confirmation Emails")

        return context


class EmailAddressConfirmationCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = "account.add_emailconfirmation"
    model = EmailConfirmation
    form_class = EmailConfirmationForm
    template_name = "iam/email_confirmation/form.html"

    def form_valid(self, form):
        object = EmailConfirmation.create(form.cleaned_data["email_address"])
        if form.cleaned_data["send_email"]:
            try:
                object.send(request=self.request)
            except Exception as e:
                logging.error(f"Error sending email confirmation using new Key. EXCEPTION: {e.__str__()}")
        messages.success(self.request, _(f"Email confirmation {object.email_address} registered for User {object.email_address.user.__str__()}"))
        return redirect(reverse_lazy("emails_confirmations"))

    def get_context_data(self, **kwargs):
        context = super(EmailAddressConfirmationCreateView, self).get_context_data(**kwargs)
        context["title"] = _("Confirmation Email ")

        return context


class EmailAddressConfirmationUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = "account.change_emailconfirmation"
    model = EmailConfirmation
    form_class = EmailConfirmationForm
    template_name = "iam/email_confirmation/form.html"

    def form_valid(self, form):
        object = EmailConfirmation.create(form.cleaned_data["email_address"])
        if form.cleaned_data["send_email"]:
            try:
                object.send(request=self.request)
            except Exception as e:
                logging.error(f"Error sending email confirmation using new Key. EXCEPTION: {e.__str__()}")
        messages.success(self.request, _(f"Email confirmation updated: {object.email_address}"))
        return redirect(reverse_lazy("emails_confirmations"))

    def get_context_data(self, **kwargs):
        context = super(EmailAddressConfirmationUpdateView, self).get_context_data(**kwargs)
        context["title"] = _("Confirmation Email")

        return context


@permission_required("account.delete_emailconfirmation")
def delete_email_address_confirmation_view(request, pk):
    object = get_object_or_404(EmailConfirmation, pk=pk)
    if request.user.has_perm("account.delete_emailconfirmation"):
        if request.method == "POST":
            object.delete()
            messages.success(request, _(f"Email confirmation {object.email_address} for User {object.email_address.user} deleted!"))
            return JsonResponse({"key": object.pk, "redirect_to": reverse_lazy("emails_confirmations")})
        return HttpResponseNotAllowed(["POST"])
    else:
        return JsonResponse({"pk": None})


class BulkDeleteEmailAddressConfirmationView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = "account.delete_emailconfirmation"

    def post(self, *args, **kwargs):
        selection = self.request.POST.getlist("selection[]")

        if len(selection) > 0:

            objects = EmailConfirmation.objects.filter(pk__in=selection)
            objects.delete()
            messages.success(self.request, _(f"{len(selection)} Email confirmations deleted successfully"))

        else:
            messages.info(self.request, _("No Email confirmations selected"))
        return redirect(reverse_lazy("emails_confirmations"))