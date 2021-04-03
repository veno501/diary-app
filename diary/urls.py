from django.urls import path
from . import views

urlpatterns = [
    path('', views.diary, name='diary'),
    path('settings/', views.diary_config, name='diary_config'),
    path('entry/', views.entry, name='entry'),
    path('edit/', views.edit, name='edit'),
]