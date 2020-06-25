import os

from django.contrib.messages import constants as messages

# common.py: contains the website settings not for solely development/production
#   Requires: urls.py (under uwhvz) in: ROOT_URLCONF = 'uwhvz.urls'
#             jinga2.py (under uwhvz) in: 'environment': 'uwhvz.jinja2.environment',
#             wsgi.py (under uwhvz) in: WSGI_APPLICATION = 'uwhvz.wsgi.application'
#             static (folder, main folder) in: STATIC_DIR = os.path.join(BASE_DIR, 'static')
#             media (folder, main folder) in: MEDIA_DIR = os.path.join(BASE_DIR, 'media')
#             app (folder, main folder) in: 'app',
#   Used in: development.py in: from .common import *
#            urls.py (under uwhvz): common.py (under uwhvz) in:
#               urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Gets the location of the whole project; __file__ gives this file, abspath gives entire path to '__file__',
#   and dirname gives parent directory; ex: C:\Users\hi; dirname gives C:\Users
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Gets location of static folder, or makes folder if non existent
STATIC_DIR = os.path.join(BASE_DIR, 'static')
if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR)

# Gets location of media folder, or makes folder if non existent
MEDIA_DIR = os.path.join(BASE_DIR, 'media')
if not os.path.exists(MEDIA_DIR):
    os.makedirs(MEDIA_DIR)

# What packages need to be added
INSTALLED_APPS = [
    'app',
    'django_su',  # must be before ``django.contrib.admin``    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sass_processor',
    'compressor',
    'svg',
    'django_user_agents',
    'rest_framework',
    'rest_auth',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'modelcluster',
    'taggit',
]

# Required middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

# Gets all URLS of the website
ROOT_URLCONF = 'uwhvz.urls'

# Configures website templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'app', 'templates', 'jinja2')],
        'APP_DIRS': False,
        'OPTIONS': {
            'environment': 'uwhvz.jinja2.environment',
            'extensions': [
                'sass_processor.jinja2.ext.SassSrc',
                'wagtail.core.jinja2tags.core',
                'wagtail.admin.jinja2tags.userbar',
                'wagtail.images.jinja2tags.images',
                'compressor.contrib.jinja2ext.CompressorExtension',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_su.context_processors.is_su',
            ],
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'uwhvz.wsgi.application'

USER_AGENTS_CACHE = 'default'

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []

AUTH_USER_MODEL = 'app.User'

AUTHENTICATION_BACKENDS = (
    'django_su.backends.SuBackend',
    'django.contrib.auth.backends.ModelBackend',
)

WAGTAIL_FRONTEND_LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/dashboard/player'
LOGOUT_REDIRECT_URL = '/'

ATOMIC_REQUESTS = True

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = STATIC_DIR
MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
    'compressor.finders.CompressorFinder',
]

WAGTAIL_SITE_NAME = 'UW Humans vs Zombies'

SASS_PRECISION = 8
SASS_OUTPUT_STYLE = 'compact'
SASS_PROCESSOR_ENABLED = True

MESSAGE_TAGS = {
    messages.DEBUG: 'dark',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# If set to True then user signups will be restricted to those who have a signup token.
# If set to False then users will be able to signup freely without token.
TOKEN_RESTRICTED_SIGNUPS = False
