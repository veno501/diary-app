from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Diary

def diaryrequired(f):
    def wrap_function(request, diary_id):
        try:
            diaryInstance = Diary.objects.get(id=diary_id, author=request.user)
        except:
            return redirect('missing')
        return f(request, diary_id, diaryInstance=diaryInstance)
    return wrap_function

@login_required
@diaryrequired
def diary(request, diary_id, diaryInstance):
    return render(request, 'diary/diary.html', {'diary': diaryInstance});

#class DiaryView(LoginRequiredMixin, ListView):
#    def get(self, request, diary_id):
#        try:
#            diaryInstance = Diary.objects.get(id=diary_id, author=user)
#        except:
#            return redirect('missing')
#        return render(request, 'diary/diary.html', {'diary': diaryInstance});

@login_required
@diaryrequired
def diary_config(request, diary_id, diaryInstance):
    return render(request, 'diary/diary_config.html', {'diary': diaryInstance});

@login_required
@diaryrequired
def entry(request, diary_id, diaryInstance):
    return render(request, 'diary/entry.html', {'diary': diaryInstance});

@login_required
@diaryrequired
def edit(request, diary_id, diaryInstance):
    return render(request, 'diary/edit.html', {'diary': diaryInstance});

def missing(request):
    return render(request, 'diary/missing.html')
