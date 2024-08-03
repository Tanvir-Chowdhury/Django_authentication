from django.contrib import admin
from django.urls import path
from authApp.views import login_view, home_view, signup_view, logout_view

urlpatterns = [
    path('home/', home_view, name = 'home'),
    path('login/', login_view, name= 'login'),
    path('', signup_view, name= 'signup'),
    path('logout/', logout_view, name= 'logout'),
]
