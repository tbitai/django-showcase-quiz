from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.detail),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/check/', views.check, name='check'),
]