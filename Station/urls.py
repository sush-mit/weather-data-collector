from django.urls import path
from . import views
# from .views import StationInputView


urlpatterns = [
    path("<str:uname>/stations/", views.station, name="station_data"),
    path("<str:uname>/stations/input", views.station, name="station_input"),
    path("<str:uname>/stations/<int:id_>/delete/", views.station, name="station_delete"),
    path("<str:uname>/stations/<int:id_>/edit/", views.station, name="station_edit"),
]