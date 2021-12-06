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
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
