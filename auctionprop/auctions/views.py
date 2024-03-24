from django.contrib.auth import authenticate, login as auth_login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *


def index(request):
    return render(request, 'auctions/index.html')

def home(request):
    return render(request, 'auctions/home.html')

# login
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        phone = request.POST["phone"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })
        try:
            user = User.objects.create_user(username, phone, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        auth_login(request, user) 
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "auctions/register.html")
