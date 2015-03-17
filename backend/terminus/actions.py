# -*- coding: utf-8 -*-
from unicodedata import normalize
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.template import Context
from django.template.loader import get_template
from django.utils.encoding import smart_str

import re


def Normalizador(txt):
    #Normalizar texto
    txt = normalize('NFKD', txt).encode('ascii', 'ignore')
    #pasar a minusculas
    txt = txt.lower()
    #quitar espacios y poner -
    txt = '-'.join( txt.split() )
    #quita caracteres que no sean letras, numeros o -
    txt = re.sub("[^\w\-]", "", txt)
    return txt

def Paginador(objetos, maximo, pagina):
    paginado = Paginator(objetos, maximo)
    try:
        paginado = paginado.page(pagina)
    except PageNotAnInteger:
        paginado = paginado.page(1)
    except EmptyPage:
        paginado = paginado.page(paginado.num_pages)
    return paginado

def Archivador(plantilla, nombre, diccionario):
    d = Context(diccionario)
    htmly     = get_template(plantilla)
    html_content = htmly.render(d)
    html_content = smart_str(html_content)
    archivo=open('paginas_renderizadas/%s.html'%nombre,'w')
    archivo.write(html_content)
    archivo.close()