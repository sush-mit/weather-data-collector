from django.urls import path
from . import views
# from .views import StationInputView


urlpatterns = [
    path("<str:uname>/stations/", views.station, name="station_data"),
    path("<str:uname>/stations/input", views.station, name="station_input"),
    path("<str:uname>/stations/delete/<int:id_>", views.station, name="station_delete"),
]