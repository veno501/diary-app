from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Diary, Entry

def diary_required(f):
    def wrap_function(request, diary_id, *args, **kwargs):
        try:
            diaryInstance = Diary.objects.get(uuid=diary_id, author=request.user)
        except:
            return redirect('missing')
        return f(request, diary_id, *args, **kwargs, diaryInstance=diaryInstance)
    return wrap_function

def entry_required(f):
    def wrap_function(request, diary_id, entry_id, diaryInstance):
        try:
            entryInstance = Entry.objects.get(uuid=entry_id, parentDiary=diaryInstance)
        except:
            return redirect('missing')
        return f(request, diary_id, entry_id, diaryInstance, entryInstance=entryInstance)
    return wrap_function

@login_required
@diary_required
def diary(request, diary_id, diaryInstance):
    entryList = Entry.objects.filter(parentDiary=diaryInstance).order_by('date created')
    return render(request, 'diary/diary.html', {'diary': diaryInstance, 'entry_list': entryList});

#class DiaryView(LoginRequiredMixin, ListView):
#    def get(self, request, diary_id):
#        try:
#            diaryInstance = Diary.objects.get(id=diary_id, author=user)
#        except:
#            return redirect('missing')
#        return render(request, 'diary/diary.html', {'diary': diaryInstance});

@login_required
@diary_required
def diary_config(request, diary_id, diaryInstance):
    return render(request, 'diary/diary_config.html', {'diary': diaryInstance});

@login_required
@diary_required
@entry_required
def entry(request, diary_id, entry_id, diaryInstance, entryInstance):
    return render(request, 'diary/entry.html', {'diary': diaryInstance, 'entry': entryInstance});

@login_required
@diary_required
@entry_required
def edit(request, diary_id, entry_id, diaryInstance, entryInstance):
    return render(request, 'diary/edit.html', {'diary': diaryInstance, 'entry': entryInstance});

def missing(request):
    return render(request, 'diary/missing.html')
