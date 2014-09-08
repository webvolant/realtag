# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contactform'
        db.create_table(u'contactform_contactform', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=240)),
            ('phone_email', self.gf('django.db.models.fields.CharField')(max_length=240)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=240)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'contactform', ['Contactform'])


    def backwards(self, orm):
        # Deleting model 'Contactform'
        db.delete_table(u'contactform_contactform')


    models = {
        u'contactform.contactform': {
            'Meta': {'object_name': 'Contactform'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'phone_email': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['contactform']