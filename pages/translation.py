# -*- coding: utf-8 -*-

from pages.models import Site
from modeltranslation.translator import translator, TranslationOptions


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
translator.register(Site, PostTranslationOptions)