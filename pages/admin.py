

from django.contrib import admin
#from modeltranslation.admin import TabbedTranslationAdmin
from pages.models import Site



#class PostAdmin(TabbedTranslationAdmin):
#    pass

admin.site.register(Site)
