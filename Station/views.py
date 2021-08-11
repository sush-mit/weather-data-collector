from django.shortcuts import render
from .forms import StationInputForm

def station_input(request):
    form = StationInputForm()
    return render(request, "Station/input.html", {"form": form})