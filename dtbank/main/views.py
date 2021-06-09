from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from .models import User
#from .forms import CreateNewList

# Create your views here.

def index(response, id):
    # ls = ToDoList.objects.get(id=id)
    return render(response, "main/login.html", {})


def home(response):
    return render(response, "main/home.html", {})


def user(response):
    return render(response, "main/user_login.html", {})


def database_manager(response):
    return render(response, "main/manager_login.html", {})


def login(response):
    if response.method == "POST":
        pass    # Do stuff

    return render(response, "main/login.html", {})