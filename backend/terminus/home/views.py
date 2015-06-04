from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def index_view(request):
    'Pagina de Bienvenida de Ontomex'
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

