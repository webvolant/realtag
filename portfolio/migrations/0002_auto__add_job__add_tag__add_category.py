# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Job'
        db.create_table(u'portfolio_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=240)),
            ('desc', self.gf('redactor.fields.RedactorField')()),
            ('ddate', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('adresse', self.gf('django.db.models.fields.CharField')(max_length=240)),
            ('imagelog', self.gf('django.db.models.fields.files.ImageField')(default='empty.png', max_length=100)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='empty.png', max_length=100)),
        ))
        db.send_create_signal(u'portfolio', ['Job'])

        # Adding M2M table for field category on 'Job'
        m2m_table_name = db.shorten_name(u'portfolio_job_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('job', models.ForeignKey(orm[u'portfolio.job'], null=False)),
            ('category', models.ForeignKey(orm[u'portfolio.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['job_id', 'category_id'])

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

        # Removing M2M table for field category on 'Job'
        db.delete_table(db.shorten_name(u'portfolio_job_category'))

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
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['portfolio.Category']", 'symmetrical': 'False'}),
            'ddate': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'desc': ('redactor.fields.RedactorField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'empty.png'", 'max_length': '100'}),
            'imagelog': ('django.db.models.fields.files.ImageField', [], {'default': "'empty.png'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'})
        },
        u'portfolio.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'})
        }
    }

    complete_apps = ['portfolio']