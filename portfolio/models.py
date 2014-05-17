# ~*~ coding: utf-8 ~*~
from django.db import models
from datetime import datetime # для даты
from django.utils import timezone  # !important
from redactor.fields import RedactorField

class Category(models.Model):
	name = models.CharField('Заголовок',max_length=240)
	def __unicode__(self):
         return self.name;

class Tag(models.Model):
	name = models.CharField('Заголовок',max_length=240)
	def __unicode__(self):
         return self.name;

class Job(models.Model):
	name = models.CharField('Заголовок',max_length=240)
	desc = RedactorField('Описание',)
	ddate = models.DateTimeField('Дата публикации', default=timezone.now)  # !important
	adresse = models.CharField('Адрес',max_length=240)
	imagelogo = models.FileField('Логотип',upload_to="media/logo")
	image = models.FileField('Главная страница',upload_to="media/portfolio")
	def __unicode__(self):
         return self.name;
class Meta: # имена для админ панели
    verbose_name = ('Работа')
    verbose_name_plural = ('Работы')


def now():   # !important
  """
  Returns an aware or naive datetime.datetime, depending on settings.USE_TZ.
  """
  if settings.USE_TZ:
      # timeit shows that datetime.now(tz=utc) is 24% slower
      return datetime.utcnow().replace(tzinfo=utc)
  else:
      return datetime.now()