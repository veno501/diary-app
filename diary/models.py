from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#from uuid import uuid4
#str(uuid4())

class Diary(models.Model):
    uuid = models.CharField(max_length=36, null=False, blank=False)
    title = models.CharField(max_length=100)
    themePreference = models.IntegerField(name='choice of color', default=0)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    def __str__(self):
        return self.title

class Entry(models.Model):
    uuid = models.CharField(max_length=36, null=False, blank=False)
    title = models.CharField(max_length=100)
    dateTime = models.DateTimeField(name='date created', default=timezone.now)
    parentDiary = models.ForeignKey(Diary, on_delete=models.SET_NULL, null=True, blank=False)
    def __str__(self):
        return self.title
