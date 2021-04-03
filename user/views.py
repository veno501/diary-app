from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('user/index.html')
    return HttpResponse(template.render({}, request))

def dashboard(request):
    template = loader.get_template('user/dashboard.html')
    return HttpResponse(template.render({}, request))

def login(request):
    template = loader.get_template('user/login.html')
    return HttpResponse(template.render({}, request))

def register(request):
    template = loader.get_template('user/register.html')
    return HttpResponse(template.render({}, request))

def user_config(request):
    template = loader.get_template('user/user_config.html')
    return HttpResponse(template.render({}, request))
