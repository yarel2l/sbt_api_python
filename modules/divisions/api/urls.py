from django.urls import path

from .views import (
    DivisionsListView
)

urlpatterns = [

    path('', DivisionsListView.as_view(), name='divisions'),

]