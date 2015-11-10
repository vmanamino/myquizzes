from django.conf.urls import url

from . import views

urlpatterns = [
    # /namequizzes/
    url(r'^$', views.index, name='index'),
    # /namequizzes/2/
    url(r'^(?P<quiz_id>[0-9]+)/$', views.detail, name='detail'),
  ]
