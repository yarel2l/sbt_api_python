from django.urls import path, include
from rest_framework import routers

from .views import (
    UserViewSet, UserDetailsView
)

router = routers.DefaultRouter()


router.register("users", UserViewSet, basename="user")


urlpatterns = [
    path("", include(router.urls)),
    path('user/', UserDetailsView.as_view(), name='rest_user_details'),
]
