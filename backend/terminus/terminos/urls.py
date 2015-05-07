from django.conf.urls import patterns, url, include

urlpatterns = patterns('terminos.views',
    url(r'^$','index_view', name='terminos_index'),
    url(r'^tag/$','busqueda_palabra'),
    url(r'^tag/(?P<tag>[\w\-]+)/$','tag_palabra'),
    url(r'^(?P<palabra>[\w\-]+)/$','palabra'),
)