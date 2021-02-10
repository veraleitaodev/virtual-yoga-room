from django.shortcuts import render
from .models import Class, Program
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def all_classes(request):
    """ A view to show all classes, including sorting and search queries """

    class_list = Class.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(class_list, 6)
    try:
        classes = paginator.page(page)
    except PageNotAnInteger:
        classes = paginator.page(1)
    except EmptyPage:
        classes = paginator.page(paginator.num_pages)

    context = {
        'classes': classes,
    }

    return render(request, 'products/classes.html', context)


def all_programs(request):
    """ A view to show all programs, including sorting and search queries """

    program_list = Program.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(program_list, 6)
    try:
        programs = paginator.page(page)
    except PageNotAnInteger:
        programs = paginator.page(1)
    except EmptyPage:
        programs = paginator.page(paginator.num_pages)

    context = {
        'programs': programs,
    }

    return render(request, 'products/programs.html', context)
