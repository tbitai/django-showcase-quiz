from django.shortcuts import render

from .models import Question

def first(request):
    first_question = Question.objects.earliest('id')
    context = {'first_question': first_question}
    return render(request, 'quiz/first.html', context)

def check(request):
    pass
    