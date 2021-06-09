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


def user_options(request):
    if('name' in request.session):
        name = request.session['name']
    else: 
        return redirect('./login/')

    return render(request, 'main/user_options', {"name":name})


def manager_options(request):
    if('name' in request.session):
        name = request.session['name']
    else: 
        return redirect('./login/')

    return render(request, 'main/manager_options', {"name":name})


def login(response):
    if response.method == "POST":
	    form = LoginForm(response.POST)
	    if form.is_valid():
	        form.save()

	    return redirect("/")
    else:
	    form = LoginForm()

    return render(response, "main/home.html", {"form":form})