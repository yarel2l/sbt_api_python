from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _
from django_select2.forms import Select2Widget

from core.constants import SCORBOT_GENDER_CHOICES
from states.models import ScorbotState
from .models import TeamCoach


class TeamCoachFilter(filters.FilterSet):
    search = filters.CharFilter(label=_("Search by team name"), method="search_filter_by")
    gender = filters.ChoiceFilter(label=_("Gender"), choices=SCORBOT_GENDER_CHOICES)
    coach = filters.CharFilter(label=_("Search by name, phone or email"), method="search_filter_by_coach")
    stateid = filters.ModelChoiceFilter(queryset=ScorbotState.objects.all(), widget=Select2Widget())
    createdt = filters.DateFromToRangeFilter(field_name="createdt", label=_("Registration Date"))
    event = filters.CharFilter(label=_("Event"), method="search_filter_by_tournament")

    class Meta:
        model = TeamCoach
        fields = ('search', 'gender', 'coach', 'stateid', 'createdt', 'yboa_id', 'event')

    def search_filter_by(self, queryset, name, value):
        return (
            queryset.filter(teamname__icontains=value) |
            queryset.filter(id__icontains=value)
        )

    def search_filter_by_coach(self, queryset, name, value):
        return (
            queryset.filter(coachname__exact=value) |
            queryset.filter(coachphone__exact=value) |
            queryset.filter(coachemail__exact=value)
        )

    def search_filter_by_tournament(self, queryset, name, value):
        return (
            queryset.filter(teamscoach_tournaments__tournamentid__event_number__icontains=value) |
            queryset.filter(teamscoach_tournaments__tournamentid__name__icontains=value)
        )