from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Class, Program, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q


def all_classes(request):
    """ A view to show all classes, including sorting and search queries """

    classes = Class.objects.all()
    query = None
    class_list = Class.objects.all()
    page = request.GET.get('page', 1)
    selected_category = Category.objects.all()
    selected_program = Program.objects.all()

    paginator = Paginator(class_list, 6)
    try:
        classes = paginator.page(page)
    except PageNotAnInteger:
        classes = paginator.page(1)
    except EmptyPage:
        classes = paginator.page(paginator.num_pages)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('classes'))

    context = {
        'classes': classes,
        'selected_program': selected_program,
        'selected_category': selected_category,
        'search_term': query,
    }

    queries = Q(name__icontains=query) | Q(description__icontains=query)
    classes = classes.filter(queries)

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


def class_details(request, class_id):
    """ A view to show individual class details """
    classes = get_object_or_404(Class, pk=class_id)

    class_list = Class.objects.all()
    page = request.GET.get('page', 1)
    selected_category = Category.objects.all()
    selected_program = Program.objects.all()

    paginator = Paginator(class_list, 6)
    try:
        classes = paginator.page(page)
    except PageNotAnInteger:
        classes = paginator.page(1)
    except EmptyPage:
        classes = paginator.page(paginator.num_pages)

    context = {
        'classes': classes,
        'selected_program': selected_program,
        'selected_category': selected_category,
    }

    return render(request, 'products/class_details.html', context)
