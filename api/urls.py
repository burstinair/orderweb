from django.conf.urls import patterns, url

from api import views

urlpatterns = patterns('',
                       url(r'^resolve$', views.resolve, name='resolve'),
                       url(r'^submit$', views.submit, name='submit'),
)
