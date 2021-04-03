from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('diary/index.html')
    context = {
        'diary_name': 'My Diary',
        'page_description': 'This is the diary landing page. It loads the data \
        for a specific diary and displays it (so, the entries).',
    }
    return HttpResponse(template.render(context, request))
