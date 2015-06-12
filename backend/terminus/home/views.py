from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect as redir
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def index_view(request):
    'Pagina de Bienvenida de Ontomex'
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def contacto(request):
    'Pagina de contacto de Ontomex'
    return render_to_response('home/contacto.html',
                          context_instance=RequestContext(request))

def acercade(request):
    'Pagina de acerca de Ontomex'
    return render_to_response('home/acercade.html',
                          context_instance=RequestContext(request))

def corpus(request):
    'Pagina de corpus donde se muestran los terminos contables'
    return render_to_response('home/corpus.html',
                          context_instance=RequestContext(request))

def log_in(request):
    'Pagina de Login(Inicio de sesion) de Ontomex'
    return render_to_response('home/login.html',
                          context_instance=RequestContext(request))

def registro(request):
    return render_to_response('home/registro.html',
                          context_instance=RequestContext(request))

def terminos(request):
    return render_to_response('terminos/terminos.html',
                          context_instance=RequestContext(request))

def termino_detalle(request):
    return render_to_response('terminos/termino_detalle.html',
                          context_instance=RequestContext(request))

def docs(request):
    return render_to_response('terminos/terminos.html',
                          context_instance=RequestContext(request))

def doc_detalle(request):
    return render_to_response('terminos/termino_detalle.html',
                          context_instance=RequestContext(request))

def busqueda(request):
    return render_to_response('terminos/busqueda.html',
                          context_instance=RequestContext(request))

terminos = { "nombre" :"Contabilidad",
           "descripcion" : "Termino de Contabilidad",
           "areaC": "Contabilidad Financiera"}
def busqueda_list(request):
    return render_to_response('terminos/busqueda_list.html',
                          terminos,
                          context_instance=RequestContext(request))


@login_required(login_url='/login')
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')
