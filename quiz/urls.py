from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.first),
    path('<int:question_id>/check/', views.check, name='check'),
]