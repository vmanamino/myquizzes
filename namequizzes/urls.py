from django.conf.urls import url

from . import views

urlpatterns = [
    # /namequizzes/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /namequizzes/2/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
  ]
