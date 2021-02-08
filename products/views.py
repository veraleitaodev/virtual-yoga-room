from django.shortcuts import render
from .models import Class


def all_classes(request):
    """ A view to show all classes, including sorting and search queries """

    classes = Class.objects.all()

    context = {
        'classes': classes,
    }

    return render(request, 'products/classes.html', context)
