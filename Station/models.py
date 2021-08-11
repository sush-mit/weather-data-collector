from django.db import models

# Create your models here.
class StationModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)