# ~*~ coding: utf-8 ~*~
from django.conf.urls import patterns, url, include

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


from django.views.generic import TemplateView




from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='index' ),
    url(r'^access/', TemplateView.as_view(template_name='access.html'), name='access' ),
    #url(r'^access/', include('contactform.urls')),
    #url(r'^localeurl/', include('localeurl.urls')),
    #url(r'^i18n/', include('django.conf.urls.i18n')),
    #url(r'^$', "#"),
    # url(r'^blog/', include('blog.urls')),
    url(r'^pages/', include('pages.urls')),
    url(r'^blogforadmin/', include('blog.urls')),
    url(r'^portfolio/', include('portfolio.urls')),
    url(r'^order/', include('orderform.urls')),
    url(r'^administrator/', include(admin.site.urls)),
    #(r'^tinymce/', include('tinymce.urls')),
    #(r'^summernote/', include('django_summernote.urls')),
    #(r'^ckeditor/', include('ckeditor.urls')),
    (r'^redactor/', include('redactor.urls')),
    (r'^ckeditor/', include('ckeditor.urls')),
)


urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)

# В конце файла:

if settings.DEBUG:

    if settings.MEDIA_ROOT:

        urlpatterns += static(settings.MEDIA_URL,

            document_root=settings.MEDIA_ROOT)

# Эта строка опциональна и будет добавлять url'ы только при DEBUG = True

urlpatterns += staticfiles_urlpatterns()