from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone

class Post(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    hr_newsline = models.CharField(max_length=200)
    datetime = models.DateTimeField(default=timezone.now)
    predicted_category = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user_name} - {self.hr_newsline} - {self.datetime} - {self.predicted_category}"

