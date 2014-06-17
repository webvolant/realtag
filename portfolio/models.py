# ~*~ coding: utf-8 ~*~
from django.db import models
from datetime import datetime # для даты
from django.utils import timezone  # !important
from redactor.fields import RedactorField

from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail

class Category(models.Model):
    name = models.CharField(max_length=240)
    def __unicode__(self):
        return self.name;

class Tag(models.Model):
    name = models.CharField(max_length=240)
    def __unicode__(self):
        return self.name;

class Job(models.Model):
    name = models.CharField('Заголовок',max_length=240)
    desc = RedactorField('Описание')
    category = models.ManyToManyField(Category)
    ddate = models.DateTimeField('Дата публикации', default=timezone.now)  # !important
    adresse = models.CharField('Адрес',max_length=240)
    imagelog = models.ImageField(upload_to="port/logo",default="empty.png") #/media/empty.png article without foto
    image = models.ImageField(upload_to="port",default="empty.png") #/media/empty.png article without foto
    
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