==================================
Change the admin widget of a field
==================================

Django TinyMCE allows you to add TinyMCE functionality to your app if you make certain modifications to your app. This is great if it is your code. However, it doesn’t work so well, if it is someone else’s code. Justin forked Django-TinyMCE to provide this lazy customization. *** The configuration is simple: the app.model name is the key, and then value is a list of fields to have TinyMCE on in the admin.

::

	TINYMCE_ADMIN_FIELDS = {
	    'app1.model1': ('body',), 
	    'app1.model2': ('blog_text', 'blog_teaser')
	}


There are several steps to this process. *** The first is creating a REGISTRY variable to hold the Model and field specifications in our settings.py

::

	from django.db.models import get_model
	import django.conf import settings

	REGISTRY = {}
	ADMIN_FIELDS = getattr(settings, 'TINYMCE_ADMIN_FIELDS', {})

	for model_name, field in ADMIN_FIELDS.items():
	    if isinstance(model_name, basestring):
	        model = get_model(*model_name.split('.'))
	        if model in registry:
	            return
	        REGISTRY[model] = field


Next in out admin.py, we declare a Model admin class, with one new attribute: editor_fields. We are also going to override a standard model admin method: *** formfield for dbfield. This is the method that given a database field will return the form field to render. *** our overridden method checks to see if this field is in our list of editor_fields, and if so, returns a version using the TinyMCE widget. *** if the field is not in our list, we punt it back to the super class.

``admin.py``

::

	# Define a new ModelAdmin subclass

	class TinyMCEAdmin(admin.ModelAdmin):
	    editor_fields = ()

	    def formfield_for_dbfield(self, db_field, **kwargs):
	        if db_field.name in self.editor_fields:
	            return db_field.formfield(widget=TinyMCE())
	        return super(TinyMCEAdmin, self).formfield_for_dbfield(
	            db_field, **kwargs)



Finally, we put the two pieces together. At the bottom of admin.py we loop through the admin’s current admin registry. *** Check if the current iteration is in our registry *** if it is, we unregister that model’s current admin *** and then re-register the model with a dynamically-created class called newadmin *** that is a subclass of our previously declared admin and the model’s current admin *** and we set that new class’s editor-fields attribute to the fields in our registry

``admin.py``

::

for model, modeladmin in admin.site._registry.items():
    if model in REGISTRY:
        admin.site.unregister(model)
        admin.site.register(
            model, 
            type('newadmin', 
                (TinyMCEAdmin, modeladmin.__class__), 
                {'editor_fields': REGISTRY[model],}
            )
        )
