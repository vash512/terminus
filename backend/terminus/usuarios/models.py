# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User



class Perfil(models.Model):
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
    user = models.ForeignKey(User, unique=True)
    ciudadOrigen = models.CharField(max_length=255, blank=True, null=True)
    gradoEstudios = models.CharField(max_length=254, blank=True, null=True)
    genero = models.ForeignKey('Genero', blank=True, null=True)
    def __unicode__(self):
        return "%s"%(self.user)

class Genero(models.Model):
    genero = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return "%s"%self.genero
