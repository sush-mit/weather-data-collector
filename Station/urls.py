from django.urls import path
from . import views


urlpatterns = [
    path("station/input", views.station, name="station_data"),
    path("station/", views.station, name="station_input"),
    path("station/delete/<int:id>", views.station, name="station_delete"),
]