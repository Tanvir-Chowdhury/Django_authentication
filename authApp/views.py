from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

@login_required(login_url='login')
def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password= password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('login')
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 and password2 and password1 == password2:
            if User.objects.filter(username = username).exists():
                pass
            else:
                user = User.objects.create_user(username, email, password1)
                user.save()
                return redirect('login')
        else:
            messages.error(request, "Passwords did not match") 
            return redirect('signup')
    return render(request, 'signup.html')


def logout_view(request):
    logout(request)
    return redirect('login')