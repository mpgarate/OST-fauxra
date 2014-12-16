from django.conf.urls import patterns, url

from questions import views, feeds

urlpatterns = patterns('',
    # questions
    url(r'^$', views.index, name='index'),
    url(r'^tagged/(?P<tag_slug>[\w-]+)/$', views.tagged, name='tagged'),
    url(r'^new/$', views.new_question, name='new'),
    url(r'^(?P<question_id>\d+)/$', views.show_question, name='show'),
    url(r'^(?P<question_id>\d+)/edit/$', views.edit_question, name='edit'),
    url(r'^(?P<question_id>\d+)/update/$', views.update_question, name='update'),
    url(r'^create/$', views.create_question, name='create'),

    # answers
    url(r'^(?P<question_id>\d+)/answers/new/$', views.new_answer, name='new_answer'),
    url(r'^(?P<question_id>\d+)/answers/create/$', views.create_answer,
        name='create_answer'),
    url(r'^answers/(?P<answer_id>\d+)/edit/$',
        views.edit_answer, name='edit_answer' ),
    url(r'^answers/(?P<answer_id>\d+)/update/$',
        views.update_answer, name='update_answer' ),

    # voting
    url(r'^vote_up/(?P<question_id>\d+)/$', views.vote_up, name='vote_up'),
    url(r'^vote_down/(?P<question_id>\d+)/$', views.vote_down, name='vote_down'),
    url(r'^vote_up_answer/(?P<answer_id>\d+)/$', views.vote_up_answer,
        name='vote_up_answer'),
    url(r'^vote_down_answer/(?P<answer_id>\d+)/$', views.vote_down_answer,
        name='vote_down_answer'),

    # rss
    url(r'^feed/$', feeds.LatestQuestionsFeed(), name="feed"),
    url(r'^(?P<question_id>\d+)/answers/feed/$', feeds.LatestAnswersFeed(),
        name="answers_feed"),
)

