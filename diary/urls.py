from django.urls import path
from . import views

urlpatterns = [
    path('<uuid:diary_id>/', views.diary, name='diary'),
    path('<uuid:diary_id>/settings/', views.diary_config, name='diary_config'),
    path('<uuid:diary_id>/entry/<uuid:entry_id>/', views.entry, name='entry'),
    path('<uuid:diary_id>/edit/<uuid:entry_id>/', views.edit, name='edit'),
    path('missing/', views.missing, name='missing'),
]