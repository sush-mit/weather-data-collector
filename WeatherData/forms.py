from django import forms

from .models import WeatherData


class WeatherDataInputForm(forms.ModelForm):
  
  date_time = forms.DateTimeField(label="Date/Time", input_formats="%Y-%m-%d %H:%M:%S")

  def __init__(self, *args, **kwargs):
      super(WeatherDataInputForm, self).__init__(*args, **kwargs)
      self.fields['date_time'].widget.attrs['placeholder'] = 'YYYY-MM-DD HH:MM:SS'

  class Meta:
      model = WeatherData
      fields =  ("date_time", "temperature_c", "weather_condition", "humidity", "cloud")
