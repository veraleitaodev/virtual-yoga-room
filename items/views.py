from django.shortcuts import render, get_object_or_404
from .models import Class, Program
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def all_programs(request):
    """ A view to show all programs, including sorting and search queries """
    programs = Program.objects.all()
    program_count = programs.count()
    page = request.GET.get('page', 1)

    paginator = Paginator(programs, 4)
    try:
        programs = paginator.page(page)
    except PageNotAnInteger:
        programs = paginator.page(1)
    except EmptyPage:
        programs = paginator.page(paginator.num_pages)

    context = {
        'programs': programs,
        'program_count': program_count,
        'page': page
    }

    return render(request, 'items/programs.html', context)


def all_classes(request):
    """ A view to show all classes, including sorting and search queries """

    classes = Class.objects.all()
    classes_count = classes.count()
    page = request.GET.get('page', 1)

    paginator = Paginator(classes, 6)
    try:
        classes = paginator.page(page)
    except PageNotAnInteger:
        classes = paginator.page(1)
    except EmptyPage:
        classes = paginator.page(paginator.num_pages)

    context = {
        'classes': classes,
        'classes_count': classes_count,
        'page': page
    }

    return render(request, 'items/classes.html', context)


def program_details(request, program_id):
    """ A view to show individual program details """

    program = get_object_or_404(Program, pk=program_id)
    selected_classes = program.class_set.all()
    context = {
        'program': program,
        'selected_classes': selected_classes,
    }

    return render(request, 'items/program-details.html', context)


def class_details(request, class_id):
    """ A view to show individual class details """
    item = get_object_or_404(Class, pk=class_id)
    context = {
        'item': item,
    }

    return render(request, 'items/class-details.html', context)
