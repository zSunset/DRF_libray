from .debug import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'libray',
        'USER': 'libray',
        'PASSWORD': 'stavropol26',
        'HOST': '127.0.0.1',
        'PORT': '5433',
    }
}