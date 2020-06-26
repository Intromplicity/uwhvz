from .common import *

# development.py: contains the settings for a test website
#   Requires: common.py (under uwhvz->settings) in: from .common import *
#             db.sqlite3 (main folder) in: os.path.join(BASE_DIR, 'db.sqlite3')
#   Used in: manage.py (main folder)
#       in: os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uwhvz.settings.development")

# SECURITY WARNING: keep the secret key used in production secret!
# How data is 'encrypted'; VERY IMPORTANT
SECRET_KEY = '6e4#bj2ea@i)f*xj4ht6rrthq@f3vw9(v8az+9==pf+3ys8pb!'

# SECURITY WARNING: don't run with debug turned on in production!
#   Allows debug features. Duh.
DEBUG = True

# Sets allowed host/domain names the site can serve
ALLOWED_HOSTS = ['*']

# The site URL
SITE_URL = 'http://127.0.0.1:8000'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# Contains settings for databases used in Django; using default settings;
#   Except for os.path to find the actual path to the database instead of just the name
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Contains settings for caches used in Django; using default settings
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
    }
}

# Makes console backend write emails instead of sending them out, sending to stdout; Development only tool
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
