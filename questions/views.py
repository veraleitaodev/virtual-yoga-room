from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


class FaqView(generic.ListView):
    """ A  """

    template_name = 'questions/faq.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the last six published questions. """
        return Question.objects.order_by('pub_date')[:6]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'questions/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'questions/results.html'


def vote(request, question_id):
    """ A view to present vote form """

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'questions/detail.html',
                      {'question': question, 'error_message':
                       "You didn't select a choice.",
                       })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question_id,)))
