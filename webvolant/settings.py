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
    DEBUG = True
    TEMPLATE_DEBUG = True
    #MEDIA_URL = 'http://static1.grsites.com/'
else:
    DEBUG = True
    TEMPLATE_DEBUG = True
    #MEDIA_URL = 'http://127.0.0.1:8000/static/'

    



ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'localeurl',
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
    'contactform',
    'portfolio',
    #'ckeditor',
    'modeltranslation',
)


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'), 
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'localeurl.middleware.LocaleURLMiddleware',
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
    'django.core.context_processors.i18n',
    'django.contrib.auth.context_processors.auth',
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


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# эта переменная будет указывать на папку проекта

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

# путь до папки media, в общем случае она пуста в начале

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'  # URL для медии в шаблонах


STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')  # пустая папка, сюда будет собирать статику collectstatic

STATIC_URL = '/static/'  # URL для шаблонов


STATICFILES_DIRS = (

    os.path.join(BASE_DIR, 'templates/css'),
)


# "Поисковики" статики. Первый ищет статику в STATICFILES_DIRS,

# второй в папках приложений.

STATICFILES_FINDERS = (

    'django.contrib.staticfiles.finders.FileSystemFinder',

    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

)

REDACTOR_OPTIONS = {'removeStyles': True}


LANGUAGE_CODE = 'ru-RU'

LANGUAGES = (
    ('ru', 'Russian'),
    ('de', 'Deutsch'),
    ('en', 'English'),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
MODELTRANSLATION_TRANSLATION_REGISTRY = 'webvolant.translation'

# включаем систему перевода django
USE_I18N = True

# указываем, где лежат файлы перевода
LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'locale'),
)
