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
    'app',                          # The uwhvz app itself
    'django_su',                    # Ability to log in as anyone as Django admin; MUST be before `django.contrib.admin`
    'django.contrib.admin',         # Django admin interface
    'django.contrib.auth',          # Authentication framework
    'django.contrib.contenttypes',  # Tracks all models installed (models under app/models)
    'django.contrib.sessions',      # Store data on anonymous users
    'django.contrib.messages',      # Used for 'pop up' messages
    'django.contrib.staticfiles',   # Condenses static files from all places to 1 location
    'sass_processor',               # Processor to compile files from markup languages (SASS/SCSS)
    'compressor',                   # Compresses linked/inline JavaScript/CSS to 1 cached file
    'svg',                          # Adds svg template tag to use svg graphics/images in templates
    'django_user_agents',           # Identifies visitor's browser, OS, device (includes mobile, tablet, touch)
    'rest_framework',               # Provides tools to build Web APIs
    'rest_auth',                    # Provides REST API points for User management for REST framework

                                    # WAGTAIL PACKAGES
    'wagtail.contrib.forms',        # Allows single page forms for data collection
    'wagtail.contrib.redirects',    # Admin interface for creating redirects
    'wagtail.embeds',               # For embedded content in Wagtail
    'wagtail.sites',                # For organizing the website? (Documentation from Wagtail NA)
    'wagtail.users',                # User editing interface
    'wagtail.snippets',             # Wagtail interface for editing non-page models/object
    'wagtail.documents',            # Wagtail document content type
    'wagtail.images',               # Wagtail image content type
    'wagtail.search',               # Search framework for page content
    'wagtail.admin',                # Wagtail admin interface
    'wagtail.core',                 # Core functions of Wagtail (Page class, model trees, Wagtail tree, etc.)
    'modelcluster',                 # Extension of Django ForeignKey relation for Wagtail
    'taggit',                       # Internal image/document tagging for Wagtail
]

# Required middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',            # Adds security enhancements to request/response cycle
    'django.contrib.sessions.middleware.SessionMiddleware',     # Adds session support for anon users
    'django.middleware.common.CommonMiddleware',                # Allows blocking users & URL rewrites
    'django.middleware.csrf.CsrfViewMiddleware',                # Protects from cross site request forgeries
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Adds user attribute to HTTPRequest objects
    'django.contrib.messages.middleware.MessageMiddleware',     # Adds cookie/session-based message support
    'django.middleware.clickjacking.XFrameOptionsMiddleware',   # Protects from clickjacking
    'django_user_agents.middleware.UserAgentMiddleware',        # Adds user_agent attribute to 'request' in views.py
    'wagtail.core.middleware.SiteMiddleware',                   # Routes pre-defined hosts to pages in Wagtail tree
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',  # Adds interface for adding redirects
]

# Gets all URLS of the website
ROOT_URLCONF = 'uwhvz.urls'

# Configures website templates
TEMPLATES = [
    {
        # To configure Django to support Jinja2 engine
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        # Sets directory path of templates to appropriate folder
        'DIRS': [os.path.join(BASE_DIR, 'app', 'templates', 'jinja2')],
        # Look for templates in installed applications? (No)
        'APP_DIRS': False,
        # Provides additional parameters to pass to template backend
        'OPTIONS': {
            # Provides path to a Jinja2 environment; MOST IMPORTANT for Jinja2
            'environment': 'uwhvz.jinja2.environment',
            # Configures Jinja2 extentions (Wagtail, SASS processor & Compressor)
            'extensions': [
                'sass_processor.jinja2.ext.SassSrc',
                'wagtail.core.jinja2tags.core',
                'wagtail.admin.jinja2tags.userbar',
                'wagtail.images.jinja2tags.images',
                'compressor.contrib.jinja2ext.CompressorExtension',
            ],
            # List of paths to callables used to populate content when templates rendered;
            #   These take in request objects to return dictionary of items to merge with context
            #       (Though all but the last ones are the default generated; last is for spoofing a user)
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
        # Configure Django for its own template engine
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        # Look for templates in installed applications? (Yes)
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

# Gets the wsgi application from wsgi.py and wraps it in a variable
WSGI_APPLICATION = 'uwhvz.wsgi.application'

# Uses default settings of User_Agents package
USER_AGENTS_CACHE = 'default'

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

# Configure password validation; did user make a good password?
AUTH_PASSWORD_VALIDATORS = []

# Overrides Django's default user model with the website's model
AUTH_USER_MODEL = 'app.User'

# Sets authentications list (things the website tries to use to authenticate a user)
AUTHENTICATION_BACKENDS = (
    'django_su.backends.SuBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Assigns URLS for Logging in, Log Out, and Finish Logging In
WAGTAIL_FRONTEND_LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/dashboard/player'
LOGOUT_REDIRECT_URL = '/'

# Wraps HTTP requests to a transaction for the database; takes up a bit more space than if it wasn't
ATOMIC_REQUESTS = True

# Sets password hashers (for storing passwords); uses Argon2 package
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/
# Sets language & Time Zone

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
# Sets URL and Roots to media & static folders

STATIC_URL = '/static/'
STATIC_ROOT = STATIC_DIR
MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR

# Sets list of finder backends for finding static files
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
    'compressor.finders.CompressorFinder',
]

# Name of the Website (used in Admin log in)
WAGTAIL_SITE_NAME = 'UW Humans vs Zombies'

# Sets SASS (style sheet language that allows non-CSS features in CSS) settings
SASS_PRECISION = 8              # Calculates any calculation to 8 decimal places
SASS_OUTPUT_STYLE = 'compact'   # Makes coding output rules take up 1 line each for each property
SASS_PROCESSOR_ENABLED = True   # Enables the SASS processor

# Customizes messages based on type of message
MESSAGE_TAGS = {
    messages.DEBUG: 'dark',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

# Where global settings of the REST framework API are kept
REST_FRAMEWORK = {
    # Customizes process of dividing something into pages
    # Enables PageNUmberPagination style globally
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # Sets size of the pages
    'PAGE_SIZE': 10
}

# If set to True then user signups will be restricted to those who have a signup token.
# If set to False then users will be able to signup freely without token.
TOKEN_RESTRICTED_SIGNUPS = False
