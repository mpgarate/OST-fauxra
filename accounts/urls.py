from django.conf.urls import patterns, url
from django.contrib.auth.views import login

from accounts import views

urlpatterns = patterns('',
    url(r'^login/$', login, name='login'),
    url(r'^register/$', views.register, name='register'),
)


