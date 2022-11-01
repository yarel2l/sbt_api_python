from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _

from .models import ScorbotSMSPhone


class ScorbotSMSPhoneFilter(filters.FilterSet):
    search = filters.CharFilter(label=_("Search by smsid, smsphoneid, smsphone, title, descrip"), method="custom_search_filter")
    active = filters.BooleanFilter(label=_("Active"), field_name="active")
    organization = filters.CharFilter(method="search_filter_by_organization")
    effectiveyear = filters.DateFromToRangeFilter(field_name="effectiveyear")

    class Meta:
        model = ScorbotSMSPhone
        fields = ('search', 'active', 'organization', 'effectiveyear')

    def custom_search_filter(self, queryset, name, value):
        return (
            queryset.filter(smsid__icontains=value) |
            queryset.filter(smsphoneid__icontains=value) |
            queryset.filter(smsphone__icontains=value) |
            queryset.filter(title__icontains=value) |
            queryset.filter(descrip__icontains=value)
        )

    def search_filter_by_organization(self, queryset, name, value):
        return (
            queryset.using("scorbot").filter(organization__name__icontains=value) |
            queryset.using("scorbot").filter(organization__shortname__icontains=value)
        )