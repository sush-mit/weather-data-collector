from django.urls import path
from django.views.generic.edit import DeleteView
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import WeatherDataInputView, WeatherDataEditView


urlpatterns = [
    path("stations/<int:station_id>", views.weather_data_data, name="weather_data_data"),
    path("stations/<int:station_id>/add/", WeatherDataInputView.as_view(), name="weather_data_input"),
    path(
        "stations/<int:station_id>/<int:pk>/delete/", views.weather_data_delete, name="weather_data_delete"
    ),
    path("stations/<int:station_id>/<int:pk>/edit/", WeatherDataEditView.as_view(), name="weather_data_edit"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
