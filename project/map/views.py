from django.shortcuts import render
from django.http import HttpResponse
from .models import Sighting

sightings = [
         {
    "X": -73.9584071,
    "Y": 40.79138125
  },
  {
    "X": -73.96711307,
    "Y": 40.77848597
  },
  {
    "X": -73.9649866,
    "Y": 40.77649297
  },
  {
    "X": -73.96706286,
    "Y": 40.77349914
  },
]

def index(request):
    content = {
            'sightings': sightings
            }
    return render(request,'map/map.html',content)
