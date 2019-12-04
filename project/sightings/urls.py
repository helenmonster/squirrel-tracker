from django.urls import path
from .views import SightingListView, SightingCreateView
from . import views

urlpatterns = [
        path('', SightingListView.as_view(), name='sightings-home'),
        path('add/',SightingCreateView.as_view(),name='sightings-create'),
]
