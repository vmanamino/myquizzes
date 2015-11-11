from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Quiz

class IndexView(generic.ListView):
  template_name = 'namequizzes/index.html'
  context_object_name = 'quizzes'

  def get_queryset(self):
    return Quiz.objects.all()

class DetailView(generic.DetailView):
  model = Quiz
  template_name = 'namequizzes/detail.html'