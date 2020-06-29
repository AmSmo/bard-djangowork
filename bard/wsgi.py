"""
WSGI config for bard project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import nltk
nltk.download('punkt')
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
