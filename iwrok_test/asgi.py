"""ASGI config for IWrok Test project."""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iwrok_test.settings")

application = get_asgi_application()
