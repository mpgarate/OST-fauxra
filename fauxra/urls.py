from django.conf.urls import patterns, include, url
from django.contrib import admin

from questions import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fauxra.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^questions/', include('questions.urls', namespace='questions')),
)
