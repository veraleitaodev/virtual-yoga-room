from django.shortcuts import render
from items.models import Class, Program
# Create your views here.


def index(request):
    """ A view to return the index page """

    program = Program.objects.all()
    classes_section = Class.objects.all()
    programs_section = Program.objects.all()
    context = {
        'classes_section': classes_section,
        'programs_section': programs_section,
        'program': program,
    }

    return render(request, 'home/index.html', context)
