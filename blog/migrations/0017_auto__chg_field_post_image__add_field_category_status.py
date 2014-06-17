# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Post.image'
        db.alter_column(u'blog_post', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))
        # Adding field 'Category.status'
        db.add_column(u'blog_category', 'status',
                      self.gf('django.db.models.fields.CharField')(default='status', max_length=240),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'Post.image'
        db.alter_column(u'blog_post', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))
        # Deleting field 'Category.status'
        db.delete_column(u'blog_category', 'status')


    models = {
        u'blog.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '240'})
        },
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Category']"}),
            'content': ('redactor.fields.RedactorField', [], {}),
            'ddate': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'empty.png'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'status': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '240'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blog.Tag']", 'symmetrical': 'False'})
        },
        u'blog.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'})
        }
    }

    complete_apps = ['blog']