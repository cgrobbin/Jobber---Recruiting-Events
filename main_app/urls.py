from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.register,name='register'),
    path('accounts/profile/',views.profile, name = 'profile'),
    path('about/', views.about, name='about'),
    path('search/',views.search, name = 'search'),
    path('searchoption/',views.searchoption,name = 'seachoption')
   
]

