from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http.response import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required

from .models import WeatherData
from Station.models import Station
from .forms import WeatherDataDeleteForm, WeatherDataInputForm


@login_required(login_url="/login/")
def weather_data_data(request):
    data = WeatherData.objects.filter(user=request.user)
    return render(
        request,
        "WeatherData/data.html",
        {"data": data},
    )


class WeatherDataInputView(LoginRequiredMixin, CreateView):
    model = WeatherData
    form_class = WeatherDataInputForm
    template_name = "WeatherData/input.html"
    login_url = "/login/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        temperature_f = (form.instance.temperature_c * 9 / 5) + 32
        form.instance.temperature_f = temperature_f
        del temperature_f
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(WeatherDataInputView, self).get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs


class WeatherDataEditView(LoginRequiredMixin, UpdateView):
    model = WeatherData
    form_class = WeatherDataInputForm
    template_name = "WeatherData/edit.html"
    login_url = "/login/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        temperature_f = (form.instance.temperature_c * 9 / 5) + 32
        form.instance.temperature_f = temperature_f
        del temperature_f
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(WeatherDataEditView, self).get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs


@login_required(login_url="/login/")
def weather_data_delete(request, pk):
    if request.method == "POST":
        data = WeatherData.objects.filter(id=pk).delete()
        return redirect(reverse("weather_data_data"))
    else:
        data = WeatherData.objects.filter(id=pk).values()[0]
        form = WeatherDataDeleteForm(initial=data)
        for f in form:
            # form.fields[f.html_name].widget.attrs['readonly'] = True
            form.fields[f.html_name].widget.attrs["disabled"] = True
        return render(
            request, "WeatherData/weatherdata_confirm_delete.html", {"form": form}
        )
