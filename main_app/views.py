from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm, EventForm
from .models import Profile, Event, User
from django.contrib import messages

# Home View
def home(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'home.html', { 'events': events })

# Register of the user
def register(request):
    error_message = ''
    if request.method == "POST":
    # registerform is made in the form.py file and response with post method
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'New account Created: {username}')
            profile = Profile(user = user, bio = '' )
            profile.save()
            username = form.cleaned_data.get('username')
            
            messages.success(request, f'New Account Created: {username}')
            login(request, user)
            messages.success(request, f'you are now logged in as: {username}')
            return redirect('profile')
    else:
        form = RegisterForm()
        error_message = 'Invalid sign up - try again'
        
        return render(request, 'registration/register.html',{ 'form': form })
        # for msg in form.error_messages:
        #     messages.error(request, form.error_messages[msg])
            
    return render(request, "registration/register.html",{'form' : form, 'message': error_message})

# after logging in they will land on profile by default.
@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, instance = request.user.profile)
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            
             u_form.save()
             p_form.save()
             messages.success(request, 'You are logged in successfully')
             return redirect('profile')
    else:
       
        profile = Profile.objects.get(user_id=request.user.id)
        p_form = ProfileUpdateForm(instance=profile)
        
        u_form = UserUpdateForm(instance = request.user)

    events = Event.objects.filter(users=request.user)
    context={'p_form': p_form, 'u_form': u_form, 'events': events}
     
    return render(request, 'profile.html',context)

# Public Profile
def public_profile(request, user_id):
    user = User.objects.get(id=user_id)
    events = Event.objects.filter(users=user)
    return render(request, 'public.html', { 'user': user, 'events': events })

# About View
def about(request):
    return render(request, 'about.html')

# Event Details
def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    total_registered = len(event.users.all())
    registered = False
    if request.user:
        if request.user in event.users.all():
            registered = True
    context = {
        'event': event,
        'registered': registered,
        'total_registered': total_registered
    }
    return render(request, 'events/detail.html', context)
            

# Register user for event
@login_required
def add_registration(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.user in event.users.all():
        messages.error(request, 'Event is already added')
    else:
        event.users.add(request.user)
        messages.success(request, 'Event has been added')
    return redirect('profile')

# Unregister user for event
@login_required
def remove_registration(request, event_id):
    event = Event.objects.get(id=event_id)
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
    query1 = request.GET['query']
    query2 = request.GET['option']
    
    # In this way we can use __icontains module to  set any attribute as query.
    events = Event.objects.filter(title__icontains = query1, focus__icontains = query2) 

    if(events):
        messages.success(request,'this is the result')
        return render(request, 'search.html',{'events': events})

    elif(not events):
        messages.error(request, 'There is no such Event')
        return redirect('home')

    return redirect('search')

# SuperUser Add Event
@login_required
def add_event(request):
    form = EventForm(request.POST or None)
    if request.POST and form.is_valid():
        new_event = form.save(commit=False)
        new_event.save()
        return redirect('home')
    else:
        return render(request, 'events/new.html', { 'form': form })

# Edit Event
@login_required
def event_edit(request, event_id):
    event = Event.objects.get(id=event_id)
    event_form = EventForm(request.POST or None, instance=event)
    if request.POST and event_form.is_valid():
        event_form.save()
        return redirect('detail', event_id=event_id)
    else:
        return render(request, 'events/edit.html', { 'event': event, 'event_form': event_form })

# Delete Event
@login_required
def event_delete(request, event_id):
    Event.objects.get(id=event_id).delete()
    return redirect('home')