from .base import *
import os

DEBUG = os.environ.get('DEBUG')

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('PG_NAME'),
        'USER': os.environ.get('PG_USER'),
        'HOST': os.environ.get('PG_HOST'),
        'PASSWORD': os.environ.get('PG_PASSWORD'),
        'PORT': os.environ.get('PG_PORT'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/usr/src/app/app/static/"
STATIC_DIR = STATIC_URL
STATICFILES_DIRS = [STATIC_DIR]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
