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


def user_operations(request):
    if('username' in request.session):
        username = request.session['username']
    else: 
        return redirect('./login/')

    return render(request, 'main/user_operations', {"username":username})


def manager_operations(request):
    if('username' in request.session):
        username = request.session['username']
    else: 
        return redirect('./login/')

    return render(request, 'main/manager_operations', {"username":username})


def login(response):
    if response.method == "POST":
	    form = LoginForm(response.POST)
	    if form.is_valid():
	        form.save()

	    return redirect("/")
    else:
	    form = LoginForm()

    return render(response, "main/home.html", {"form":form})