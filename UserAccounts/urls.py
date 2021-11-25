from django.urls import path
from . import views


urlpatterns = [
    path("users/", views.user, name="user_redirect"),
    path("users/<str:username>/", views.userpage, name="userpage"),
]
