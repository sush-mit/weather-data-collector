from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core import validators


latitude_re = "^(\+|-)?(?:90(?:(?:\.0{1,6})?)|(?:[0-9]|[1-8][0-9])(?:(?:\.[0-9]{1,6})?))$"
longitude_re = "^(\+|-)?(?:180(?:(?:\.0{1,6})?)|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])(?:(?:\.[0-9]{1,6})?))$"
validate_latitude = validators.RegexValidator(latitude_re, "Invalid latitude value.", 'Invalid')
validate_longitude = validators.RegexValidator(longitude_re, "Invalid longitude value.", 'Invalid')

# Create your models here.
class Station(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200, validators=[validate_latitude])
    longitude = models.CharField(max_length=200, validators=[validate_longitude])
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("station_data")
