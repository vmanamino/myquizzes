import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Quiz

def create_quiz(name='What\'s up?', username='Hugo'):
  """
  creates quiz with name for quiz, and username for facebook user
  """
  return Quiz.objects.create(name=name, username=username)

class QuizModel(TestCase):

  def test_quiz_name(self):
    """
    tests model attribute name
    """
    quiz = create_quiz(name = 'What are you doing now?')
    self.assertEqual(quiz.name, 'What are you doing now?')

  def test_quiz_username(self):
    """
    tests model attribute username
    """
    quiz = create_quiz(username = 'vlad')
    self.assertEqual(quiz.username, 'vlad')

  def test_unicode_representation(self):
    """
    Object representation returns Quiz name in unicode which can be converted to string
    """
    self.assertEqual(str(create_quiz()), 'What\'s up?')

class QuizViewTests(TestCase):
  def test_index_view_with_no_quizzes(self):
    """
    No quizzes, appropriate message
    """
    response = self.client.get(reverse('namequizzes:index'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'No quizzes available')
    self.assertQuerysetEqual(response.context['quizzes'], [])
  def test_index_view_with_quizzes(self):
    """
    displays quizzes
    """
    for i in range(1,6):
      name = 'Quiz %d' %(i)
      create_quiz(name=name)
    response = self.client.get(reverse('namequizzes:index'))
    self.assertEqual(response.status_code, 200)
    self.assertQuerysetEqual(response.context['quizzes'].order_by('name'), ['<Quiz: Quiz 1>', '<Quiz: Quiz 2>', '<Quiz: Quiz 3>', '<Quiz: Quiz 4>', '<Quiz: Quiz 5>'])

  def test_detail_view_with_no_quiz(self):
    response = self.client.get(reverse('namequizzes:detail', args=(1,)))
    self.assertEqual(response.status_code, 404)

  def test_detail_view_with_quiz(self):
    quiz = create_quiz()
    response = self.client.get(reverse('namequizzes:detail', args=(quiz.id,)))
    self.assertEqual(response.status_code, 200)

