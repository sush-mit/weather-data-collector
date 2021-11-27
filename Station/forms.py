from django import forms
from django.utils.regex_helper import flatten_result
from .models import Countries, Cities, Station


class StationInputForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["city"].queryset = Cities.objects.none()

        if "country" in self.data:
            try:
                country_id = self.data.get("country")
                self.fields["city"].queryset = Cities.objects.filter(
                    country_id=country_id
                )
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields["city"].queryset = Cities.objects.filter(
                country_id=self.instance.country.id
            )

    class Meta:
        model = Station
        fields = ("name", "country", "city", "latitude", "longitude")
