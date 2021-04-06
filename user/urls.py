from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('register/', views.register, name='register'),
    path('settings/', views.user_config, name='user_config'),
]