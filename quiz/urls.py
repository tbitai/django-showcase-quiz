from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.first, name='first'),
    path('<int:question_id>/check/', views.check, name='check'),
]