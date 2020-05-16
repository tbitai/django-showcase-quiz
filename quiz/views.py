from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

def first(request):
    first_question = Question.objects.earliest('id')
    return HttpResponse(first_question.text)
