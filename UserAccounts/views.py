<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.urls import reverse

def users(request):
    return redirect(reverse('userpage', args=[request.user.username]))
    

def userpage(request, username):
    if request.user.username == username:
        return render(request, "UserAccounts/userpage.html")
    else:
        return redirect("/login/")
=======
from django.shortcuts import render
>>>>>>> e1ad4587b88ceb53d74b62c0a2e5e8f967cf3a11
