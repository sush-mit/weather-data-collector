from django import forms
  
from .models import StationModel
  
class StationInputForm(forms.ModelForm):
    class Meta:
        model = StationModel
        fields = "__all__"