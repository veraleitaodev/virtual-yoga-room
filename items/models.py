from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=254, null=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    CATEGORY = (
        ('Beginners', 'Beginners'),
        ('Challenges', 'Challenges'),
        ('Dynamic', 'Dynamic'),
        ('Therapeutic', 'Therapeutic')
    )

    sku = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    category = models.CharField(max_length=254, null=True, choices=CATEGORY)
    description = models.TextField()
    number_classes = models.IntegerField()
    image_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField()
    rating = models.DecimalField(
        max_digits=6, decimal_places=1, null=True, blank=True)
    instructor = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Class(models.Model):
    class Meta:
        verbose_name_plural = 'Classes'

    sku = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    program = models.ForeignKey(
        'Program', null=True,  on_delete=models.SET_NULL)
    description = models.TextField()
    video = models.URLField(max_length=1024, blank=True)
    image_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField()
    rating = models.DecimalField(
        max_digits=6, decimal_places=1, null=True, blank=True)
    instructor = models.CharField(max_length=254)

    def __str__(self):
        return self.name
