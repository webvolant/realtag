# ~*~ coding: utf-8 ~*~
from django.db import models
from django.contrib import admin
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

class Contactform(models.Model):
	name = models.CharField(verbose_name=_(u'Имя'), max_length=240)
	phone_email = models.CharField(verbose_name=_(u'Телефон или e-mail'), max_length=240)
	subject = models.CharField(verbose_name=_(u'Тема запроса'), max_length=240)
	text = models.TextField(verbose_name=_(u'Сообщение'),)
	def __unicode__(self):
         return self.name;
class Meta: # имена для админ панели
    verbose_name = ('Contact')
    verbose_name_plural = ('Contacts')

class ContactForm(ModelForm): 
	class Meta:
		model = Contactform
				

