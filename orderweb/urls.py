from django.conf.urls import patterns, include, url

from api import urls

urlpatterns = patterns('',
	url(r'^api/', include(urls)),
)
