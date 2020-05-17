from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

from .models import Question, Choice

def first(request):
    first_question = Question.objects.earliest('id')
    context = {'first_question': first_question}
    return render(request, 'quiz/first.html', context)

def check(request, question_id):
    choice = Choice.objects.get(id=request.POST['choice'])
    if choice.correct:
        messages.success(request, 'That\'s right!')
    else:
        messages.error(request, 'Wrong!')
    return HttpResponseRedirect(reverse('quiz:first'))
    