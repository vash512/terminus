from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from terminus.settings import API_KEY
import mandrill


# Create your views here.
def index_view(request):
    'Pagina de Bienvenida de Ontomex'
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def contacto(request):
    'Pagina de contacto de Ontomex'
    msgEnv=False
    if request.method=='POST':
        mandrill_client = mandrill.Mandrill(API_KEY)
        nombre=request.POST.get('name','')
        msg=request.POST.get('msg','')
        mail=request.POST.get('email','')
        mensaje="""
        Se ha resivido un mensaje de Contacto con Ontomex<br>
        Nombre: %s<br>
        Correo: %s<br>
        Mensaje: <br>
        %s
        """%(nombre, mail, msg)
        para=[{"email":'belen.s.uria.15@gmail.com', "type": "bcc"},
              {"email":'xtornasol512@gmail.com', "type": "bcc"}]

        message = {
                "html": mensaje,
                "subject": "Contacto con Ontomex",
                "from_email": "contacto@ontomex.com",
                "from_name": "Contacto con Ontomex",
                "to": para
            }
        result = mandrill_client.messages.send(message=message, async=False)
        msgEnv=True

    ctx={'enviado':msgEnv}
    return render_to_response('home/contacto.html',ctx,
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
    usuario=request.user
    if usuario.is_anonymous():
        if request.method=='POST':
            #solicitud de login por post
            if True:
                usuariof=request.POST.get('username','')
                clavef=request.POST.get('password','')
                acceso=authenticate(username=usuariof,password=clavef)
                if acceso is not None:
                    if acceso.is_active:
                        login(request,acceso)
                        #Pantalla del Perfil
                        return HttpResponseRedirect('/')
                    else:
                        error="Posiblemente tu usuario este baneado o desactivado, comunicate con el administrador"
                else:
                    error="El usuario no existe, verifique que este bien escrito"
            else:
                error="Datos invalidos en el formulario"
            ctx={'error':error}
            return render_to_response('home/login.html', ctx,
                          context_instance=RequestContext(request))
        else:
            #Login
            return render_to_response('home/login.html',
                          context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')


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

terminosDic = { "nombre" :"Contabilidad",
           "descripcion" : "Termino de Contabilidad",
           "areaC": "Contabilidad Financiera"}
def busqueda_list(request):
    return render_to_response('terminos/busqueda_list.html',
                          terminosDic,
                          context_instance=RequestContext(request))


@login_required(login_url='/login')
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')


def registro(request):
    usuario=request.user
    error=""
    if not usuario.is_anonymous():
        return HttpResponseRedirect('/')
    else:
        registrado=False
        if request.method=='POST':

            usuario=request.POST.get('username','')
            password=request.POST.get('password','')
            mail=request.POST.get('email','')
            try:
                user=User.objects.get(username=usuario)
            except :
                user=None
            if not user:
                try:
                    user=User.objects.get(email=mail)
                except :
                    user=None
                if not user:
                    user = User.objects.create_user(usuario, mail, password)
                    user.save()
                    registrado=True
                else:
                    error="El correo %s ya esta ciendo usado por otro usuario, seleccione otro"%(mail)
                
            else:
                error="El usuario %s ya existe, seleccionar otro nombre de cuenta"%(usuario)

        ctx={"regTer":registrado, "error": error}
        return render_to_response('home/registro.html', ctx,
                          context_instance=RequestContext(request))