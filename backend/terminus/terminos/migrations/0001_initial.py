# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Corpus'
        db.create_table(u'terminos_corpus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'terminos', ['Corpus'])

        # Adding model 'Termino'
        db.create_table(u'terminos_termino', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('significado', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('corpus', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['terminos.Corpus'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'terminos', ['Termino'])

        # Adding M2M table for field documento on 'Termino'
        m2m_table_name = db.shorten_name(u'terminos_termino_documento')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('termino', models.ForeignKey(orm[u'terminos.termino'], null=False)),
            ('documento', models.ForeignKey(orm[u'terminos.documento'], null=False))
        ))
        db.create_unique(m2m_table_name, ['termino_id', 'documento_id'])

        # Adding model 'Documento'
        db.create_table(u'terminos_documento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('archivo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('areaContable', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['terminos.AreaContable'])),
        ))
        db.send_create_signal(u'terminos', ['Documento'])

        # Adding model 'AreaContable'
        db.create_table(u'terminos_areacontable', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaContable', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'terminos', ['AreaContable'])

        # Adding model 'UrlTermino'
        db.create_table(u'terminos_urltermino', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('termino', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['terminos.Termino'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=225)),
        ))
        db.send_create_signal(u'terminos', ['UrlTermino'])


    def backwards(self, orm):
        # Deleting model 'Corpus'
        db.delete_table(u'terminos_corpus')

        # Deleting model 'Termino'
        db.delete_table(u'terminos_termino')

        # Removing M2M table for field documento on 'Termino'
        db.delete_table(db.shorten_name(u'terminos_termino_documento'))

        # Deleting model 'Documento'
        db.delete_table(u'terminos_documento')

        # Deleting model 'AreaContable'
        db.delete_table(u'terminos_areacontable')

        # Deleting model 'UrlTermino'
        db.delete_table(u'terminos_urltermino')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'terminos.areacontable': {
            'Meta': {'object_name': 'AreaContable'},
            'areaContable': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'terminos.corpus': {
            'Meta': {'object_name': 'Corpus'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'terminos.documento': {
            'Meta': {'object_name': 'Documento'},
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'areaContable': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['terminos.AreaContable']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'terminos.termino': {
            'Meta': {'object_name': 'Termino'},
            'corpus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['terminos.Corpus']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'documento': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['terminos.Documento']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'significado': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'terminos.urltermino': {
            'Meta': {'object_name': 'UrlTermino'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'termino': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['terminos.Termino']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '225'})
        }
    }

    complete_apps = ['terminos']