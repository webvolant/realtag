# ~*~ coding: utf-8 ~*~
from django.db import models
from ckeditor.fields import RichTextField

from datetime import datetime # для даты
from django.utils import timezone  # !important

class Site(models.Model):
    title = models.CharField(verbose_name=u'Title',max_length=255,default='title')
    alias = models.CharField(verbose_name=u'Alias',max_length=255,default='alias')
    content = RichTextField(verbose_name=u'Content',default=" ")
    keywords = models.TextField(verbose_name=u'Keywords',default="zweifach,")
    uptodate = models.DateTimeField(verbose_name=u'Update Date', default=timezone.now)
    ddate = models.DateTimeField(verbose_name=u'Pub date', default=timezone.now)  # !important
    status = models.CharField(verbose_name=u'Status',max_length=240, default=1) # 0 or 1
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name =('Site')
        verbose_name_plural = ("Sites")










