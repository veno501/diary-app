from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import ListView
from diary.models import Diary
from diary.forms import DiaryCreationForm

def index(request):
    if (request.user.is_authenticated):
        return redirect('dashboard')
    return render(request, 'user/index.html')

@login_required
def dashboard(request):
    diaryList = Diary.objects.filter(author=request.user).order_by('title')

    if request.method == 'POST':
        form = DiaryCreationForm(request.POST)
        if form.is_valid():
            newDiary = Diary(title=form.cleaned_data['title'], 
                themePreference=form.cleaned_data['color'], author=request.user)
            newDiary.save()
            return redirect('diary', diary_id=newDiary.uuid)
    else:
        form = DiaryCreationForm()

    return render(request, 'user/dashboard.html', 
        {'diary_list': diaryList, 'form': form})

# class DashboardView(LoginRequiredMixin, ListView):
#     model = Diary
#     template_name = 'user/dashboard.html'
#     context_object_name = 'diary_list'

#     def get_queryset(self):
#         return Diary.objects.filter(author=self.request.user).order_by('title')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         if self.request.method == 'POST':
#             form = DiaryCreationForm(self.request.POST)
#             if form.is_valid():
#                 newDiary = Diary(title=form.cleaned_data['title'], 
#                     themePreference=form.cleaned_data['themePreference'], author=self.request.user)
#                 newDiary.save()
#                 return redirect('diary', diary_id=newDiary.uuid)
#         else:
#             form = DiaryCreationForm()

#         context['form'] = form
#         return context


def register(request):
    return render(request, 'user/register.html')

@login_required
def user_config(request):
    return render(request, 'user/user_config.html')
