from .common import *

# production.py: contains the settings for a LIVE website
#   Requires: common.py (under uwhvz/settings) in: from .common import *
#             db.sqlite3 (main folder) in: os.path.join(BASE_DIR, 'db.sqlite3')
#   Used in: wsgi.py (uwhvz) in: os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uwhvz.settings.production")

SECRET_KEY = os.environ['SECRET_KEY']

# No Debug features allowed here!
DEBUG = False

# Sets allowed host/domain names the site can serve
ALLOWED_HOSTS = ['*']

# Site URL
SITE_URL = 'https://uwhvz.uwaterloo.ca'

# List of people who get code error notifications through email (though ensure email system works!)
ADMINS = [
    ('UW HvZ SuperUser', 'uwhumansvszombies@gmail.com'),

]

SERVER_EMAIL = 'uwhumansvszombies@gmail.com'                   # Email address error msgs come from
DEFAULT_FROM_EMAIL = 'uwhumansvszombies@gmail.com'             # Email address for automated msgs from site admins
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Backend to use for sending mail; using default
EMAIL_USE_TLS = True                                           # Use TLS (secure) connection when talking to SMTP server
EMAIL_HOST = 'smtp.gmail.com'                                  # Host to use for sending email; gmail
EMAIL_HOST_USER = 'uwhumansvszombies@gmail.com'                # Username to use for SMTP server
EMAIL_HOST_PASSWORD = os.environ['EMAIL_PASSWORD']             # Password to use for SMTP server; from env. variables
EMAIL_PORT = 587                                               # Port to use for SMTP server

# Contains settings for databases used in Django; using default settings;
#   Except for os.path to find the actual path to the database instead of just the name
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Disables Compressor
COMPRESS_OFFLINE = True

# Contains settings for caches used in Django; using default settings
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
