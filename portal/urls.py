from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    (r'^$', 'portal.views.home'),
    (r'^get/$', 'portal.views.get'),
)
