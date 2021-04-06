from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.mixins import LoginRequiredMixin
#from .models import Diary

@login_required
def diary(request):
    return render(request, 'diary/diary.html', {'diary_name': 'My Diary'});

#class DiaryView(LoginRequiredMixin,generic.ListView):
#    model = Entry

@login_required
def diary_config(request):
    return render(request, 'diary/diary_config.html', {'diary_name': 'My Diary'});

@login_required
def entry(request):
    return render(request, 'diary/entry.html', {'diary_name': 'My Diary'});

@login_required
def edit(request):
    return render(request, 'diary/edit.html', {'diary_name': 'My Diary'});
