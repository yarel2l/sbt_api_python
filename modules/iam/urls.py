from django.urls import path

from .views import (
    ManageUsersView, UserCreateView, AccountInformationView, CustomPasswordChangeView, DeactivateAccountView,
    UserPermissionsView, delete_user_account_view, BulkDeleteAccountsView, ManageEmailsView,
    EmailAddressCreateView, EmailAddressUpdateView, delete_email_address, BulkDeleteEmailAddressView,
    ManageEmailsConfirmationView, EmailAddressConfirmationCreateView, EmailAddressConfirmationUpdateView,
    delete_email_address_confirmation_view, BulkDeleteEmailAddressConfirmationView,
    change_user_language_view,
    AccountProfileSettingsView
)

urlpatterns = [
    path("language/", change_user_language_view, name="change_site_language"),

    path("users/", ManageUsersView.as_view(), name="users_list"),
    path("users/new/", UserCreateView.as_view(), name="users_new"),
    path("users/bulk/remove/", BulkDeleteAccountsView.as_view(), name="bulk_delete"),

    path("user/<uid>/information/", AccountInformationView.as_view(), name="account_information"),
    path("user/<uid>/password/", CustomPasswordChangeView.as_view(), name="password_change_view"),
    path("user/<uid>/deactivate/", DeactivateAccountView.as_view(), name="account_deactivate_view"),
    path("user/<uid>/permissions/", UserPermissionsView.as_view(), name="account_permissions"),
    path("user/<uid>/settings/", AccountProfileSettingsView.as_view(), name="account_profile"),
    path("user/<uid>/delete/", delete_user_account_view, name="account_delete"),

    path("emails/", ManageEmailsView.as_view(), name="emails"),
    path("emails/new/", EmailAddressCreateView.as_view(), name="emails_new"),
    path("emails/<pk>/edit/", EmailAddressUpdateView.as_view(), name="emails_edit"),
    path("emails/<pk>/delete/", delete_email_address, name="emails_delete"),
    path("emails/bulk/remove/", BulkDeleteEmailAddressView.as_view(), name="emails_delete_bulk"),

    path("emails/confirmation/", ManageEmailsConfirmationView.as_view(), name="emails_confirmations"),
    path("emails/confirmation/new/", EmailAddressConfirmationCreateView.as_view(), name="emails_confirmations_new"),
    path("emails/confirmation/<pk>/edit/", EmailAddressConfirmationUpdateView.as_view(), name="emails_confirmations_edit"),
    path("emails/confirmation/<pk>/delete/", delete_email_address_confirmation_view, name="emails_confirmations_delete"),
    path("emails/confirmation/bulk/remove/", BulkDeleteEmailAddressConfirmationView.as_view(), name="emails_confirmations_delete_bulk"),

]