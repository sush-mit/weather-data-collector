from django.urls import path
from . import views


urlpatterns = [
    path("station/input", views.station_input, name="station_input"),
    path("station/", views.station_input, name="station_input"),
]