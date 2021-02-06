from django.shortcuts import render
from classes.models import Category, Class
# Create your views here.


def index(request):
    """ A view to return the index page """

    category = Category.objects.all()
    classes_section = Class.objects.all().order_by
    context = {
        'classes_section': classes_section,
        'category': category,
    }

    return render(request, 'home/index.html', context)
