from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("db_manager/", views.db_manager, name="db_manager"),
    path("user/", views.user, name="user"),
    path("validate_manager/", views.validateManager, name="validate_manager"),
    path("validate_user/", views.validateUser, name="validate_user"),
    path("db_manager/manager_operations/", views.mngOperations, name="manager_operations"),
    path("user/user_operations/", views.userOperations, name="user_operations"),
    path('user/user_operations/<int:no>', views.userOperations, name='operation'),
]