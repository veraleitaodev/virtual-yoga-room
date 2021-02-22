from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(blank=False)
    date = models.DateField()
    author = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.title
