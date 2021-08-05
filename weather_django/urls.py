from main import views as main_views

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", main_views.home),
    path("", include("AccountsManager.urls")),
]