from django.shortcuts import render, redirect
from django.urls import reverse

def users(request):
    return redirect(reverse('userpage', args=[request.user.username]))
    

def userpage(request, username):
    if request.user.username == username:
        return render(request, "UserAccounts/userpage.html")
    else:
        return redirect("/login/")
