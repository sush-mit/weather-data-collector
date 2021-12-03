from django.urls import path
from django.views.generic.edit import DeleteView
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import StationInputView, StationEditView, StationDeleteView


urlpatterns = [
    path("stations/", views.station_data, name="station_data"),
    path("stations/input", StationInputView.as_view(), name="station_input"),
    path(
        "stations/<int:pk>/delete/", StationDeleteView.as_view(), name="station_delete"
    ),
    path("stations/<int:pk>/edit/", StationEditView.as_view(), name="station_edit"),
    path(
        "stations/input/ajax/load-cities/", views.load_cities, name="ajax_load_cities"
    ),
    path(
        "stations/?sort_by=name&order=desc",
        views.station_data,
        name="station_data_name_desc",
    ),
    path(
        "stations/?sort_by=name&order=asc",
        views.station_data,
        name="station_data_name_asc",
    ),
    path(
        "stations/?sort_by=country&order=desc",
        views.station_data,
        name="station_data_country_desc",
    ),
    path(
        "stations/?sort_by=country&order=asc",
        views.station_data,
        name="station_data_country_asc",
    ),
    path(
        "stations/?sort_by=city&order=desc",
        views.station_data,
        name="station_data_city_desc",
    ),
    path(
        "stations/?sort_by=city&order=asc",
        views.station_data,
        name="station_data_city_asc",
    ),
    path(
        "stations/?sort_by=date_created&order=desc",
        views.station_data,
        name="station_data_created_desc",
    ),
    path(
        "stations/?sort_by=date_created&order=asc",
        views.station_data,
        name="station_data_created_asc",
    ),
    path(
        "stations/?sort_by=date_updated&order=desc",
        views.station_data,
        name="station_data_updated_desc",
    ),
    path(
        "stations/?sort_by=date_updated&order=asc",
        views.station_data,
        name="station_data_updated_asc",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
