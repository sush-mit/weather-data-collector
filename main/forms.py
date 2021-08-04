from django import forms

class RegisterForm(forms.Form):
    user_name = forms.CharField(label="", max_length=32, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
    user_email = forms.EmailField(label="", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}))
    user_password = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "form-control", "type":"password", "placeholder": "Password"}))
    user_password_repeat = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "form-control", "type":"password", 'placeholder': "Confirm password"}))

class LoginForm(forms.Form):
    user_name = forms.CharField(label="", max_length=32, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
    user_email = forms.EmailField(label="", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}))
    user_password = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "form-control", "type":"password", "placeholder": "Password"}))