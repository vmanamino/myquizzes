from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from .models import Quiz

def index(request):
  quizzes = Quiz.objects.all()
  template = loader.get_template('namequizzes/index.html')
  context = { 'quizzes': quizzes }
  return render(request, 'namequizzes/index.html', context)

def detail(request, quiz_id):
  quiz = get_object_or_404(Quiz, pk=quiz_id)
  return render(request, 'namequizzes/detail.html', {'quiz': quiz})