from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'libray',
        'USER': 'libray',
        'PASSWORD': 'stavropol26',
        'HOST': 'db',
        'PORT': '5432',
    }
}