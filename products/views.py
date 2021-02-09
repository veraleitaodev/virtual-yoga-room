from django.shortcuts import render
from .models import Class, Program


def all_classes(request):
    """ A view to show all classes, including sorting and search queries """

    classes = Class.objects.all()

    context = {
        'classes': classes,
    }

    return render(request, 'products/classes.html', context)


def all_programs(request):
    """ A view to show all programs, including sorting and search queries """

    programs = Program.objects.all()

    context = {
        'programs': programs,
    }

    return render(request, 'products/programs.html', context)
