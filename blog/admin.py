from django.contrib import admin
from blog.models import Category
from blog.models import Tag
from blog.models import Post

#from django_summernote.admin import SummernoteModelAdmin
#rom django_summernote.widgets import SummernoteWidget

admin.site.register(Category)
admin.site.register(Tag)



# Apply summernote to all TextField in model.
#class SummernoteModelAdmin(admin.ModelAdmin):
#    formfield_overrides = {models.TextField: {'widget': SummernoteWidget}}

