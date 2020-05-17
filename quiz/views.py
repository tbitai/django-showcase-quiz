from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

def first(request):
    first_question = Question.objects.earliest('id')
    template = loader.get_template('quiz/first.html')
    context = {'first_question': first_question}
    return HttpResponse(template.render(context, request))
