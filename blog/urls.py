from django.conf.urls import patterns, url, include

from blog import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	#url(r'^(?P<id>\d+)$', 'category', name="url_category")
    
    url(r'^(?P<post_id>\d+)/$', views.detailblog, name='detailblog'),
    # vurl(r'^blog/(?P.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

