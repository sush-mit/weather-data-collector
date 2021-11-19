from django.urls import path
from . import views


urlpatterns = [
    path("user/", views.user, name="user_redirect"),
    path("users/<str:username>/", views.userpage, name="userpage"),
    path("<str:username>/", views.user, name="username_redirect"),
]