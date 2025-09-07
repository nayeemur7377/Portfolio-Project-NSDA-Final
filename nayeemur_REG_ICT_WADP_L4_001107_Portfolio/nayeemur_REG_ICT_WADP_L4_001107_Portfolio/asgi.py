"""
ASGI config for nayeemur_REG_ICT_WADP_L4_001107_Portfolio project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nayeemur_REG_ICT_WADP_L4_001107_Portfolio.settings')

application = get_asgi_application()
