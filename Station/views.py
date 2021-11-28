from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http.response import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext

from .models import Station
from .forms import StationInputForm
from .csv_data import CSVData


@login_required(login_url="/login/")
def station_data(request):
    if request.user.is_authenticated:
        data = Station.objects.filter(user=request.user)
        return render(request, "Station/data.html", {"data": data})
    else:
        return HttpResponseForbidden()


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


class StationDeleteView(LoginRequiredMixin, DeleteView):
    model = Station
    login_url = "/login/"
    success_url = "/stations/"

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(user=user)


def load_cities(request):
    country_id = request.GET.get("country_id")
    cities = [city_data['name'] for city_data in CSVData.CITIES if city_data['country_id'] == country_id]
    return render(
        request, "Station/city_dropdown_list_options.html", {"cities": cities}
    )