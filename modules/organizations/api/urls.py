from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    OrganizationsView,
    SMSPhoneListView
)
router = DefaultRouter()

router.register("", OrganizationsView, basename="organization")


urlpatterns = [
    path("", include(router.urls)),
    # path('smsid/', SMSPhoneListView.as_view(), name='smsid'),
]