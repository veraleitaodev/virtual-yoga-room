from django.shortcuts import render


def faq(request):
    """ A view to return the frequently asked questions page """

    return render(request, 'questions/questions.html')
