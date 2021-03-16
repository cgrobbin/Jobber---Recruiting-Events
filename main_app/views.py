from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
# Create your views here.
def home(request):
    
  return render(request, 'home.html')
# for register of the user
def register(response):
    error_message = ''
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('/')
    else:
        form = RegisterForm()

    return render(response, "registration/register.html",{'form' : form})
# after logging in they will land on profile by default.
def profile(request):
    return render(request, 'profile.html')