# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Order'
        db.create_table(u'orderform_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=240)),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=240)),
            ('sourcelang', self.gf('django.db.models.fields.CharField')(max_length=100, blank='true')),
            ('resultlang', self.gf('django.db.models.fields.CharField')(max_length=100, blank='true')),
            ('doc_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank='true')),
            ('comments', self.gf('django.db.models.fields.TextField')(blank='true')),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=100, blank='true')),
        ))
        db.send_create_signal(u'orderform', ['Order'])


    def backwards(self, orm):
        # Deleting model 'Order'
        db.delete_table(u'orderform_order')


    models = {
        u'orderform.order': {
            'Meta': {'object_name': 'Order'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': "'true'"}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'doc_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': "'true'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'resultlang': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': "'true'"}),
            'sourcelang': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': "'true'"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': "'true'"})
        }
    }

    complete_apps = ['orderform']