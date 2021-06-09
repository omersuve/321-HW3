from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("database_manager/", views.database_manager, name="database_manager"),
    path("user/", views.user, name="user"),
    
    #path('shows/<int:genre>', views.listShows, name='listshows'),
]