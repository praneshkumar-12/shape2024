from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path(
        "checkavail/<project_id>/", views.check_availability, name="check_availability"
    ),
    path("checkavail/", views.check_availability, name="check_availability"),
    path("confirm_project/", views.confirm_project, name="confirm_project"),
    path("view_selected_project/", views.view_selected_project, name="view_selected"),
    path("logout/", views.logout, name="logout"),
]
