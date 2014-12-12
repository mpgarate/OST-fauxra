from django.conf.urls import patterns, url

from images import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<image_id>\d+)/$', views.show, name='show'),
    url(r'^new/$', views.new, name='new'),
    url(r'^create/$', views.create, name='create'),
)


