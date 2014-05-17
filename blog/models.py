# ~*~ coding: utf-8 ~*~

from django.db import models
from django.contrib import admin
from redactor.fields import RedactorField

from datetime import datetime # для даты
from django.utils import timezone  # !important

#TIME_FORMAT = '%d.%m.%Y'
#datetime.datetime.strptime(myStr, "%Y-%m-%d %H:%M")
#null = false - для базы
#blank = true - для админки
#"required" is a valid argument for Django forms. For models, you want the keyword args blank=True (for the admin) and null=True (for the database).
# Про встраивание South не с начала проекта
from django import forms

class Category(models.Model):
	name = models.CharField(max_length=240)
	def __unicode__(self):
         return self.name;

class Tag(models.Model):
	name = models.CharField(max_length=240)
	def __unicode__(self):
         return self.name;

class Post(models.Model):
	name = models.CharField(max_length=240)
	content = RedactorField(verbose_name=u'Text') #TextField(verbose_name=u'Text') #tinymce_models.HTMLField()
	category = models.ForeignKey(Category)
	tag = models.ManyToManyField(Tag)
	alias = models.CharField(max_length=240)
	# test = models.CharField(max_length=240)
	image = models.FileField(upload_to="media")
	#pdate = models.DateTimeField(auto_now=True,null=True,blank=False)
	ddate = models.DateTimeField('pub_date', default=timezone.now)  # !important
	#update_time = models.DateTimeField('date', null=True, auto_now=True,blank=True)
	#pdate = models.DateTimeField('pdate',default=datetime.now)
	#pdate = models.DateTimeField('pdate',default=datetime.now)
	#date = models.DateTimeField(auto_now=True, verbose_name=u"Date", blank=False)
	#test = models.TextField(blank=False)
	#pub_date = models.DateField(null=True, blank=True)
	#publication_date = forms.DateField(input_formats=('%d/%m/%Y',), widget=forms.DateInput(format='%d/%m/%Y'))
	def __unicode__(self):
         return self.name;



#Класс для админки, тут будут дополнительные атрибуты необходимые для админки
class PostAdmin(admin.ModelAdmin):
    # в таблице списка постов выводить только колонку title, если вы добавите еще одно имя поля, то и оно выведется
    list_display = ('name',)
    
def now():   # !important
  """
  Returns an aware or naive datetime.datetime, depending on settings.USE_TZ.
  """
  if settings.USE_TZ:
      # timeit shows that datetime.now(tz=utc) is 24% slower
      return datetime.utcnow().replace(tzinfo=utc)
  else:
      return datetime.now()
    

# связываем эту модель с моделью PostAdmin

admin.site.register(Post, PostAdmin)
