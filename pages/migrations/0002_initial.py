# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Site'
        db.create_table(u'pages_site', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='title', max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='alias', max_length=255)),
            ('content', self.gf('ckeditor.fields.RichTextField')(default=' ')),
            ('keywords', self.gf('django.db.models.fields.TextField')(default='zweifach,')),
            ('uptodate', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('ddate', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('status', self.gf('django.db.models.fields.CharField')(default=1, max_length=240)),
        ))
        db.send_create_signal(u'pages', ['Site'])


    def backwards(self, orm):
        # Deleting model 'Site'
        db.delete_table(u'pages_site')


    models = {
        u'pages.site': {
            'Meta': {'object_name': 'Site'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'alias'", 'max_length': '255'}),
            'content': ('ckeditor.fields.RichTextField', [], {'default': "' '"}),
            'ddate': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'default': "'zweifach,'"}),
            'status': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '240'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'title'", 'max_length': '255'}),
            'uptodate': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['pages']