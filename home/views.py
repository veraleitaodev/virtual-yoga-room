from django.shortcuts import render
from products.models import Category, Class, Program
# Create your views here.


def index(request):
    """ A view to return the index page """

    category = Category.objects.all()
    program = Program.objects.all()
    classes_section = Class.objects.all().order_by
    context = {
        'classes_section': classes_section,
        'category': category,
        'program': program,
    }

    return render(request, 'home/index.html', context)
