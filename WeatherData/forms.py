from django import forms

from .models import WeatherData


class WeatherDataInputForm(forms.ModelForm):
  
  date_time = forms.DateTimeField(label="Date/Time", input_formats="%Y-%m-%d %H:%M:%S")

  def __init__(self, *args, **kwargs):
      super(WeatherDataInputForm, self).__init__(*args, **kwargs)
      self.fields['date_time'].widget.attrs['placeholder'] = 'YYYY-MM-DD HH:MM:SS'
      self.fields['date_time'].widget.attrs['autocomplete'] = 'off'

  class Meta:
      model = WeatherData
      fields =  ("station", "date_time", "temperature_c", "weather_condition", "humidity", "cloud", "wind_kph")


class WeatherDataDeleteForm(forms.Form):
    date_time = forms.DateTimeField()
    temperature_f = forms.DecimalField()
    temperature_c = forms.DecimalField()
    weather_condition = forms.CharField(max_length=255)
    humidity = forms.DecimalField()
    cloud = forms.DecimalField()