from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from account.forms import UserForm
# Create your views here.


def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password )
        if user:
            login(request, user)
            return redirect("blog:blog")
        else:
            error = "Provide the good credentials"
            context = {
                'error': error
            }
            return render(request, "account/login.html", context)
    else:
        return render(request, "account/login.html", context)
def login_success(request):
    context = {}
    context ['user'] = request.user
    return render(request, "account/success.html", context)


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse("user_login"))