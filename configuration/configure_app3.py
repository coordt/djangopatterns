"""
The main DebugToolbar class that loads and renders the Toolbar.
"""
from django.conf import settings
from django.template.loader import render_to_string

class DebugToolbar(object):

    def __init__(self, request):
        self.request = request
        self.panels = []
        base_url = self.request.META.get('SCRIPT_NAME', '')
        self.config = {
            'INTERCEPT_REDIRECTS': True,
            'MEDIA_URL': f'{base_url}/__debug__/m/',
        } | getattr(settings, 'DEBUG_TOOLBAR_CONFIG', {})
        
        # ... more code below