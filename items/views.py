from django.shortcuts import render, get_object_or_404
from .models import Class, Program
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.contrib import messages
# from django.db.models import Q


def all_classes(request):
    """ A view to show all items, including sorting and search queries """

    classes = Class.objects.all()
    # query = None
    # programs = Program.objects.all()
    # sort = None
    # direction = None

    context = {
        'classes': classes
    }

    # if request.GET:
    #     if 'sort' in request.GET:
    #         sortkey = request.GET['sort']
    #         sort = sortkey
    #         if sortkey == 'name':
    #             sortkey = 'lower_name'
    #             classes = classes.annotate(lower_name=Lower('name'))

    #         if sortkey == 'program':
    #             sortkey = 'program__name'
    #             programs = 'programs.annotate()'

    #         if 'direction' in request.GET:
    #             direction = request.GET['direction']
    #             if direction == 'desc':
    #                 sortkey = f'-{sortkey}'
    #         classes = classes.order_by(sortkey)

    #     if 'program' in request.GET:
    #         programs = request.GET['program'].split(',')
    #         classes = classes.filter(program__name__in=programs)
    #         programs = Program.objects.filter(name__in=programs)

    #     if 'q' in request.GET:
    #         query = request.GET['q']
    #         if not query:
    #             messages.error(request,
    #                            ("You didn't enter any search criteria!"))
    #             return redirect(reverse('items'))

    #         queries = Q(
    #             name__icontains=query) | Q(description__icontains=query)
    #         classes = classes.filter(queries)

    # current_sorting = f'{sort}_{direction}'

    # context = {
    #     'pr': classes,
    #     'search_term': query,
    #     'current_programs': programs,
    #     'current_sorting': current_sorting,
    # }

    return render(request, 'items/classes.html', context)


def all_programs(request):
    """ A view to show all programs, including sorting and search queries """
    programs = Program.objects.all()
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
        'program_list': program_list,
        'page': page
    }

    return render(request, 'items/programs.html', context)


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
