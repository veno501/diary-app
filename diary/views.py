from django.shortcuts import render

def diary(request):
    return render(request, 'diary/diary.html', {'diary_name': 'My Diary'});

def diary_config(request):
    return render(request, 'diary/diary_config.html', {'diary_name': 'My Diary'});

def entry(request):
    return render(request, 'diary/entry.html', {'diary_name': 'My Diary'});

def edit(request):
    return render(request, 'diary/edit.html', {'diary_name': 'My Diary'});
