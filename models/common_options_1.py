from django.db import models
from coolapp.settings import MULTIPLE_SITES, SINGLE_SITE

if MULTIPLE_SITES or SINGLE_SITE:
    from django.contrib.sites.models import Site

class Entry(models.Model):
    title = models.CharField(max_length=100)
    # Other stuff
    
    if MULTIPLE_SITES:
        sites = models.ManyToManyField(Site)
    if SINGLE_SITE:
        sites = models.ForeignKey(Site)
