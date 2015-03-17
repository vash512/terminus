from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from usuarios.models import Grupo, Alumno, UsuarioAlumno


class AlumnoEnLinea(admin.StackedInline):
    model = Alumno
    extra = 2

class AdminGrupo(admin.ModelAdmin):
	model = Grupo
	inlines=[AlumnoEnLinea,]

admin.site.register(UsuarioAlumno)
admin.site.register(Grupo, AdminGrupo)
admin.site.register(Alumno)