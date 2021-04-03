from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('user/dashboard.html')
    context = {
        'page_description': 'This is the user dashboard. It will display \
          user info and diaries written (or it will redirect to the login page).',
    }
    return HttpResponse(template.render(context, request))
