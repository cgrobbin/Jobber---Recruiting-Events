from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile
def home(request):
    
  return render(request, 'home.html')

# for register of the user
def register(response):
    
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(user = user, bio = '' )
            profile.save()
            login(response, user)
        return redirect('profile')
    else:
        form = RegisterForm()

    return render(response, "registration/register.html",{'form' : form})
# after logging in they will land on profile by default.


@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, instance = request.user.profile)
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
             u_form.save()
             p_form.save()
             
             return redirect('profile')
    else:
       
        profile = Profile.objects.get(user_id=request.user.id)
        p_form = ProfileUpdateForm(instance=profile)
        u_form = UserUpdateForm(instance = request.user)

    context={'p_form': p_form, 'u_form': u_form}

    return render(request, 'profile.html',context)
       