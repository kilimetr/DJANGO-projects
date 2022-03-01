from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from polls.models import Question, Choice



class Polls_indexView(generic.ListView):
    template_name = "polls/polls_index.html"

    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


class Polls_detailView(generic.DetailView):
    template_name = "polls/polls_detail.html"

    model = Question


class Polls_resultsView(generic.DetailView):
    template_name = "polls/polls_results.html"

    model = Question


def Polls_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = Question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/polls_detail.html", {
            "question": question,
            "error_message": "You did not select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse("Polls:Polls_results", args = (question.id)))



