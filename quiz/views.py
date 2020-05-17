from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

from .models import Question, Choice

def detail(request, question_id=None):
    question = Question.objects.earliest('id') if question_id is None else Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'quiz/detail.html', context)

def check(request, question_id):
    choice = Choice.objects.get(id=request.POST['choice'])
    if choice.correct:
        messages.success(request, 'That\'s right!')
    else:
        messages.error(request, 'Wrong!')
    next_question = Question.objects.filter(id__gt=question_id).earliest('id')
    return HttpResponseRedirect(reverse('quiz:detail', args=(next_question.id,)))
    