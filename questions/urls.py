from django.conf.urls import patterns, url

from questions import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new_question, name='new'),
    url(r'^(?P<question_id>\d+)/$', views.show_question, name='show'),
    url(r'^create/$', views.create_question, name='create'),
    url(r'^(?P<question_id>\d+)/answers/new/$', views.new_answer, name='new_answer'),
    url(r'^(?P<question_id>\d+)/answers/create/$', views.create_answer,
        name='create_answer'),
)


