from django.conf.urls import patterns, url

from forums import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new_question, name='new_question'),
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'^create/$', views.create_question, name='create_question'),
)


