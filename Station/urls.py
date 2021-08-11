from django.urls import path
from . import views


urlpatterns = [
    path("station/input", views.station_input, name="station_input"),
    path("station/", views.station_data, name="station_data"),
    path("station/delete/<int:id>", views.station_delete, name="station_delete"),
]