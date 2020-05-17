from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice

def first(request):
    first_question = Question.objects.earliest('id')
    context = {'first_question': first_question}
    return render(request, 'quiz/first.html', context)

def check(request, question_id):
    choice = Choice.objects.get(id=request.POST['choice'])
    return HttpResponse(choice.correct)
    