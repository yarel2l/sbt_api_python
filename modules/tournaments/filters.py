from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _

from .models import Tournament


class TournamentFilter(filters.FilterSet):
    search = filters.CharFilter(label=_("Search by Tournament Name and Number"), method="search_filter_by")
    status = filters.CharFilter(label=_("Search by Status Id or Status descr"), method="search_filter_by_status")
    organization = filters.CharFilter(method="search_filter_by_organization")
    state = filters.CharFilter(method="search_filter_by_state")
    smsid = filters.CharFilter(method="search_filter_by_smsid")
    startdate = filters.DateFromToRangeFilter(field_name="startdate")
    enddate = filters.DateFromToRangeFilter(field_name="startdate")

    class Meta:
        model = Tournament
        fields = ('search', 'status', 'organization', 'state', 'smsid', 'startdate', 'enddate')

    def search_filter_by(self, queryset, name, value):
        return (
            queryset.filter(name__icontains=value) |
            queryset.filter(tournament_number__icontains=value)
        )

    def search_filter_by_status(self, queryset, name, value):
        return (
            queryset.filter(status__statusid__exact=value) |
            queryset.filter(status__statusdesc__exact=value)
        )

    def search_filter_by_organization(self, queryset, name, value):
        return (
            queryset.filter(organization__name__icontains=value) |
            queryset.filter(organization__shortname__icontains=value)
        )

    def search_filter_by_state(self, queryset, name, value):
        return (
            queryset.filter(state__state__exact=value)
        )

    def search_filter_by_smsid(self, queryset, name, value):
        return (
            queryset.filter(smsid__smsid__exact=value) |
            queryset.filter(smsid__smsphoneid__exact=value) |
            queryset.filter(smsid__smsphone__exact=value) |
            queryset.filter(smsid__descrip__exact=value)
        )