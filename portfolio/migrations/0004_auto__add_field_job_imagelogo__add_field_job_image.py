# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Job.imagelogo'
        db.add_column(u'portfolio_job', 'imagelogo',
                      self.gf('django.db.models.fields.files.FileField')(default='imagelogo', max_length=100),
                      keep_default=False)

        # Adding field 'Job.image'
        db.add_column(u'portfolio_job', 'image',
                      self.gf('django.db.models.fields.files.FileField')(default='image', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Job.imagelogo'
        db.delete_column(u'portfolio_job', 'imagelogo')

        # Deleting field 'Job.image'
        db.delete_column(u'portfolio_job', 'image')


    models = {
        u'portfolio.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'})
        },
        u'portfolio.job': {
            'Meta': {'object_name': 'Job'},
            'adresse': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'ddate': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'imagelogo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'})
        },
        u'portfolio.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'})
        }
    }

    complete_apps = ['portfolio']