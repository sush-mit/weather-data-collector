from django.http.response import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from .forms import StationInputForm
from .models import StationModel

def station(request, uname=None, id_=None):
    if request.user.is_authenticated:
      if 'input' in request.path:
        return station_input(request,uname)
      elif 'delete' in request.path:
        return station_delete(request, uname, id_)
      elif 'delete' in request.path:
        return station_edit(request, uname, id_)
      else:
        return station_data(request)
    else:    
      return HttpResponseForbidden()
  
def station_data(request):
  data = StationModel.objects.all()
  return render(request, "Station/data.html", {"data": data})

def station_input(request, uname):
      if request.method == "POST":
          form = StationInputForm(request.POST)
          if form.is_valid():
              form.save()

              return redirect(f"/{uname}/station")
      else:
          form = StationInputForm()
      form = StationInputForm()
      return render(request, "Station/input.html", {"form": form})

def station_edit(request, uname, id_):
  data_to_edit = StationModel.objects.get(id=id_)
  data = StationModel.objects.all()
  return redirect(f"/{uname}/station")

def station_delete(request, uname, id_):
    data_to_delete = StationModel.objects.get(id=id_)
    data_to_delete.delete()
    data = StationModel.objects.all()
    return redirect(f"/{uname}/station")