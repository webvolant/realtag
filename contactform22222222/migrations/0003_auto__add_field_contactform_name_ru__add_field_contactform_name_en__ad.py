# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Contactform.name_ru'
        db.add_column(u'contactform_contactform', 'name_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contactform.name_en'
        db.add_column(u'contactform_contactform', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contactform.phone_email_ru'
        db.add_column(u'contactform_contactform', 'phone_email_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contactform.phone_email_en'
        db.add_column(u'contactform_contactform', 'phone_email_en',
                      self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contactform.subject_ru'
        db.add_column(u'contactform_contactform', 'subject_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contactform.subject_en'
        db.add_column(u'contactform_contactform', 'subject_en',
                      self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contactform.text_ru'
        db.add_column(u'contactform_contactform', 'text_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contactform.text_en'
        db.add_column(u'contactform_contactform', 'text_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Contactform.name_ru'
        db.delete_column(u'contactform_contactform', 'name_ru')

        # Deleting field 'Contactform.name_en'
        db.delete_column(u'contactform_contactform', 'name_en')

        # Deleting field 'Contactform.phone_email_ru'
        db.delete_column(u'contactform_contactform', 'phone_email_ru')

        # Deleting field 'Contactform.phone_email_en'
        db.delete_column(u'contactform_contactform', 'phone_email_en')

        # Deleting field 'Contactform.subject_ru'
        db.delete_column(u'contactform_contactform', 'subject_ru')

        # Deleting field 'Contactform.subject_en'
        db.delete_column(u'contactform_contactform', 'subject_en')

        # Deleting field 'Contactform.text_ru'
        db.delete_column(u'contactform_contactform', 'text_ru')

        # Deleting field 'Contactform.text_en'
        db.delete_column(u'contactform_contactform', 'text_en')


    models = {
        u'contactform.contactform': {
            'Meta': {'object_name': 'Contactform'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'phone_email': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'phone_email_en': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'phone_email_ru': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'subject_en': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'subject_ru': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['contactform']