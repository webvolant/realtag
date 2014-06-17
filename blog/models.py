# ~*~ coding: utf-8 ~*~

from django.db import models
from django.contrib import admin
from redactor.fields import RedactorField

from datetime import datetime # для даты
from django.utils import timezone  # !important

from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail

#TIME_FORMAT = '%d.%m.%Y'
#datetime.datetime.strptime(myStr, "%Y-%m-%d %H:%M")
#null = false - для базы
#blank = true - для админки
#"required" is a valid argument for Django forms. For models, you want the keyword args blank=True (for the admin) and null=True (for the database).
# Про встраивание South не с начала проекта
from django import forms

class Category(models.Model):
    name = models.CharField(max_length=240)
    status =models.CharField(max_length=240)
    def __unicode__(self):
         return self.name;
class Meta: # имена для админ панели
    verbose_name = ('Категория')
    verbose_name_plural = ('Категории')

class Tag(models.Model):
	name = models.CharField(max_length=240)
	def __unicode__(self):
         return self.name;
class Meta: # имена для админ панели
    verbose_name = ('Тэг')
    verbose_name_plural = ('Тэги')

class Post(models.Model):
    name = models.CharField(verbose_name=u'Title',max_length=240)
    alias = models.CharField(verbose_name=u'Alias',max_length=240)
    content = RedactorField(verbose_name=u'Text') #TextField(verbose_name=u'Text') #tinymce_models.HTMLField()
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag)

    #image = models.FileField(upload_to="media")
	
    image = models.ImageField(verbose_name=u'Image',upload_to="blogpic",default="empty.png") #/media/empty.png article without foto
	
    #pdate = models.DateTimeField(auto_now=True,null=True,blank=False)
    uptodate = models.DateTimeField(verbose_name=u'Update Date', default=datetime.now())
    ddate = models.DateTimeField(verbose_name=u'Pub date', default=timezone.now)  # !important
    status = models.CharField(verbose_name=u'Status',max_length=240, default=1) # 0 or 1
    keywords = models.TextField(verbose_name=u'Keywords')
    #update_time = models.DateTimeField('date', null=True, auto_now=True,blank=True)
	#pdate = models.DateTimeField('pdate',default=datetime.now)
	#pdate = models.DateTimeField('pdate',default=datetime.now)
	#date = models.DateTimeField(auto_now=True, verbose_name=u"Date", blank=False)
	#test = models.TextField(blank=False)
	#pub_date = models.DateField(null=True, blank=True)
	#publication_date = forms.DateField(input_formats=('%d/%m/%Y',), widget=forms.DateInput(format='%d/%m/%Y'))
    def __unicode__(self):
        return self.name;
    class Meta: # имена для админ панели
        verbose_name = ('Пост')
        verbose_name_plural = ('Посты')


def now():   # !important
  """
  Returns an aware or naive datetime.datetime, depending on settings.USE_TZ.
  """
  if settings.USE_TZ:
      # timeit shows that datetime.now(tz=utc) is 24% slower
      return datetime.utcnow().replace(tzinfo=utc)
  else:
      return datetime.now()
    


