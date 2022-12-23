from .settings import *

STATIC_ROOT = "assets"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hotelleela',
        'USER': 'postgres',
        'PASSWORD': 'postgres@hotel#leela',
        'HOST': '18.116.135.213',
        'PORT': '5432',
    }
}