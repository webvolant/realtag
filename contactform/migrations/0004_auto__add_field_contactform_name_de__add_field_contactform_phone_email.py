# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Contactform.name_de'
        db.add_column(u'contactform_contactform', 'name_de',
                      self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contactform.phone_email_de'
        db.add_column(u'contactform_contactform', 'phone_email_de',
                      self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contactform.subject_de'
        db.add_column(u'contactform_contactform', 'subject_de',
                      self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contactform.text_de'
        db.add_column(u'contactform_contactform', 'text_de',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Contactform.name_de'
        db.delete_column(u'contactform_contactform', 'name_de')

        # Deleting field 'Contactform.phone_email_de'
        db.delete_column(u'contactform_contactform', 'phone_email_de')

        # Deleting field 'Contactform.subject_de'
        db.delete_column(u'contactform_contactform', 'subject_de')

        # Deleting field 'Contactform.text_de'
        db.delete_column(u'contactform_contactform', 'text_de')


    models = {
        u'contactform.contactform': {
            'Meta': {'object_name': 'Contactform'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'phone_email': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'phone_email_de': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'phone_email_en': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'phone_email_ru': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'subject_de': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'subject_en': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'subject_ru': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'text_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['contactform']