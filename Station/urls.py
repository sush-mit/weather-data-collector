from django.urls import path
from . import views
from .views import StationInputView


urlpatterns = [
    path("stations/", views.station, name="station_data"),
    path("stations/input", StationInputView.as_view(), name="station_input"),
    path("stations/<int:id_>/delete/", views.station, name="station_delete"),
    path("stations/<int:id_>/edit/", views.station, name="station_edit"),
]