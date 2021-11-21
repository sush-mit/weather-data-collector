from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.http.response import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import render, redirect
from .forms import StationInputForm
from .models import Station

def station(request, uname=None, id_=None):
    if request.user.is_authenticated:
      if not uname == request.user.username:
        return HttpResponseNotFound()
      if 'input' in request.path:
        return station_input(request, uname)
      elif 'delete' in request.path:
        return station_delete(request, uname, id_)
      elif 'edit' in request.path:
        return station_edit(request, uname, id_)
      else:
        return station_data(request, uname)
    else:    
      return HttpResponseForbidden()
  
def station_data(request, uname):
  data = Station.objects.filter(user=request.user)
  return render(request, "Station/data.html", {"data": data})

# def station_input(request, uname):
#       if request.method == "POST":
#           form = StationInputForm(request.POST)
#           form.instance.user = request.user
#           if form.is_valid():
#               form.save()
#               return redirect(f"/{uname}/stations")
#           else:
#             return HttpResponseBadRequest()
#       form = StationInputForm()
#       return render(request, "Station/input.html", {"form": form})
    
class StationInputView(LoginRequiredMixin, CreateView):
  model = Station
  template_name = 'Station/input.html'
  fields = ('name', 'country', 'city', 'latitude', 'longitude')
  login_url = "/login/"
  
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

def station_edit(request, uname, id_):
  data_to_edit = Station.objects.get(id=id_)
  data = Station.objects.all()
  return redirect(f"/{uname}/station")

def station_delete(request, uname, id_):
    data_to_delete = Station.objects.get(id=id_)
    data_to_delete.delete()
    data = Station.objects.all()
    return redirect(f"/{uname}/stations")