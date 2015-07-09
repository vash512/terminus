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
    url(r'^ayuda', 'ayuda'),
    #terminos urls de prueba
    url(r'^terminos', 'terminos'),
    url(r'^terminos/termino', 'termino_detalle'),
    url(r'^q/$', 'busqueda'),
    url(r'^q/termino', 'busqueda_list'),
    url(r'^docs/doc', 'doc_detalle'),
    url(r'^docs/$', 'docs'),
    #estas direcciones las debe administrar terminos.urls y terminos.views
    url(r'^login/', 'log_in'),
    url(r'^registro/', 'registro'),
    url(r'^logout/', 'log_out'),

)