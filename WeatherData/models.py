from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from Station.models import Station

# Create your models here.
class WeatherData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    date_time = models.DateTimeField(null=True)
    temperature_f = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    temperature_c = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    weather_condition = models.CharField(max_length=255, null=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    cloud = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return {
            "User": self.user,
            "Station": self.station,
            "Date_Time": self.date_time,
            "Temperature_F": self.temperature_f,
            "Temperature_C": self.temperature_c,
            "Weather_Condition": self.weather_condition,
            "Humidity": self.humidity,
            "Cloud": self.cloud,
        }

    def get_absolute_url(self):
        return reverse("station_data")
