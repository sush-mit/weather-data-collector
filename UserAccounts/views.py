from django.http.response import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseNotFound


def user(request, username=None):
    if not username:
        username = request.user.username
    return redirect(reverse("userpage", args=[username]))


def userpage(request, username):
    if request.user.username == username:
        return render(request, "UserAccounts/userpage.html")
    else:
        return HttpResponseForbidden()
