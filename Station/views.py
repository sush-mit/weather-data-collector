import calendar
from datetime import datetime, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse
from django.views.generic import CreateView, UpdateView
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

from .models import Countries, Station
from WeatherData.models import WeatherData
from .forms import StationInputForm, StationDeleteForm
from .csv_data import CSVData


@login_required(login_url="/login/")
def station_data(request):

    data = Station.objects.filter(user=request.user)
    return render(request, "Station/data.html", {"data": data})


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
        data["country"] = Countries.objects.filter(id=data["country_id"])[0]
        del data["country_id"]
        form = StationDeleteForm(initial=data)
        for f in form:
            # form.fields[f.html_name].widget.attrs['readonly'] = True
            form.fields[f.html_name].widget.attrs["disabled"] = True
        return render(request, "Station/station_confirm_delete.html", {"form": form})


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


@login_required(login_url="/login/")
def station_dashboard_view(request, station_id):
    tf = request.GET.get("tf")
    if tf == "day" or not tf:
        return station_dashboard_day(request, station_id)
    if tf == "week":
        return station_dashboard_week(request, station_id)
    if tf == "month":
        return station_dashboard_month(request, station_id)
    if tf == "year":
        return station_dashboard_year(request, station_id)


def station_dashboard_day(request, station_id):
    station = Station.objects.filter(user=request.user).get(id=station_id)
    # test_date = datetime.today() - timedelta(days=1)
    hours = set(
        query.date_time.hour
        for query in WeatherData.objects.filter(station=station).filter(
            date_time__startswith=datetime.today().date()
        )
    )
    avg_temperatures_c = [
        avg_temperature_c
        for hour in hours
        for avg_temperature_c in WeatherData.objects.filter(station=station)
        .filter(date_time__startswith=datetime.today().date())
        .filter(date_time__hour=hour).aggregate(Avg('temperature_c')).values()
    ]
    if avg_temperatures_c == [] or hours == set():
        data_not_found(request)
    data = {"temperatures_c": avg_temperatures_c, "hours": hours}
    return render(request, "Station/station_dashboard_day.html", {"data": data})


def station_dashboard_week(request, station_id):
    one_week_ago = datetime.today() - timedelta(days=7)
    station = Station.objects.filter(user=request.user).get(id=station_id)
    week_days = set(
        query.date_time.weekday()
        for query in WeatherData.objects.filter(station=station).filter(
            date_time__gte=one_week_ago
        )
    )
    avg_temperatures_c = [
        avg_temperature_c
        for week_day in week_days
        for avg_temperature_c in WeatherData.objects.filter(station=station)
        .filter(date_time__gte=one_week_ago)
        .filter(date_time__week_day=abs(week_day - 7)).aggregate(Avg('temperature_c')).values()
    ] # abs(week_day - 7) because django stores the days from 1(sunday)-7(saturday) unlike the usual 0(monday)-6(sunday)
    week_days = [calendar.day_abbr[week_day] for week_day in week_days]
    if avg_temperatures_c == [] or week_days == set():
        data_not_found(request)
    data = {"temperatures_c": avg_temperatures_c, "week_days": week_days}
    return render(request, "Station/station_dashboard_week.html", {"data": data})


def station_dashboard_month(request, station_id):
    station = Station.objects.filter(user=request.user).get(id=station_id)
    days = set(
        query.date_time.day
        for query in WeatherData.objects.filter(station=station).filter(
            date_time__month=datetime.today().month
        )
    )
    avg_temperatures_c = [
        avg_temperature_c
        for day in days
        for avg_temperature_c in WeatherData.objects.filter(station=station)
        .filter(date_time__month=datetime.today().month)
        .filter(date_time__day=day).aggregate(Avg('temperature_c')).values()
    ]
    if avg_temperatures_c == [] or days == set():
        data_not_found(request)
    data = {"temperatures_c": avg_temperatures_c, "days": days}
    return render(request, "Station/station_dashboard_month.html", {"data": data})

def station_dashboard_year(request, station_id):
    station = Station.objects.filter(user=request.user).get(id=station_id)
    months = set(
        query.date_time.month
        for query in WeatherData.objects.filter(station=station).filter(
            date_time__year=datetime.today().year
        )
    )
    avg_temperatures_c = [
        avg_temperature_c
        for month in months
        for avg_temperature_c in WeatherData.objects.filter(station=station)
        .filter(date_time__year=datetime.today().year)
        .filter(date_time__month=month).aggregate(Avg('temperature_c')).values()
    ]
    months = [calendar.month_abbr[month] for month in months]
    if avg_temperatures_c == [] or months == set():
        data_not_found(request)
    data = {"temperatures_c": avg_temperatures_c, "months": months}
    return render(request, "Station/station_dashboard_year.html", {"data": data})


def data_not_found(request):
    pass
