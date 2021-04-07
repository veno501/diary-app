from django.urls import path
from . import views

urlpatterns = [
    path('<int:diary_id>/', views.diary, name='diary'),
    path('<int:diary_id>/settings/', views.diary_config, name='diary_config'),
    path('<int:diary_id>/entry/', views.entry, name='entry'),
    path('<int:diary_id>/edit/', views.edit, name='edit'),
    path('missing/', views.missing, name='missing'),
]