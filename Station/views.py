from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, redirect
from .forms import StationInputForm
from .models import Station
from django.contrib import messages
from django.views.generic import CreateView

def station(request, uname=None, id_=None):
    if request.user.is_authenticated:
      # if 'input' in request.path:
      #   return station_input(request,uname)
      if 'delete' in request.path:
        return station_delete(request, uname, id_)
      elif 'delete' in request.path:
        return station_edit(request, uname, id_)
      else:
        return station_data(request)
    else:    
      return HttpResponseForbidden()
  
def station_data(request):
  data = Station.objects.filter(user=request.user)
  return render(request, "Station/data.html", {"data": data})

class StationInputView(CreateView):
    model = Station
    fields = ("name", "country", "city", "latitude", "longitude")
    template_name = "Station/input.html"
    
    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)
  

# def station_input(request, uname):
#       if request.method == "POST":
#           form = StationInputForm(request.POST)
#           if form.is_valid():
#               form.save()
#               return redirect(f"/{uname}/station")
#           else:
#             return HttpResponseBadRequest()
#       form = StationInputForm()
#       return render(request, "Station/input.html", {"form": form})

def station_edit(request, uname, id_):
  data_to_edit = Station.objects.get(id=id_)
  data = Station.objects.all()
  return redirect(f"/{uname}/station")

def station_delete(request, uname, id_):
    data_to_delete = Station.objects.get(id=id_)
    data_to_delete.delete()
    data = Station.objects.all()
    return redirect(f"/{uname}/stations")