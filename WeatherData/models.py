from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from Station.models import Station

# Create your models here.
class WeatherData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    date_time = models.DateTimeField(null=True)
    temperature_f = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    temperature_c = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    weather_condition = models.CharField(max_length=255, null=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    cloud = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    wind_kph = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.date_time}"

    def get_absolute_url(self):
        return reverse("weather_data_data")
