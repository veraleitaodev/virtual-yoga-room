from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Lecture, Program


def all_programs(request):
    """ A view to show all programs, including sorting and search queries """
    programs = Program.objects.all()
    program_count = programs.count()

    query = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                programs = lectures.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            programs = programs.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('items:programs'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            programs = programs.filter(queries)
            program_count = programs.count()

    current_sorting = f'{sort}_{direction}'

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
        'page': page,
        'search_term': query,
        'current_sorting': current_sorting
    }

    return render(request, 'items/programs.html', context)


def all_lectures(request):
    """ A view to show all lectures, including sorting and search queries """

    lectures = Lecture.objects.all()
    lectures_count = lectures.count()

    query = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                lectures = lectures.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            lectures = lectures.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('items:lectures'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            lectures = lectures.filter(queries)
            lectures_count = lectures.count()

    current_sorting = f'{sort}_{direction}'

    page = request.GET.get('page', 1)
    paginator = Paginator(lectures, 6)
    try:
        lectures = paginator.page(page)
    except PageNotAnInteger:
        lectures = paginator.page(1)
    except EmptyPage:
        lectures = paginator.page(paginator.num_pages)

    context = {
        'lectures': lectures,
        'lectures_count': lectures_count,
        'search_term': query,
        'current_sorting': current_sorting,
        'page': page
    }

    return render(request, 'items/lectures.html', context)


def program_details(request, program_id):
    """ A view to show individual program details """

    program = get_object_or_404(Program, pk=program_id)
    selected_lectures = program.lecture_set.all()

    # paginator code
    paginator = Paginator(selected_lectures, 2)
    pageMd = request.GET.get('page')
    pageLg = request.GET.get('page')
    selected_lectures_md = paginator.get_page(pageMd)
    paginatorLg = Paginator(selected_lectures, 3)
    selected_lectures_lg = paginatorLg.get_page(pageLg)

    context = {
        'program': program,
        'selected_lectures': selected_lectures,
        'selected_lectures_md': selected_lectures_md,
        'selected_lectures_lg': selected_lectures_lg,
    }

    return render(request, 'items/program-details.html', context)


def lecture_details(request, lecture_id):
    """ A view to show individual lecture details """
    item = get_object_or_404(Lecture, pk=lecture_id)
    context = {
        'item': item,
    }

    return render(request, 'items/lecture-details.html', context)
