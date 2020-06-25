#!/usr/bin/env python
import os
import sys

# manage.py: a program to launch the uwhvz website
#   Requires: development.py (under uwhvz->settings),
#       in: os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uwhvz.settings.development")

# __name__ is set to its name ("manage") if imported, else set to __main__,
#   Used to ensure this program is the 'wrapper'
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uwhvz.settings.development")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
