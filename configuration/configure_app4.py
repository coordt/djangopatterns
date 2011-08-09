DEFAULT_SETTINGS = {
    'ENABLED': False,
    'DEBUG': False,
    
    # ... other settings
}

DEFAULT_MARKUP_SETTINGS = {
    'ENABLED': False,
    'FIELD_SUFFIX': "tagged",
    'EXCLUDE': [],
    'CONTENT_CACHE_TIMEOUT': 3600,
    'MIN_RELEVANCE': 0,
}

temp_settings = getattr(settings, 'SUPERTAGGING_SETTINGS', {})
USER_SETTINGS = dict(DEFAULT_SETTINGS.items() + temp_settings.items())
USER_SETTINGS['MARKUP'] = dict(
    DEFAULT_MARKUP_SETTINGS.items() + USER_SETTINGS.get('MARKUP', {}).items()
)