from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, welcome, post_picture, recent, load

urlpatterns = patterns('',
		url(r'^hello/$', hello), 
		url(r'^date',current_datetime),
		url(r'^$',welcome),
		url(r'^save/$',post_picture),
		url(r'^recent/$',recent),
		url(r'^recent/([^/]+)$', load),
		)




