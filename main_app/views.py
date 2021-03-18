from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile, Event, User
from django.contrib import messages




def home(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'home.html', { 'events': events })

# for register of the user
def register(request):
    
    if request.method == "POST":
# registerform is made in the form.py file and response with post method
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            profile = Profile(user = user, bio = '' )
            profile.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'New Account Created: {username}')
            login(request, user)
            messages.success(request, f'you are now logged in as: {username}')
        return redirect('profile')
    else:
        form = RegisterForm()
        for msg in form.error_messages:
            messages.error(request, form.error_messages[msg])
    return render(request, "registration/register.html",{'form' : form})

# after logging in they will land on profile by default.
@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, instance = request.user.profile)
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
             u_form.save()
             p_form.save()
             messages.success(request, 'You are logged in')
             return redirect('profile')
    else:
       
        profile = Profile.objects.get(user_id=request.user.id)
        p_form = ProfileUpdateForm(instance=profile)
        u_form = UserUpdateForm(instance = request.user)

    events = Event.objects.filter(users=request.user)

    context={'p_form': p_form, 'u_form': u_form, 'events': events}
    
    return render(request, 'profile.html',context)

# About View
def about(request):
    return render(request, 'about.html')

# Event Details
def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/detail.html', { 'event': event})
            

# Register user for event
@login_required
def add_registration(request, event_id):
    event = Event.objects.get(id=event_id)

    # checked whether the user had that event or not
    x = event.users.all()
    for X in x:
        if X != request.user:
            event.users.add(request.user)
            
        else :
            messages.error(request, 'Event is already added') 
    # (request.user.email) == request.user.email:
        # event.users.add(request.user.id)
    
        # print('Its already been added')
        


    # print(request.user)
    print(event)
    print(event.users.all())
    
    return redirect('profile')
    

# Unregister user for event
@login_required
def remove_registration(request, event_id):
    
    event = Event.objects.get(id=event_id)

    # instance = User.objects.get(id=request.user.id)
    # instance.delete()
    # event.users.remove(request.user.id)
    x = event.users.all()
    for X in x:
        if X == request.user:
            event.users.remove(request.user.id)
            return render(request, 'landing.html', {'message': "You sure you want to delete all those things"})
            messages.success(request, 'not deleted')
        else:
                
            messages.error(request, 'deleted')
            
    
    if request.method == 'POST':
        event.users.remove(request.user.id)
    
    
    
    return redirect('profile')
    
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



 
 



