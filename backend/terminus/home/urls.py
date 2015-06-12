# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns=patterns('home.views',
	url(r'^$', 'index_view', name='index'),
    url(r'^humans.txt$', TemplateView.as_view(template_name='statics/humans.txt', content_type='text/plain; charset=utf-8')),
    url(r'^robots.txt$', TemplateView.as_view(template_name='statics/robots.txt', content_type='text/plain; charset=utf-8')),
    url(r'^sitemap.xml$', TemplateView.as_view(template_name='statics/sitemap.xml', content_type='application/xml; charset=utf-8')),
    url(r'^contacto/', 'contacto' ),
    url(r'^acercade/', 'acercade'),
    url(r'^corpuscontable', 'corpus'),
    url(r'^login/', 'log_in'),
    url(r'^registro/', 'registro'),
    url(r'^logout/', 'log_out'),

)