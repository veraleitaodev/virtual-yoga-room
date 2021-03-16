from django.db import models

from profiles.models import UserProfile
from items.models import Program


class OrderItem(models.Model):
    program = models.OneToOneField(
        Program, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    dete_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.program.name


class Order(models.Model):
    reference_key = models.CharField(max_length=20)
    owner = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now=True)
    items = models.ManyToManyField(OrderItem)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.program.price for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.reference_key)
