from django.contrib import admin
from sightings.apps import SightingsConfig
from .models import Sighting
admin.site.register(Sighting)
