from django.shortcuts import render
from items.models import Lecture, Program
# Create your views here.


def index(request):
    """ A view to return the index page """

    program = Program.objects.all()
    lectures_section = Lecture.objects.all()
    programs_section = Program.objects.all()
    context = {
        'lectures_section': lectures_section,
        'programs_section': programs_section,
        'program': program,
    }

    return render(request, 'home/index.html', context)
