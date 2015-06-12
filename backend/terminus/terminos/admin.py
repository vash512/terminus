from django.contrib import admin
from terminos.models import Corpus, Termino, Documento

class TerminoAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('nombre', 'significado', 'corpus')
    search_fields=('id', 'nombre', 'descripcion','corpus__nombre', 'corpus__descripcion')
    list_filter =('corpus',)
    filter_horizontal =('documento',)
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()

class CorpusAdmin(admin.ModelAdmin):
    exclude = ('user',)
    search_fields=('id', 'nombre')
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()

class DocumentoAdmin(admin.ModelAdmin):
    search_fields=('id', 'nombre', 'descripcion')
    filter_horizontal =('areaContable',)


admin.site.register(Corpus, CorpusAdmin)
admin.site.register(Termino, TerminoAdmin)
admin.site.register(Documento, DocumentoAdmin)
