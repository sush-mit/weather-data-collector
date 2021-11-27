from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core import validators


latitude_re = (
    "^(\+|-)?(?:90(?:(?:\.0{1,6})?)|(?:[0-9]|[1-8][0-9])(?:(?:\.[0-9]{1,6})?))$"
)
longitude_re = "^(\+|-)?(?:180(?:(?:\.0{1,6})?)|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])(?:(?:\.[0-9]{1,6})?))$"
validate_latitude = validators.RegexValidator(
    latitude_re, "Invalid latitude value.", "Invalid"
)
validate_longitude = validators.RegexValidator(
    longitude_re, "Invalid longitude value.", "Invalid"
)


class Countries(models.Model):
    name = models.CharField(max_length=100)
    # iso3 = models.CharField(max_length=3, blank=True, null=True)
    # numeric_code = models.CharField(max_length=3, blank=True, null=True)
    # iso2 = models.CharField(max_length=2, blank=True, null=True)
    # phonecode = models.CharField(max_length=255, blank=True, null=True)
    # capital = models.CharField(max_length=255, blank=True, null=True)
    # currency = models.CharField(max_length=255, blank=True, null=True)
    # currency_symbol = models.CharField(max_length=255, blank=True, null=True)
    # tld = models.CharField(max_length=255, blank=True, null=True)
    # native = models.CharField(max_length=255, blank=True, null=True)
    # region = models.CharField(max_length=255, blank=True, null=True)
    # subregion = models.CharField(max_length=255, blank=True, null=True)
    # timezones = models.TextField(blank=True, null=True)
    # translations = models.TextField(blank=True, null=True)
    # latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    # longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    # emoji = models.CharField(max_length=191, blank=True, null=True)
    # emojiu = models.CharField(db_column='emojiU', max_length=191, blank=True, null=True)  # Field name made lowercase.
    # created_at = models.DateTimeField(blank=True, null=True)
    # updated_at = models.DateTimeField()
    # flag = models.IntegerField()
    # wikidataid = models.CharField(db_column='wikiDataId', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = "countries"


class Cities(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Countries, on_delete=models.DO_NOTHING)
    # state = models.ForeignKey('States', models.DO_NOTHING)
    # state_code = models.CharField(max_length=255)
    # country_code = models.CharField(max_length=2)
    # latitude = models.DecimalField(max_digits=10, decimal_places=8)
    # longitude = models.DecimalField(max_digits=11, decimal_places=8)
    # created_at = models.DateTimeField()
    # updated_at = models.DateTimeField()
    # flag = models.IntegerField()
    # wikidataid = models.CharField(db_column='wikiDataId', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = "cities"


class Station(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Countries, on_delete=models.DO_NOTHING)
    city = models.ForeignKey(Cities, on_delete=models.DO_NOTHING)
    latitude = models.CharField(max_length=200, validators=[validate_latitude])
    longitude = models.CharField(max_length=200, validators=[validate_longitude])
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("station_data")
