from django.http.response import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from .forms import StationInputForm
from .models import StationModel

def station(request):
    if request.user.is_authenticated:
      if 'input' in request.path:
        station_input(request)
      elif 'delete' in request.path:
        station_delete(request)
      else:
        station_data(request)
    else:    
      return HttpResponseForbidden()
  
def station_data(request):
  data = StationModel.objects.all()
  return render(request, "Station/data.html", {"data": data})

def station_input(request):
      if request.method == "POST":
          form = StationInputForm(request.POST)
          if form.is_valid():
              form.save()

              return redirect("/station")
      else:
          form = StationInputForm()
      form = StationInputForm()
      return render(request, "Station/input.html", {"form": form})

def station_delete(request, id):
    data_to_delete = StationModel.objects.get(id=id)
    data_to_delete.delete()
    data = StationModel.objects.all()
    return redirect("/station")