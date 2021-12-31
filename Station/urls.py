from django.urls import path
from django.views.generic.edit import DeleteView
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import StationInputView, StationEditView, station_dashboard_view


urlpatterns = [
    path("stations/", views.station_data, name="station_data"),
    path("stations/add", StationInputView.as_view(), name="station_input"),
    path("stations/<int:pk>/delete/", views.station_delete, name="station_delete"),
    path("stations/<int:pk>/edit/", StationEditView.as_view(), name="station_edit"),
    path(
        "stations/input/ajax/load-cities/", views.load_cities, name="ajax_load_cities"
    ),
    path(
        "stations/<int:station_id>/dashboard/",
        station_dashboard_view,
        name="station_dashboard",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
