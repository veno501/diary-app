from django.db import models
from django.utils import timezone

class Diary(models.Model):
    title = models.CharField(max_length=100)
    themePreference = models.IntegerField(name='choice of color', default=0)
    def __str__(self):
        return self.title

class Entry(models.Model):
    title = models.CharField(max_length=100)
    dateTime = models.DateTimeField(name='date created', default=timezone.now())
    def __str__(self):
        return self.title
