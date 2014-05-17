# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Post.test'
        db.delete_column(u'blog_post', 'test')


    def backwards(self, orm):
        # Adding field 'Post.test'
        db.add_column(u'blog_post', 'test',
                      self.gf('django.db.models.fields.CharField')(default='test', max_length=240),
                      keep_default=False)


    models = {
        u'blog.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'})
        },
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Category']"}),
            'content': ('redactor.fields.RedactorField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blog.Tag']", 'symmetrical': 'False'})
        },
        u'blog.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'})
        }
    }

    complete_apps = ['blog']