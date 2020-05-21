from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    correct = models.BooleanField()

    def __str__(self):
        return f'{self.question.text} {self.text}{" ✓" if self.correct else ""}'
