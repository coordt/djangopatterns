from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

API_KEY = getattr(settings, 'COOLAPP_API_KEY', None)

if API_KEY is None:
    raise ImproperlyConfigured("You haven't set 'COOLAPP_API_KEY'.")
