from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.http import HttpResponse
from .models import Sighting

def index(request):
    context = {
            'sightings': sightings
            }
    return render(request, 'sightings/home.html', context)

class SightingListView(ListView):
    model = Sighting
    template_name = 'sightings/home.html'
    context_object_name = 'sightings'

class SightingCreateView(CreateView):
    model = Sighting
    fields = ['Latitude', 
    'Longitude',
    'Unique_Squirrel_ID', 
    'Hectare', 
    'Shift', 
    'Date', 
    'Age', 
    'Primary_Fur_Color', 
    'Location', 
    'Specific_Location', 
    'Running', 
    'Chasing', 
    'Climbing', 
    'Eating', 
    'Foraging', 
    'Other_Activities', 
    'Kuks',
     'Quaas', 'Moans', 'Tail_flags', 'Tail_twiches', 'Indifferent', 'Runs_from']


def create(request):
    return HttpResponse("Hello")
