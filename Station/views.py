from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.forms import Form
from django.urls.base import reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http.response import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext

from .models import Countries, Station
from .forms import StationInputForm, StationDeleteForm
from .csv_data import CSVData


@login_required(login_url="/login/")
def station_data(request):

    data = Station.objects.filter(user=request.user)
    return render(
        request,
        "Station/data.html",
        {"data": data}
        )


class StationInputView(LoginRequiredMixin, CreateView):
    model = Station
    form_class = StationInputForm
    template_name = "Station/input.html"
    login_url = "/login/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class StationEditView(LoginRequiredMixin, UpdateView):
    model = Station
    form_class = StationInputForm
    template_name = "Station/edit.html"
    login_url = "/login/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required(login_url="/login/")
def station_delete(request, pk):
    if request.method == "POST":
      Station.objects.filter(id=pk).delete()
      return redirect(reverse("station_data"))
    else:
      data = Station.objects.filter(id=pk).values()[0]
      data['country'] = Countries.objects.filter(id=data['country_id'])[0]
      del data['country_id']
      form = StationDeleteForm(initial=data)
      for f in form:
        # form.fields[f.html_name].widget.attrs['readonly'] = True
        form.fields[f.html_name].widget.attrs['disabled'] = True
      return render(
          request,
          "Station/station_confirm_delete.html",
          {"form": form}
          )


def load_cities(request):
    country_id = request.GET.get("country_id")
    cities = [
        city_data["name"]
        for city_data in CSVData.CITIES
        if city_data["country_id"] == country_id
    ]
    return render(
        request, "Station/city_dropdown_list_options.html", {"cities": cities}
    )
