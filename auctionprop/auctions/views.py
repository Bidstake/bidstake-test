# myapp/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'auctions/index.html')
def login(request):
    return render(request, 'auctions/login.html')
def register(request):
    return render(request, 'auctions/register.html')