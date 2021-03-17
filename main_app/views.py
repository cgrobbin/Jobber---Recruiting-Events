from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile, Event



def home(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'home.html', { 'events': events })

# for register of the user
def register(response):
    
    if response.method == "POST":
# registerform is made in the form.py file and response with post method
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

# About View
def about(request):
    return render(request, 'about.html')

# search
def search(request):
    # this is the query that we access from the url which is send from the search form
    query = request.GET['query']
    # In this way we can use __icontains module to  set any attribute as query.
    events = Event.objects.filter(title__icontains = query)
  
    
    params = {'events': events, 'query': query }
    return render(request, 'search.html', params)

# focus contains only three option.
def searchoption(request):
    option = request.GET['option']
    events = Event.objects.filter(focus__icontains = option)

    return render(request, 'search.html',{'events': events})


