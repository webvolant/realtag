# ~*~ coding: utf-8 ~*~
from django.contrib import admin
from portfolio.models import Job
from portfolio.models import Category
from portfolio.models import Tag

admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Tag)
