from django.conf.urls import patterns, url, include

from orderform import views

urlpatterns = patterns('',
	url(r'^$', views.order, name='order'),

)