import django_tables2 as tables
from allauth.account.models import EmailAddress, EmailConfirmation
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django_tables2 import A
from django_tables2.utils import AttributeDict

ACTIONS_ATTR = {"th": {"class": "text-center"}, "td": {"class": "text-center"}}
SELECTION_ATTR = {'class': "form-check-input widget-13-check"}

User = get_user_model()


class CustomCheckboxColumn(tables.columns.CheckBoxColumn):

    @property
    def header(self):
        default = {"type": "checkbox"}

        general = self.attrs.get("input")
        specific = self.attrs.get("th__input")
        attrs = AttributeDict(default, **(specific or general or {}))

        input = "<input class='form-check-input' type='checkbox' data-kt-check='true' data-kt-check-target='.widget-13-check'>"  #% attrs.as_html()
        header_attrs = AttributeDict(SELECTION_ATTR)
        label = f"<div class='form-check form-check-sm form-check-custom form-check-solid'>{input}</div>"

        return mark_safe(label)

    def render(self, value, bound_column, record):
        input = super(CustomCheckboxColumn, self).render(value, bound_column, record)
        # include span
        # input = input #+ "<span></span>"
        input = "<input class='form-check-input widget-13-check' type='checkbox' name='selection' value="+str(record.pk)+">"
        attrs = AttributeDict(SELECTION_ATTR)
        # label = f"<label {attrs.as_html()}>{input}</label>"
        label = f"<div class='form-check form-check-sm form-check-custom form-check-solid'>{input}</div>"

        return mark_safe(label)


class Selection(tables.Table):
    selection = CustomCheckboxColumn(accessor="id")


class TranslatedTable(tables.Table):
    def __init__(self, *args, **kwargs):
        super(TranslatedTable, self).__init__(*args, **kwargs)
        for column in self.base_columns:
            verbose = self.base_columns[column].verbose_name
            if verbose:
                self.base_columns[column].verbose_name = _(verbose)
            else:
                self.base_columns[column].verbose_name = _(column)


class UserTable(Selection):

    account = tables.columns.TemplateColumn(verbose_name=_("Account"),
                                            template_name="iam/users/table/table_account.html",
                                            order_by=("first_name", "last_name", "email", "username")
                                            )

    auth_token = tables.columns.TemplateColumn(
        verbose_name=_("Auth Token"),
        template_name="iam/users/table/table_token.html",
        order_by=("auth_token",)
    )

    is_active = tables.columns.TemplateColumn(
        verbose_name=_("Status"),
        template_name="iam/users/table/table_boolean.html",
        order_by=("is_active",)
    )
    actions = tables.columns.TemplateColumn(
        verbose_name=_("Actions"), template_name="iam/users/table/table_actions.html", orderable=False
    )

    class Meta:
        model = User
        fields = ("selection", "account", "auth_token", "is_active", "actions")


class EmailAddressTable(Selection):
    user = tables.columns.RelatedLinkColumn()
    actions = tables.columns.TemplateColumn(
        verbose_name=_("Actions"), template_name="iam/emails/table/table_actions.html",
        orderable=False,
        attrs=ACTIONS_ATTR
    )

    class Meta:
        model = EmailAddress
        fields = ("selection", "user", "email", "primary", "verified", "actions")


class EmailAddressConfirmationTable(Selection):
    email_address = tables.columns.LinkColumn("emails_confirmations_edit", args=[A('pk')],
                                              verbose_name=_("Email address"))
    actions = tables.columns.TemplateColumn(
        verbose_name=_("Actions"), template_name="iam/email_confirmation/table/table_actions.html",
        orderable=False,
        attrs=ACTIONS_ATTR
    )

    class Meta:
        model = EmailConfirmation
        fields = ("selection", "email_address", "key", "sent", "actions")