# -*- coding: utf-8 -*-
"""
from modeltranslation.translator import translator, TranslationOptions
from contactform.models import Contactform


class ContactformTranslationOptions(TranslationOptions):
    
    
    fields = ('name', 'phone_email','subject', 'text',)

translator.register(Contactform, ContactformTranslationOptions)

"""