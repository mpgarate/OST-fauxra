from django.conf.urls import patterns, include, url
from django.contrib import admin

from questions import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^questions/', include('questions.urls', namespace='questions')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^images/', include('images.urls', namespace='images')),
)
