from django.conf.urls import patterns, url, include

from blog import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
    url(r'^category/(?P<catid>\d+)/$', views.category, name='category'), #blog/category/4
    url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
)

