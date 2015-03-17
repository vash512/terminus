from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from terminos.models import Corpus, Termino, Documento, AreaContable

class TerminoAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('nombre', 'significado', 'corpus')
    search_fields=('clave', 'nombre', 'descripcion','corpus__nombre', 'corpus__descripcion')
    list_filter =('corpus',)
    filter_horizontal =('documento',)
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()

class CorpusAdmin(admin.ModelAdmin):
    exclude = ('user',)
    search_fields=('clave', 'nombre', 'descripcion')
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()


admin.site.register(Corpus, CorpusAdmin)
admin.site.register(Termino, TerminoAdmin)
admin.site.register(Documento)
admin.site.register(AreaContable)
