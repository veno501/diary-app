from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from diary.models import Diary

def index(request):
    return render(request, 'user/index.html');

class DashboardView(LoginRequiredMixin, ListView):
    model = Diary
    template_name = 'user/dashboard.html'
    paginate_by = 1

    def get_queryset(self):
        return Diary.objects.filter(author=self.request.user).order_by('title')

def register(request):
    return render(request, 'user/register.html');

@login_required
def user_config(request):
    return render(request, 'user/user_config.html');
