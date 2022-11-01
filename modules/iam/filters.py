import django_filters
from allauth.account.models import EmailAddress, EmailConfirmation
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django_select2.forms import Select2Widget
from django_filters import FilterSet

User = get_user_model()


class UserFilter(FilterSet):
    search = django_filters.CharFilter(label=_("Search"), method="my_custom_filter")
    is_active = django_filters.BooleanFilter(field_name="is_active", label=_('Account Active'),
                                             widget=Select2Widget())
    join_date = django_filters.DateRangeFilter(field_name="date_joined", label=_('Registration Date'),
                                               widget=Select2Widget())
    preferred_language = django_filters.ChoiceFilter(field_name="preferred_language", label=_('Languages'),
                                                     choices=settings.LANGUAGES, widget=Select2Widget)

    class Meta:
        model = User
        fields = ("search", "preferred_language", "is_active", "join_date")

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(Q(username__icontains=value)
                               | Q(email__icontains=value)
                               | Q(mobile__icontains=value)
                               | Q(first_name__icontains=value)
                               )


class EmailAddressFilter(FilterSet):
    search = django_filters.CharFilter(label=_("Search"), method="my_custom_filter")
    verified = django_filters.BooleanFilter(label=_("Verified"), widget=Select2Widget())
    primary = django_filters.BooleanFilter(label=_("Primary"), widget=Select2Widget())

    class Meta:
        model = EmailAddress
        fields = ("search", "verified", "primary")

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(user__first_name__icontains=value) | queryset.filter(user__email__icontains=value) | \
               queryset.filter(user__mobile__icontains=value) | queryset.filter(user__sername__icontains=value) | queryset.filter(email=value)


class EmailAddressConfirmationFilter(FilterSet):
    search = django_filters.CharFilter(label=_("Search"), method="my_custom_filter")
    sent = django_filters.DateRangeFilter(label=_("Sent Date"), widget=Select2Widget())
    created = django_filters.DateRangeFilter(label=_("Created Date"), widget=Select2Widget())

    class Meta:
        model = EmailConfirmation
        fields = ("search", "sent", "created")

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(email_address__icontains=value) | queryset.filter(key__icontains=value)
