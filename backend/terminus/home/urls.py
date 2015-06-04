# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns=patterns('home.views',
	url(r'^$','index_view', name='index'),
)