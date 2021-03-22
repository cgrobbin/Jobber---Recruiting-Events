from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.register,name='register'),
    path('accounts/profile/',views.profile, name = 'profile'),
    path('accounts/profile/<int:user_id>/', views.public_profile, name='public_profile'),
    path('about/', views.about, name='about'),
    path('search/',views.search, name = 'search'),
    path('events/<int:event_id>/', views.event_detail, name='detail'),
    path('events/<int:event_id>/edit/', views.event_edit, name='edit'),
    path('events/<int:event_id>/delete/', views.event_delete, name='delete'),
    path('events/<int:event_id>/add_registration/', views.add_registration, name='add_registration'),
    path('events/<int:event_id>/remove_registration/', views.remove_registration, name='remove_registration'),
    path('events/add_event/', views.add_event, name='add_event'),
    
]