from django.contrib import admin
from django.forms import ModelForm
from suit_redactor.widgets import RedactorWidget
from terminos.models import Corpus, Termino, Documento, AreaContable
from django_summernote.admin import SummernoteModelAdmin

class TerminoForm(ModelForm):
    class Meta:
        widgets = {
            'descripcion': RedactorWidget(editor_options={'lang': 'en'}),
        }

class TerminoAdmin(SummernoteModelAdmin):
    #form = TerminoForm

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
