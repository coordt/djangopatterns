===================================
Adding fieldsets to a model's admin
===================================

.. warning::
   This is just a stub document. It will be fleshed out more. If you wish to comment on it, please e-mail coreyoordt at gmail.

.. code-block:: python

	for model, modeladmin in admin.site._registry.items():
	    if model in model_registry.values() and modeladmin.fieldsets:
	        fieldsets = getattr(modeladmin, 'fieldsets', ())
	        fields = [cat.split('.')[2] for cat in registry if registry[cat] == model]
	        # check each field to see if already defined
	        for cat in fields:
	            for k,v in fieldsets:
	                if cat in v['fields']:
	                    fields.remove(cat)
	        # if there are any fields left, add them under the categories fieldset
	        if len(fields) > 0:
	            print fields
	            admin.site.unregister(model)
	            admin.site.register(model, type('newadmin', (modeladmin.__class__,), {
	                'fieldsets': fieldsets + (('Categories', {
	                    'fields': fields
	                }),)
	            }))
