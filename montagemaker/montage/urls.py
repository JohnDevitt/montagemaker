# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('montage.views',
    url(r'^list/$', 'list', name='list'),
    url(r'^build/$', 'build', name='build'),
)