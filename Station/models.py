from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Station(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
      return self.name
    
    def get_absolute_url(self):
        return reverse("station_data", args=(self.user.username, ))