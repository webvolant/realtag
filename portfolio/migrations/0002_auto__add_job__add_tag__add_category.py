# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Job'
        db.create_table(u'portfolio_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=240)),
            ('adresse', self.gf('django.db.models.fields.CharField')(max_length=240)),
        ))
        db.send_create_signal(u'portfolio', ['Job'])

        # Adding model 'Tag'
        db.create_table(u'portfolio_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=240)),
        ))
        db.send_create_signal(u'portfolio', ['Tag'])

        # Adding model 'Category'
        db.create_table(u'portfolio_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=240)),
        ))
        db.send_create_signal(u'portfolio', ['Category'])


    def backwards(self, orm):
        # Deleting model 'Job'
        db.delete_table(u'portfolio_job')

        # Deleting model 'Tag'
        db.delete_table(u'portfolio_tag')

        # Deleting model 'Category'
        db.delete_table(u'portfolio_category')


    models = {
        u'portfolio.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'})
        },
        u'portfolio.job': {
            'Meta': {'object_name': 'Job'},
            'adresse': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'})
        },
        u'portfolio.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'})
        }
    }

    complete_apps = ['portfolio']