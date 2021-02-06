from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=100)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.title