from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from user.models import UserModel
from uuid import uuid4

# UUID generation
#   from uuid import uuid4
#   str(uuid4())

# class Diary(models.Model):
#     uuid = models.CharField(max_length=36, default=uuid4, null=False)
#     title = models.CharField(max_length=100)
#     themePreference = models.IntegerField(default=0)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
#     def __str__(self):
#         return self.title

class DiaryEntry(models.Model):
    uuid = models.CharField(max_length=36, default=uuid4, null=False)
    title = models.CharField(max_length=50, null=False)
    dateTime = models.DateTimeField(default=timezone.now, null=False)
    location = models.CharField(max_length=200, default='', null=False, blank=True)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=8000, default='', null=False, blank=True)
    def __str__(self):
        return self.title
