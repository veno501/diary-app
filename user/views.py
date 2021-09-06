from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .forms import RegisterForm, LoginForm, UserConfigForm

def index(request):
    if (request.user.is_authenticated):
        return redirect('dashboard')
    return render(request, 'user/index.html')

def register(request):
    if request.method=="POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
          print("registration form is valid")
          user = form.save(commit=False)
          user.save()
          auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
          return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, "user/register.html", {'form': form})

@login_required
def login(request):
    form = LoginForm()
    return render(request, 'user/login.html', {'form': form})

@login_required
def user_config(request):
    if request.method == 'POST':
        form = UserConfigForm(request.POST)
        if form.is_valid():
            request.user.theme = form.cleaned_data['theme']
            request.user.save()
            return redirect('dashboard')
    # else:
    #     form = UserConfigForm(initial={'theme': request.user.theme})
    # return render(request, 'user/user_config.html', {'form': form})
