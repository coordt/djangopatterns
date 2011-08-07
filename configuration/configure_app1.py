from django.conf import settings

COOL_WORD = getattr(settings, 'COOLAPP_COOL_WORD', 'cool')
