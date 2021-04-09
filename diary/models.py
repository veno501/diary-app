from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# UUID generation
#   from uuid import uuid4
#   str(uuid4())

# COLOR PALETTE for themes
#   main thumbnailing theme: theme 0 , mix-of-the-two color #BC8250
#   background: off-white #F8EBE3 / slightly darker #EBDED5
#   theme 0: coral orange #C47B58 , leather brown #BC9671
#   theme 1: teal blue #3E5952 , slate gray #9EA8A7
#   theme 2: crimson red #AF6757 , salmon pink #BC968B

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
