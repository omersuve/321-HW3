from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm

#from .forms import CreateNewList

# Create your views here.

def home(response):
    return render(response, "main/home.html", {})


def user(response):
    return render(response, "main/user_login.html", {})


def database_manager(response):
    return render(response, "main/manager_login.html", {})


def login(response):
    if response.method == "POST":
	    form = LoginForm(response.POST)
	    if form.is_valid():
	        form.save()

	    return redirect("/")
    else:
	    form = RegisterForm()

    return render(response, "/login.html", {"form":form})