from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('user_dashboard') if not user.is_staff else redirect('admin_dashboard')
        return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')

@login_required
def user_dashboard(request):
    return render(request, 'accounts/user_dashboard.html')

@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    users = User.objects.all()
    return render(request, 'accounts/admin_dashboard.html', {'users': users})

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'accounts/home.html')
