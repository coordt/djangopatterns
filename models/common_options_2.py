from django.db import models
from myapp.settings import USE_TAGGING

if USE_TAGGING:
    from tagging.fields import TagField

class Entry(models.Model):
    title = models.CharField(max_length=100)
    # Other stuff
    
    if USE_TAGGING:
        tags = TagField()
