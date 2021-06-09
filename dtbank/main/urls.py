from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),

    path("database_manager/", views.database_manager, name="database_manager"),
    path("user/", views.user, name="user"),
    path("manager_operations/", views.manager_options, name="manager_operations"),
    path("user_operations/", views.user_options, name="user_operations"),
]