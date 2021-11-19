from django import forms
  
from .models import Station
  
class StationInputForm(forms.ModelForm):

    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'autofocus': True}))
    country = forms.CharField(max_length=200)
    city = forms.CharField(max_length=200)
    latitude = forms.CharField(max_length=200)
    longitude = forms.CharField(max_length=200)