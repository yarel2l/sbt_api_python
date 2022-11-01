from django.urls import path

from .views import UserList, UserDetails

urlpatterns = [

    path('users/', UserList.as_view()),
    path('user/<pk>/', UserDetails.as_view()),
]