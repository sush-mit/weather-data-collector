from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(f"/{request.user.username}")
    else:
        form = RegisterForm()

    return render(request, "AccountsManager/register.html", {"form":form})