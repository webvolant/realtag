from django.conf.urls import patterns, url, include
from django.conf.urls import *


from pages import views

urlpatterns = patterns('',
	#url(r'^$', views.index, name='index'),
    url(r'^$', views.home, name='home'),

	#url(r'^$', views.site, name='site'),
	url(r'^(?P<alias>[a-z]*)/$', views.site, name='site'),
    url(r'^ckeditor/', include('ckeditor.urls')),
)