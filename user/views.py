from django.shortcuts import render

def index(request):
    return render(request, 'user/index.html');

def dashboard(request):
    return render(request, 'user/dashboard.html');

#def login(request):
#    return render(request, 'user/login.html');

def register(request):
    return render(request, 'user/register.html');

def user_config(request):
    return render(request, 'user/user_config.html');
