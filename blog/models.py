from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    content = models.TextField(blank=False)
    date = models.DateField(null=True, blank=True)
    author = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=300, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    username = models.ForeignKey(User, on_delete=models.RESTRICT)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.username)
