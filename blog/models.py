import datetime
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=600)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self
