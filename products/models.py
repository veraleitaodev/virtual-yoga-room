from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Program(models.Model):

    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    number_classes = models.IntegerField()
    image_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField()
    rating = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)
    instructor = models.CharField(max_length=254, null=True)

    def __str__(self):
        return self.name


class Class(models.Model):
    class Meta:
        verbose_name_plural = 'Classes'

    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True)
    name = models.CharField(max_length=254)
    program = models.ForeignKey('Program', null=True,  on_delete=models.SET_NULL)
    description = models.TextField()
    video = models.URLField(max_length=1024, blank=True)
    image_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField()
    rating = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)
    instructor = models.CharField(max_length=254, null=True)

    def __str__(self):
        return self.name
