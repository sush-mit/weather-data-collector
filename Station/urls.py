from django.urls import path
from . import views


urlpatterns = [
    path("<str:uname>/station/", views.station, name="station_data"),
    path("<str:uname>/station/input", views.station, name="station_input"),
    path("<str:uname>/station/delete/<int:id_>", views.station, name="station_delete"),
]