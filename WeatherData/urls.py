from django.urls import path
from django.views.generic.edit import DeleteView
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import WeatherDataInputView, WeatherDataEditView


urlpatterns = [
    path("weather_data/", views.weather_data_data, name="weather_data_data"),
    path(
        "weather_data/add/", WeatherDataInputView.as_view(), name="weather_data_input"
    ),
    path(
        "weather_data/<int:pk>/delete/",
        views.weather_data_delete,
        name="weather_data_delete",
    ),
    path(
        "weather_data/<int:pk>/edit/",
        WeatherDataEditView.as_view(),
        name="weather_data_edit",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
