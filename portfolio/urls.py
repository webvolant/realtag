# ~*~ coding: utf-8 ~*~
from django.conf.urls import patterns, url, include

from portfolio import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
)  
