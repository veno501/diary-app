from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def diary(request):
    template = loader.get_template('diary/diary.html')
    return HttpResponse(template.render({'diary_name': 'My Diary'}, request))

def diary_config(request):
    template = loader.get_template('diary/diary_config.html')
    return HttpResponse(template.render({'diary_name': 'My Diary'}, request))

def entry(request):
    template = loader.get_template('diary/entry.html')
    return HttpResponse(template.render({'diary_name': 'My Diary'}, request))

def edit(request):
    template = loader.get_template('diary/edit.html')
    return HttpResponse(template.render({'diary_name': 'My Diary'}, request))
