from django.shortcuts import render, get_object_or_404
from .models import Class, Program
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def all_programs(request):
    """ A view to show all programs, including sorting and search queries """
    programs = Program.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(programs, 6)
    try:
        programs = paginator.page(page)
    except PageNotAnInteger:
        programs = paginator.page(1)
    except EmptyPage:
        programs = paginator.page(paginator.num_pages)

    context = {
        'programs': programs,
        'page': page
    }

    return render(request, 'items/programs.html', context)


def all_classes(request):
    """ A view to show all items, including sorting and search queries """

    classes = Class.objects.all()
    classes_page = classes

    context = {
        'classes': classes,
        'classes-page': classes_page
        }

    return render(request, 'items/classes.html', context)


def class_details(request, class_id):
    """ A view to show individual class details """
    item = get_object_or_404(Class, pk=class_id)
    context = {
        'item': item,
    }

    return render(request, 'items/class_details.html', context)


def program_details(request, program_id):
    """ A view to show individual program details """

    program = get_object_or_404(Program, pk=program_id)
    context = {
        'program': program,
    }

    return render(request, 'items/program_details.html', context)
