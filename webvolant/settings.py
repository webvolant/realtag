# ~*~ coding: utf-8 ~*~

"""
Django settings for webvolant project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import socket

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+*$=$a@*u(oxl1+fao4eye8!w01vk_$q=7^w01n81d2qghe0v&'

# SECURITY WARNING: don't run with debug turned on in production!

if socket.gethostname().startswith('vLinuxMint'):
    LIVEHOST = False
else: 
    LIVEHOST = True


if LIVEHOST:
    DEBUG = False
    TEMPLATE_DEBUG = False
    ALLOWED_HOSTS = [
    '.realtag.volant247.lclients.ru',  # Allow domain and subdomains
    '.realtag.volant247.lclients.ru.',  # Also allow FQDN and subdomains
    ]
    #MEDIA_URL = 'http://static1.grsites.com/'
else:
    DEBUG = True
    TEMPLATE_DEBUG = True
    #MEDIA_URL = 'http://127.0.0.1:8000/static/'
    ALLOWED_HOSTS = [
    '.127.0.0.1',  # Allow domain and subdomains
    '.127.0.0.1.',  # Also allow FQDN and subdomains
    ]

    
THUMBNAIL_DEBUG = True

# Application definition

INSTALLED_APPS = (
    #'localeurl',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    #'tinymce',
    'redactor',
    #'django-wysiwyg'
    'bootstrap3',
    'south',
    #'contactform',
    'portfolio',
    #'ckeditor',
    #'modeltranslation',
    'sorl.thumbnail',
    'pages',
    'ckeditor',
    'orderform',
    'captcha',
)

############################### VARIABLES
STATUS_SHOW = 1
STATUS_HIDE = 0


ARTICLES_COUNT = 3
ARTICLES_COUNT_PAGE = 2

###############################

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'), 
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'localeurl.middleware.LocaleURLMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.csrf.CsrfResponseMiddleware',
)

ROOT_URLCONF = 'webvolant.urls'

WSGI_APPLICATION = 'webvolant.wsgi.application'


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    #'django.core.context_processors.i18n',
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

if LIVEHOST:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'volant24_realt29',
            'USER': 'volant24_realt29',
            'PASSWORD': 'MWbKtCt1ai',
            'HOST': 'mysql2.locum.ru',
            'PORT': '3306',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'webvolant',
            'USER': 'root',
            'PASSWORD': '9c471de3',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }

CAPTCHA_BACKGROUND_COLOR = 'white'
CAPTCHA_FOREGROUND_COLOR = '#000'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-RU'
USE_I18N = True

TIME_ZONE = 'UTC'

USE_L10N = True

USE_TZ = True

# эта переменная будет указывать на папку проекта

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

# путь до папки media, в общем случае она пуста в начале

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'  # URL для медии в шаблонах

#MEDIA_ROOT = '/home/code/webvolant/media/'
#MEDIA_URL = 'http://127.0.0.1:8000/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')  # пустая папка, сюда будет собирать статику collectstatic

STATIC_URL = '/static/'  # URL для шаблонов


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'blog/templates/blog_static'),
    os.path.join(BASE_DIR, 'templates/css'),
)


# "Поисковики" статики. Первый ищет статику в STATICFILES_DIRS,

# второй в папках приложений.

STATICFILES_FINDERS = (

    'django.contrib.staticfiles.finders.FileSystemFinder',

    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

)

REDACTOR_OPTIONS = {'removeStyles': True}



#
LANGUAGES = (
    #('de', 'Deutsch'),
    ('ru', 'Russian'),

#    ('en', 'English'),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
MODELTRANSLATION_TRANSLATION_REGISTRY = 'webvolant.translation'




CKEDITOR_UPLOAD_PATH = "media/"



EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'volant247@googlemail.com'
EMAIL_HOST_PASSWORD = '9c471de3'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'volant247@googlemail.com'