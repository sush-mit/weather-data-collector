from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http.response import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required

from .models import WeatherData

@login_required(login_url="/login/")
def weather_data_data(request, station_id):
        data = WeatherData.objects.filter(user=request.user).filter(station=station_id)
        return render(
            request,
            "WeatherData/data.html",
            {"data": data},
        )

class WeatherDataInputView(LoginRequiredMixin, CreateView):
    model = WeatherData
    template_name = "WeatherData/input.html"
    login_url = "/login/"
    fields = '__all__'


class WeatherDataEditView(LoginRequiredMixin, UpdateView):
    model = WeatherData
    template_name = "WeatherData/edit.html"
    login_url = "/login/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.station = 1
        return super().form_valid(form)


class WeatherDataDeleteView(LoginRequiredMixin, DeleteView):
    model = WeatherData
    login_url = "/login/"
    success_url = "/stations/"

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(user=user)