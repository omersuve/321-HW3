from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .users.userForm import UserLoginForm
from .dbmanagers.managerForm import ManagerLoginForm
from main.users.user_functions import *

#from .forms import CreateNewList

# Create your views here.

def home(response):
    return render(response, "main/home.html", {})


def user(response):
    context = {"login_fail": False, "login_form":UserLoginForm()}
    return render(response, "main/user_login.html", context)


def db_manager(response):
    context = {"login_fail": False, "login_form":ManagerLoginForm()}
    return render(response, "main/manager_login.html", context)


def validateUser(request):
    username = request.POST.get("username")
    
    #loginCheck = checkCreditentials(name, surname)

    if(username):
        request.session['username'] = username
        return render(request, 'main/login.html', {})
    else:
        context = {"login_fail": True, "login_form":UserLoginForm()}    
    return render(request, 'main/login.html', context)

def validateManager(request):
    username = request.POST.get("username")
    
    #loginCheck = checkCreditentials(name, surname)

    if(username):
        request.session['username'] = username
        return render(request, 'main/login.html', {})
    else:
        context = {"login_fail": True, "login_form":managerForm()}    
    return render(request, 'main/login.html', context)


def userOperations(request):
    result_list = []
    no = 1
    if no == 1:
        result_list = view_drugs_side_effects()
    if no == 2:
        pass

    return render(request, 'main/user_operations.html', {"result_list": result_list})

def mngOperations(request):
    return render(request, 'main/manager_operations.html', {})