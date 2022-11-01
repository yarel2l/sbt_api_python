from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _

from core.constants import SCORBOT_GENDER_CHOICES
from .models import ScorbotDivision


class ScorbotDivisionFilter(filters.FilterSet):
    search = filters.CharFilter(label=_("Search by name"), method="custom_search_filter")
    gender = filters.ChoiceFilter(label=_("Gender"), choices=SCORBOT_GENDER_CHOICES)
    grade = filters.CharFilter(label=_("Search by gradenbr, grade, byage, bygrade"), method="search_filter_by_grade")
    tournament = filters.CharFilter(label=_("Search by Tournament name or number"), method="search_filter_by_tournament")

    class Meta:
        model = ScorbotDivision
        fields = ('search', 'tournament', 'gender', 'grade', 'teamsperpool', 'gamesperpool', 'minimumgames')

    def custom_search_filter(self, queryset, name, value):
        return (
            queryset.filter(name__icontains=value)
        )

    def search_filter_by_tournament(self, queryset, name, value):
        return (
            queryset.filter(tournamentid__tournament_number__icontains=value) |
            queryset.filter(tournamentid__name__icontains=value)
        )

    def search_filter_by_grade(self, queryset, name, value):
        return (
            queryset.filter(gradeid__gradenbr__icontains=value) |
            queryset.filter(gradeid__grade__icontains=value) |
            queryset.filter(gradeid__byage__icontains=value) |
            queryset.filter(gradeid__bygrade__icontains=value)
        )