======================
Lazy Manager Insertion
======================

.. warning::
   This is just a stub document. It will be fleshed out more. If you wish to comment on it, please e-mail coreyoordt at gmail.

Loosely based on Django-mptt. It is very similar to how we handled inserting a field.
::

	COOLAPP_MODELS = {
	    'app1.Model': 'cool_manager',
	    'app2.Model': 'cool_manager',
	}


At the bottom of this app’s models.py, you can read the configuration from settings. 

loop through them and Do a bit of error checking 

Load the model class 

Loop through the given fields 

We make sure that the model doesn’t have an attribute by the same name, we add the field to the model by instantiating the manager and calling its contribute_to_class method.


::

	from django.db.models import get_model
	import django.conf import settings
	from coolapp.managers import CustomManager

	MODELS = getattr(settings, 'COOLAPP_MODELS', {})

	for model_name, mgr_name in MODELS.items():
	    if not isinstance(model_name, basestring):
	        continue
    
	    model = get_model(*model_name.split('.'))
    
	    if not getattr(model, mgr_name, False):
	        manager = CustomManager()
	        manager.contribute_to_class(model, mgr_name)