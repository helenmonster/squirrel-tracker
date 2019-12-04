from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sightings'),
    path('add/', views.add, name='sightings-add'),
    path('stats/', views.stats, name='sightings-stats'),
    path('<unique-squirrel-id>/', views.squirrel, name='sightings-unique-squirrel-id'),
]











