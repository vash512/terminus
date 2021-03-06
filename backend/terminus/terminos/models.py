# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from actions import Normalizador

class Corpus(models.Model):
    class Meta:
        verbose_name = "Corpus Contable"
        verbose_name_plural = "Corpus Contables"
    nombre = models.CharField(max_length=100, unique=True, verbose_name = "Area Contable")
    siglas = models.CharField(blank=True, null=True, max_length=5)
    descripcion = models.TextField()
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.nombre

class Termino(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    significado = models.CharField(max_length=10, verbose_name = "Siglas")
    documento = models.ManyToManyField('Documento', blank=True, null=True)
    corpus = models.ForeignKey(Corpus, verbose_name = "Subdominio")
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.nombre

class Documento(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    archivo = models.FileField(upload_to='archivos/documentos')
    #areaContable = models.ForeignKey('AreaContable')
    areaContable = models.ManyToManyField('Corpus', blank=True, null=True)
    def __unicode__(self):
        return self.nombre


class UrlTermino(models.Model):
    termino = models.ForeignKey('Termino')
    url = models.CharField(max_length=225)
    def __unicode__(self):
        return self.url

def update_UrlTermino(sender, instance, **kwargs):
    termino = None
    urlNormal = Normalizador(instance.nombre)
    try:
        termino =UrlTermino.objects.get(termino=instance)
    except:
        pass
    if termino:
        termino.url = urlNormal
        termino.save()
    else:
        termino = UrlTermino()
        termino.termino = instance
        termino.url = urlNormal
        termino.save()

post_save.connect(update_UrlTermino, sender=Termino, dispatch_uid="update_url_termino")
