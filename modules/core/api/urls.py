from django.urls import path

from .views import (
    TimezoneListView,
    GradesListView,
    StatusListView,
    EventTypeListView,
)

urlpatterns = [

    path('timezone/', TimezoneListView.as_view(), name='timezones'),
    path('grade/', GradesListView.as_view(), name='grades'),
    path('status/', StatusListView.as_view(), name='status'),
    path('event-type/', EventTypeListView.as_view(), name='event-type'),


]