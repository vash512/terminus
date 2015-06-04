# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns=patterns('home.views',
	url(r'^$', 'index_view', name='index'),
    url(r'^contacto/', 'contacto' ),
    url(r'^acercade/', 'acercade'),
    url(r'^login/', 'log_in'),
    url(r'^logout/', 'log_out'),

)