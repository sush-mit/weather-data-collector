from django import forms

from .csv_data import CSVData
from .models import Station
from .models import Countries


class StationInputForm(forms.ModelForm):

    country = forms.ModelChoiceField(queryset=Countries.objects.all(), empty_label="Select a country")
    city = forms.ChoiceField(choices=[("None", "Select a city")], required=False)

    latitude = forms.DecimalField(
        max_digits=10, decimal_places=8, max_value=90, min_value=-90
    )
    longitude = forms.DecimalField(
        max_digits=11, decimal_places=8, max_value=180, min_value=-180
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "country" in self.data:
            try:
                country_id = self.data.get("country")
                cities = [
                    city_data["name"]
                    for city_data in CSVData.CITIES
                    if city_data["country_id"] == country_id
                ]
                choices = [(city, city) for city in cities]
                self.fields["city"]._set_choices(choices)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            cities = [
                city_data["name"]
                for city_data in CSVData.CITIES
                if int(city_data["country_id"]) == self.instance.country.id
            ]
            choices = [(city, city) for city in cities]
            self.fields["city"]._set_choices(choices)

    class Meta:
        model = Station
        fields = ("name", "country", "city", "latitude", "longitude")


class StationDeleteForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(max_length=255)
    country = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    latitude = forms.DecimalField()
    longitude = forms.DecimalField()
    date_created = forms.DateTimeField()
    date_updated = forms.DateTimeField()