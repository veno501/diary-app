from django.db import models

class Diary(models.Model):
    title = models.CharField(max_length=200)
    themePreference = models.IntegerField(default=0)
    colorPreference = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Entry(models.Model):
    title = models.CharField(max_length=200)
    dateTime = models.DateTimeField('date created')
    contentPath = models.CharField(max_length=200)
    def __str__(self):
        return self.title
