from django.shortcuts import render, redirect
from .forms import StationInputForm
from .models import StationModel

def station_data(request):
    data = StationModel.objects.all()
    return render(request, "Station/data.html", {"data": data})

def station_input(request):
    if request.method == "POST":
        form = StationInputForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(f"/station")
    else:
        form = StationInputForm()
    form = StationInputForm()
    return render(request, "Station/input.html", {"form": form})