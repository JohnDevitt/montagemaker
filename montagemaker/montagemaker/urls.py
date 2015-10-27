# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    (r'^', include('montage.urls')),
) + static(settings.MEDIA_URL, montage_root=settings.MEDIA_ROOT)