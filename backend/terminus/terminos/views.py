# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect as redirect301
from terminos.models import UrlPalabra, Palabra
from actions import Paginador

maximo_paginas=3


def index_view(request):
    #La iteracion es un compusto de las urls y la palabra.
    NumdePalabras=0
    palabras=UrlPalabra.objects.all()
    pagina = request.GET.get("pagina", "")
    if palabras:
        NumdePalabras = len(palabras)
        palabras = Paginador(palabras, maximo_paginas, pagina)
    cxt = {'palabras':palabras, 'filtro':False, 'NumdePalabras':NumdePalabras}

    return render_to_response('terminos/listaPalabras.html',
                          cxt,
                          context_instance=RequestContext(request))


def palabra(request, palabra):
    pal = None
    try:
        pal = UrlPalabra.objects.get(url=palabra)
        cxt = {'palabra':pal.palabra, 'url':pal.url}
    except :
        cxt = {'palabra':pal, 'url':None}

    return render_to_response('terminos/palabra.html',
                          cxt,
                          context_instance=RequestContext(request))


def tag_palabra(request, tag):
    NumdePalabras=0
    palabras=UrlPalabra.objects.filter(palabra__tags__tag__icontains=tag)
    pagina = request.GET.get("pagina", "")
    if palabras:
        NumdePalabras = len(palabras)
        palabras = Paginador(palabras, maximo_paginas, pagina)
    cxt = {'palabras':palabras, 'filtro':True, 'tag':tag, 'NumdePalabras':NumdePalabras}

    return render_to_response('terminos/listaPalabras.html',
                          cxt,
                          context_instance=RequestContext(request))

def busqueda_palabra(request):
    NumdePalabras=0
    tag = request.GET.get("busqueda", "")
    palabras = None
    if tag:
        palabras=UrlPalabra.objects.filter(palabra__tags__tag__icontains=tag)
        pagina = request.GET.get("pagina", "")
        if palabras:
            NumdePalabras = len(palabras)
            palabras = Paginador(palabras, maximo_paginas, pagina)
    cxt = {'palabras':palabras, 'filtro':True, 'tag':tag, 'NumdePalabras':NumdePalabras}

    return render_to_response('terminos/listaPalabras.html',
                          cxt,
                          context_instance=RequestContext(request))