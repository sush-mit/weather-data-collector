from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import RegisterForm

# from .forms import RegisterForm, LoginForm
from .models import UserAccountsModel

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
    else:
        form = RegisterForm()

    return render(request, "AccountsManager/register.html", {"form":form})

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
        return render(request, "AccountsManager/login.html", {"form":form})
