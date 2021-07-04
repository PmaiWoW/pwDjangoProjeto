from django.shortcuts import render
from django.db import models
from django.forms import HiddenInput
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index_page_view(request):
    if not request.user.is_authenticated:
        context = {
            'message': "You must log in before viewing this page."
        }
        return HttpResponseRedirect(reverse('users:login'))
    return render(request, 'users/auth-user.html')


def login_page_view(request):
    if request.user.is_authenticated:
        return render(request, 'users/auth-user.html')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('users:home'))
        else:
            return render(request, 'users/login.html',
                          {
                              'message': 'Invalid credentials'
                          })
    return render(request, 'users/login.html')


def logout_page_view(request):
    logout(request)
    return render(request, 'users/login.html',
                  {
                      'message': "Logged out"
                  })
