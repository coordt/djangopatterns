====================
Lazy Field Insertion
====================

The idea is allow developers to decide which models will have categories in the project’s settings.py, using a dictionary with the model as the key and the field or fields as the value.



.. code-block:: python

	'FK_REGISTRY': {
	    'flatpages.flatpage': 'category',
	    'simpletext.simpletext': (
	        'primary_category', 
	        {'name': 'secondary_category', 'related_name': 'simpletext_sec_cat'},
	    ),
	},
	'M2M_REGISTRY': {
	    'simpletext.simpletext': {'name': 'categories', 'related_name': 'm2mcats'},
	    'flatpages.flatpage': (
	        {'name': 'other_categories', 'related_name': 'other_cats'}, 
	        {'name': 'more_categories', 'related_name': 'more_cats'}, 
	    ),
	},


at the bottom of the category app's __init__.py, you can read the configuration from settings. 

loop through them 

Do a bit of error checking 

Load the model class 

Loop through the given fields 

We make sure that the field doesn't already exist by attempting to get it

Finally we add the field to the model by instantiating the field and calling its contribute_to_class method.

.. code-block:: python

	import fields

	from django.db.models import FieldDoesNotExist

	class AlreadyRegistered(Exception):
	    """
	    An attempt was made to register a model more than once.
	    """
	    pass

	# The field registry keeps track of the individual fields created.
	#  {'app.model.field': Field(**extra_params)}
	#  Useful for doing a schema migration
	field_registry = {}

	# The model registry keeps track of which models have one or more fields
	# registered.
	# {'app': [model1, model2]}
	# Useful for admin alteration
	model_registry = {}

	def register_m2m(model, field_name='categories', extra_params={}):
	    return _register(model, field_name, extra_params, fields.CategoryM2MField)

	def register_fk(model, field_name='category', extra_params={}):
	    return _register(model, field_name, extra_params, fields.CategoryFKField)

	def _register(model, field_name, extra_params={}, field=fields.CategoryFKField):
	    app_label = model._meta.app_label
	    registry_name = ".".join((app_label, model.__name__, field_name)).lower()
    
	    if registry_name in field_registry:
	        return #raise AlreadyRegistered
	    opts = model._meta
	    try:
	        opts.get_field(field_name)
	    except FieldDoesNotExist:
	        if app_label not in model_registry:
	            model_registry[app_label] = []
	        if model not in model_registry[app_label]:
	            model_registry[app_label].append(model)
	        field_registry[registry_name] = field(**extra_params)
	        field_registry[registry_name].contribute_to_class(model, field_name)

	from categories import settings
	from django.core.exceptions import ImproperlyConfigured
	from django.db.models import get_model

	for key, value in settings.FK_REGISTRY.items():
	    model = get_model(*key.split('.'))
	    if model is None:
	        raise ImproperlyConfigured('%s is not a model' % key)
	    if isinstance(value, (tuple, list)):
	        for item in value:
	            if isinstance(item, basestring):
	                register_fk(model, item)
	            elif isinstance(item, dict):
	                field_name = item.pop('name')
	                register_fk(model, field_name, extra_params=item)
	            else:
	                raise ImproperlyConfigured("CATEGORY_SETTINGS['FK_REGISTRY'] doesn't recognize the value of %s" % key)
	    elif isinstance(value, basestring):
	        register_fk(model, value)
	    elif isinstance(item, dict):
	        field_name = item.pop('name')
	        register_fk(model, field_name, extra_params=item)
	    else:
	        raise ImproperlyConfigured("CATEGORY_SETTINGS['FK_REGISTRY'] doesn't recognize the value of %s" % key)
	for key, value in settings.M2M_REGISTRY.items():
	    model = get_model(*key.split('.'))
	    if model is None:
	        raise ImproperlyConfigured('%s is not a model' % key)
	    if isinstance(value, (tuple, list)):
	        for item in value:
	            if isinstance(item, basestring):
	                register_m2m(model, item)
	            elif isinstance(item, dict):
	                field_name = item.pop('name')
	                register_m2m(model, field_name, extra_params=item)
	            else:
	                raise ImproperlyConfigured("CATEGORY_SETTINGS['M2M_REGISTRY'] doesn't recognize the value of %s: %s" % (key, item))
	    elif isinstance(value, basestring):
	        register_m2m(model, value)
	    elif isinstance(value, dict):
	        field_name = value.pop('name')
	        register_m2m(model, field_name, extra_params=value)
	    else:
	        raise ImproperlyConfigured("CATEGORY_SETTINGS['M2M_REGISTRY'] doesn't recognize the value of %s" % key)
