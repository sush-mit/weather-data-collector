from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http.response import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required

from .models import Station


@login_required(login_url="/login/")
def station_data(request):
    if request.user.is_authenticated:
        data = Station.objects.filter(user=request.user)
        return render(request, "Station/data.html", {"data": data})
    else:
        return HttpResponseForbidden()


class StationInputView(LoginRequiredMixin, CreateView):
    model = Station
    template_name = "Station/input.html"
    fields = ("name", "country", "city", "latitude", "longitude")
    login_url = "/login/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class StationEditView(LoginRequiredMixin, UpdateView):
    model = Station
    template_name = "Station/input.html"
    fields = ("name", "country", "city", "latitude", "longitude")
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
