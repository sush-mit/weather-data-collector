from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# class LoginForm(forms.Form):
#     user_name = forms.CharField(label="", max_length=32, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
#     user_email = forms.EmailField(label="", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}))
#     user_password = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "form-control", "type":"password", "placeholder": "Password"}))