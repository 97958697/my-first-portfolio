"""
WSGI config for first_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

# add project root to sys.path
project_home = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_home not in sys.path:
    sys.path.insert(0, project_home)


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

application = get_wsgi_application()
