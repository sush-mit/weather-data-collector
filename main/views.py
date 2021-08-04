from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import RegisterForm, LoginForm
from .models import UserAccountsModel

def home(request):
    return render(request, "main/home.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["user_name"]
            user_email = form.cleaned_data["user_email"]
            user_password = form.cleaned_data["user_password"]
            user_password_repeat = form.cleaned_data["user_password_repeat"]
            if user_password != user_password_repeat:
                pass # Raise error
            user_account_model = UserAccountsModel(user_name=user_name, user_email=user_email, user_password=user_password)
            user_account_model.save()
            return HttpResponseRedirect("/")
    else:
        form = RegisterForm()
        return render(request, "main/register.html", {"form":form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            input_user_name = form.cleaned_data["user_name"]
            input_user_email = form.cleaned_data["user_email"]
            input_user_password = form.cleaned_data["user_password"]

        #     user_account_model = UserAccountsModel.objects.all()
        #     user_name = user_account_model["user_name"]
        #     user_email = user_account_model["user_email"]
        #     user_password = user_account_model["user_password"]

        # if input_user_name == user_name and input_user_email == user_email and input_user_password ==user_password:
        #     return HttpReponse()
    else:
        form = LoginForm()
        return render(request, "main/login.html", {"form":form})
