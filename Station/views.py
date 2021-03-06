import calendar
from datetime import datetime, timedelta

from django.utils import timezone
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
    # test_date = timezone.now() - timedelta(days=1)
    hours = set(
        query.date_time.hour
        for query in WeatherData.objects.filter(station=station).filter(
            date_time__startswith=timezone.now().date()
        )
    )
    avg_temperatures_c, avg_humidity, avg_clouds, avg_windspeeds = get_average_day(
        hours=hours, station=station
    )
    data = {
        "temperatures_c": avg_temperatures_c,
        "humidity": avg_humidity,
        "clouds": avg_clouds,
        "windspeeds": avg_windspeeds,
        "hours": hours,
    }
    return render(request, "Station/station_dashboard_day.html", {"data": data})


def station_dashboard_week(request, station_id):
    station = Station.objects.filter(user=request.user).get(id=station_id)
    one_week_ago = timezone.now() - timedelta(days=7)
    week_days = set(
        query.date_time.weekday()
        for query in WeatherData.objects.filter(station=station).filter(
            date_time__gte=one_week_ago
        )
    )
    avg_temperatures_c, avg_humidity, avg_clouds, avg_windspeeds = get_average_week(
        one_week_ago=one_week_ago, week_days=week_days, station=station
    )
    week_days = [calendar.day_abbr[week_day] for week_day in week_days]
    data = {
        "temperatures_c": avg_temperatures_c,
        "humidity": avg_humidity,
        "clouds": avg_clouds,
        "windspeeds": avg_windspeeds,
        "week_days": week_days,
    }
    return render(request, "Station/station_dashboard_week.html", {"data": data})


def station_dashboard_month(request, station_id):
    station = Station.objects.filter(user=request.user).get(id=station_id)
    days = set(
        query.date_time.day
        for query in WeatherData.objects.filter(station=station).filter(
            date_time__month=timezone.now().month
        )
    )
    avg_temperatures_c, avg_humidity, avg_clouds, avg_windspeeds = get_average_month(
        days=days, station=station
    )
    week_days = [calendar.day_abbr[day] for day in days]

    data = {
        "temperatures_c": avg_temperatures_c,
        "humidity": avg_humidity,
        "clouds": avg_clouds,
        "windspeeds": avg_windspeeds,
        "week_days": week_days,
    }
    return render(request, "Station/station_dashboard_month.html", {"data": data})


def station_dashboard_year(request, station_id):
    station = Station.objects.filter(user=request.user).get(id=station_id)
    months = set(
        query.date_time.month
        for query in WeatherData.objects.filter(station=station).filter(
            date_time__year=timezone.now().year
        )
    )
    avg_temperatures_c, avg_humidity, avg_clouds, avg_windspeeds = get_average_year(
        months=months, station=station
    )
    months = [calendar.month_abbr[month] for month in months]
    data = {
        "temperatures_c": avg_temperatures_c,
        "humidity": avg_humidity,
        "clouds": avg_clouds,
        "windspeeds": avg_windspeeds,
        "months": months,
    }
    return render(request, "Station/station_dashboard_year.html", {"data": data})


def get_average_day(hours, station):
    avg_temperatures_c = [
        float(avg_temperature_c)
        for hour in hours
        for avg_temperature_c in WeatherData.objects.filter(station=station)
        .filter(date_time__startswith=timezone.now().date())
        .filter(date_time__hour=hour)
        .aggregate(Avg("temperature_c"))
        .values()
    ]
    avg_humidity = [
        float(avg_hum)
        for hour in hours
        for avg_hum in WeatherData.objects.filter(station=station)
        .filter(date_time__startswith=timezone.now().date())
        .filter(date_time__hour=hour)
        .aggregate(Avg("humidity"))
        .values()
    ]
    avg_clouds = [
        float(avg_clds)
        for hour in hours
        for avg_clds in WeatherData.objects.filter(station=station)
        .filter(date_time__startswith=timezone.now().date())
        .filter(date_time__hour=hour)
        .aggregate(Avg("cloud"))
        .values()
    ]
    avg_windspeeds = [
        float(avg_wnds)
        for hour in hours
        for avg_wnds in WeatherData.objects.filter(station=station)
        .filter(date_time__startswith=timezone.now().date())
        .filter(date_time__hour=hour)
        .aggregate(Avg("wind_kph"))
        .values()
    ]
    return avg_temperatures_c, avg_humidity, avg_clouds, avg_windspeeds


