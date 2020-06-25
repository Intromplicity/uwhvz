import os

from django.core.wsgi import get_wsgi_application

# wsgi.py: wraps the wsgi application & sets the os environment default to the production settings
#   Requires: production.py (uwhvz/settings) in:
#       os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uwhvz.settings.production")
#   Used in: common.py (uwhvz/settings) in: WSGI_APPLICATION = 'uwhvz.wsgi.application'

# Sets the string environment default to production.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uwhvz.settings.production")

# Wraps the wsgi application (used in common.py)
application = get_wsgi_application()
