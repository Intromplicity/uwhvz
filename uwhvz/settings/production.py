from .common import *

# production.py: contains the settings for a LIVE website
#   Requires: common.py (under uwhvz/settings) in: from .common import *
#             db.sqlite3 (main folder) in: os.path.join(BASE_DIR, 'db.sqlite3')
#   Used in: wsgi.py (uwhvz) in: os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uwhvz.settings.production")

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = ['*']
SITE_URL = 'https://uwhvz.uwaterloo.ca'

ADMINS = [
    ('UW HvZ SuperUser', 'uwhumansvszombies@gmail.com'),

]

SERVER_EMAIL = 'uwhumansvszombies@gmail.com'
DEFAULT_FROM_EMAIL = 'uwhumansvszombies@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'uwhumansvszombies@gmail.com'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_PASSWORD']
EMAIL_PORT = 587

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

COMPRESS_OFFLINE = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
    }
}

# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_HSTS_SECONDS = 60
# SECURE_HSTS_PRELOAD = True
# X_FRAME_OPTIONS = 'DENY'
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
