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

def log_in(request):
    'Pagina de Login(Inicio de sesion) de Ontomex'
    return redir('/admin')

@login_required(login_url='/login')
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')
