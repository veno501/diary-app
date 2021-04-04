from django.contrib import admin

from .models import Diary, Entry

admin.site.register(Diary)
admin.site.register(Entry)