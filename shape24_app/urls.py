from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("checkavail/<project_id>/", views.check_availability, name="check_availability"),
    path("checkavail/", views.check_availability, name="check_availability"),
]
