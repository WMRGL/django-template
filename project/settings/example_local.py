from project.settings.base import *

# Version
VERSION = "0.1.0"

# Security
DEBUG = True
ALLOWED_HOSTS = []
SECRET_KEY = ''

# Database
DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'TEST': {
        }
    }
}

# Channels
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_rabbitmq.core.RabbitmqChannelLayer',
        'CONFIG': {
            'host': 'amqp://<vhost_user>:<vhost_passwd>@127.0.0.1:5672/<vhost>'
        }
    }
}

# Celery
CELERY_BROKER_URL = 'amqp://<vhost_user>:<vhost_passwd>@127.0.0.1:5672/<vhost>'
CELERY_RESULT_BACKEND = 'rpc'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_ROOT = BASE_DIR / 'static' / f"v{VERSION}"
STATIC_DIR = STATIC_ROOT
STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR / 'media' / 'files'
MEDIA_URL = '/media/'


