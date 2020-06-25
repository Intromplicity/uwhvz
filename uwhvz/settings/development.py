from .common import *

# development.py: contains the settings for a test website
#   Requires: common.py (under uwhvz->settings) in: from .common import *
#             db.sqlite3 (main folder) in: os.path.join(BASE_DIR, 'db.sqlite3')
#   Used in: manage.py (main folder)
#       in: os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uwhvz.settings.development")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6e4#bj2ea@i)f*xj4ht6rrthq@f3vw9(v8az+9==pf+3ys8pb!'

# SECURITY WARNING: don't run with debug turned on in production!
#   Allows debug features. Duh.
DEBUG = True

ALLOWED_HOSTS = ['*']

# The site URL
SITE_URL = 'http://127.0.0.1:8000'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
