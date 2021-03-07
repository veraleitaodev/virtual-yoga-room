from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    content = models.TextField(blank=False)
    date = models.DateField()
    author = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300, null=False, blank=False)
    date = models.DateField()
    name = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name
