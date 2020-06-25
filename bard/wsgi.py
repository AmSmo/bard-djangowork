"""
WSGI config for bard project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/opt/python/current/app')

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bard.settings')

application = get_wsgi_application()
