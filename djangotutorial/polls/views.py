from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice

# Create your views here.

# render returns a HttpResponse already
# raise Http404 exception in case objects are not found
# shortcuts: get_object_or_404 and get_list_or_404

def index(request):
    # latest_question_list = Question.objects.order_by("date_posted")[:5]
    # output = " || ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    context = {
        "latest_question_list": Question.objects.order_by("date_posted")[:5]
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    # question = "Question %s: %s" % (question_id, Question.objects.get(pk=question_id).question_text)
    # choices = ' || '.join([choice.choice_text for choice in Choice.objects.filter(question=Question.objects.get(pk=question_id))])
    # return HttpResponse(question + ' || ' + choices)
    context = {
        "question": Question.objects.get(pk=question_id),
        "choice_list": Choice.objects.filter(question=Question.objects.get(pk=question_id))
    }
    return render(request, "polls/detail.html", context)