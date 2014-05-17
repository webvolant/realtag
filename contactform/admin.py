# -*- coding: utf-8 -*-
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from contactform.models import Contactform

class ContactformAdmin(TabbedTranslationAdmin):
    pass
    
admin.site.register(Contactform, ContactformAdmin)