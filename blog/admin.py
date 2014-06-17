from django.contrib import admin
from blog.models import Category
from blog.models import Tag
from blog.models import Post

from django.contrib.admin import ModelAdmin

from sorl.thumbnail.shortcuts import get_thumbnail

#from django_summernote.admin import SummernoteModelAdmin
#rom django_summernote.widgets import SummernoteWidget

admin.site.register(Tag)


class AdminCategory(ModelAdmin):
    search_fields = ['name']
    list_display = ['name','status']
    list_filter = ['name']

admin.site.register(Category,AdminCategory)


class PostAdmin(admin.ModelAdmin):
	search_fields = ['name']   
	list_display = ('name','icon','status','category','ddate')
	list_filter = ['name','status','category']
	def icon(self, obj):
			img = obj.image
			img_resize_url = unicode(get_thumbnail(img, '100x100').url)
			html = '<a class="image-picker" href="%s"><img src="%s" alt="%s"/></a>'
			return html % (img.url, img_resize_url, img.name)
	icon.short_description = u'image'
	icon.allow_tags = True


admin.site.register(Post, PostAdmin)

