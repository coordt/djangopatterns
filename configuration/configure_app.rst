=========================================================
You want to configure your app without modifying its code
=========================================================

.. warning::
   This is just a stub document. It will be fleshed out more. Please don't comment on it.

Django debug tool bar uses one dictionary to store all its configurations.

It creates a standard set of configurations

And then updates them with which ever options are overridden in the project’s settings.py

.. code-block:: python

	from django.conf import settings

	TOOLBAR_CONFIG = {
	    'INTERCEPT_REDIRECTS': True,
	    'SHOW_TOOLBAR_CALLBACK': default_show_toolbar,
	    'EXTRA_SIGNALS': [],
	    'HIDE_DJANGO_SQL': True,
	    'SHOW_TEMPLATE_CONTEXT': True,
	    'TAG': 'body',
	}

	TOOLBAR_CONFIG.update(getattr(settings, 'DEBUG_TOOLBAR_CONFIG', {}))