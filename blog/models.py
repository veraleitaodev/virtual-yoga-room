from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    content = models.TextField(blank=False)
    date = models.DateField()
    author = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=300, null=False, blank=False)
    date = models.DateField()
    name = models.CharField(max_length=150, blank=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
