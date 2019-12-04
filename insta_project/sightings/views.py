from django.shortcuts import render


def home(request):
    return render(request, 'sightings/home.html')

def add(request):
    return render(request, 'sightings/add.html')

def stats(request):
    return render(request, 'sightings/stats.html')

def squirrel(request):
    return render(request, 'sightings/squirrel.html')















