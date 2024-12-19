from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def detail(request, question_id):
    return HttpResponse("Question %s" % question_id)