def get_average_week(one_week_ago, week_days, station):
    avg_temperatures_c = [
        float(avg_temperature_c)
        for week_day in week_days
        for avg_temperature_c in WeatherData.objects.filter(station=station)
        .filter(date_time__gte=one_week_ago)
        .filter(date_time__iso_week_day=week_day + 1)
        .aggregate(Avg("temperature_c"))
        .values()
    ]  # week_day + 1 because iso_week_day names week days from 1 - 7 (Mon - Sat) unlike python's 0 - 6 (Mon - Sun)
    avg_humidity = [
        float(avg_hum)
        for week_day in week_days
        for avg_hum in WeatherData.objects.filter(station=station)
        .filter(date_time__gte=one_week_ago)
        .filter(date_time__iso_week_day=week_day + 1)
        .aggregate(Avg("humidity"))
        .values()
    ]
    avg_clouds = [
        float(avg_clds)
        for week_day in week_days
        for avg_clds in WeatherData.objects.filter(station=station)
        .filter(date_time__gte=one_week_ago)
        .filter(date_time__iso_week_day=week_day + 1)
        .aggregate(Avg("cloud"))
        .values()
    ]
    avg_windspeeds = [
        float(avg_wnds)
        for week_day in week_days
        for avg_wnds in WeatherData.objects.filter(station=station)
        .filter(date_time__gte=one_week_ago)
        .filter(date_time__iso_week_day=week_day + 1)
        .aggregate(Avg("wind_kph"))
        .values()
    ]

    return avg_temperatures_c, avg_humidity, avg_clouds, avg_windspeeds


def get_average_month(days, station):
    avg_temperatures_c = [
        float(avg_temperature_c)
        for day in days
        for avg_temperature_c in WeatherData.objects.filter(station=station)
        .filter(date_time__month=timezone.now().month)
        .filter(date_time__day=day)
        .aggregate(Avg("temperature_c"))
        .values()
    ]
    avg_humidity = [
        float(avg_hum)
        for day in days
        for avg_hum in WeatherData.objects.filter(station=station)
        .filter(date_time__month=timezone.now().month)
        .filter(date_time__day=day)
        .aggregate(Avg("humidity"))
        .values()
    ]
    avg_clouds = [
        float(avg_clds)
        for day in days
        for avg_clds in WeatherData.objects.filter(station=station)
        .filter(date_time__month=timezone.now().month)
        .filter(date_time__day=day)
        .aggregate(Avg("cloud"))
        .values()
    ]
    avg_windspeeds = [
        float(avg_wnds)
        for day in days
        for avg_wnds in WeatherData.objects.filter(station=station)
        .filter(date_time__month=timezone.now().month)
        .filter(date_time__day=day)
        .aggregate(Avg("wind_kph"))
        .values()
    ]
    return avg_temperatures_c, avg_humidity, avg_clouds, avg_windspeeds


def get_average_year(months, station):
    avg_temperatures_c = [
        float(avg_temperature_c)
        for month in months
        for avg_temperature_c in WeatherData.objects.filter(station=station)
        .filter(date_time__year=timezone.now().year)
        .filter(date_time__month=month)
        .aggregate(Avg("temperature_c"))
        .values()
    ]
    avg_humidity = [
        float(avg_hum)
        for month in months
        for avg_hum in WeatherData.objects.filter(station=station)
        .filter(date_time__year=timezone.now().year)
        .filter(date_time__month=month)
        .aggregate(Avg("humidity"))
        .values()
    ]
    avg_clouds = [
        float(avg_clds)
        for month in months
        for avg_clds in WeatherData.objects.filter(station=station)
        .filter(date_time__year=timezone.now().year)
        .filter(date_time__month=month)
        .aggregate(Avg("cloud"))
        .values()
    ]
    avg_windspeeds = [
        float(avg_wnds)
        for month in months
        for avg_wnds in WeatherData.objects.filter(station=station)
        .filter(date_time__year=timezone.now().year)
        .filter(date_time__month=month)
        .aggregate(Avg("wind_kph"))
        .values()
    ]
    return avg_temperatures_c, avg_humidity, avg_clouds, avg_windspeeds
