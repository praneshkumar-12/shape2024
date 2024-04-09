from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("login/", views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path(
        "checkavail/<project_id>/", views.check_availability, name="check_availability"
    ),
    path("checkavail/", views.check_availability, name="check_availability"),
    path("confirm_project/", views.confirm_project, name="confirm_project"),
    path(
        "get_all_availabilities/",
        views.get_all_availabilities,
        name="get_all_availabilities",
    ),
    path("view_selected_project/", views.view_selected_project, name="view_selected"),
    path("administrator/", views.admin_home, name="admin_home"),
    path(
        "administrator/allotments/",
        views.AllotmentsDownloadView.as_view(),
        name="file_download",
    ),
    path("logout/", views.logout, name="logout"),
]
