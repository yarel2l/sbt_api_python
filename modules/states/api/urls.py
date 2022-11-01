from django.urls import path

from .views import (
    StatesListView
)

urlpatterns = [

    path('', StatesListView.as_view(), name='states'),

]