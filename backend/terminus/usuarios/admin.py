from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from usuarios.models import Perfil, Genero

admin.site.register(Perfil)
admin.site.register(Genero)