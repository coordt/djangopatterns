=========================
Configurable Applications
=========================

.. warning::
   This is just a stub document. It will be fleshed out more. Please don't comment on it.

.. contents::
   :local:

What problem does this pattern solve?
=====================================

You want to allow configuration of your app without having to modify its code. You may also want to provide reasonable defaults that users can override.

When to use it
==============

Use this whenever project- or implementation-specific information is required at runtime or there are obvious choices or options for the application.

Good examples:

* API key
* Debugging flags
* Location(s) to look for files
* Which features should be used (feature flags)

Implementation
==============

Create a ``settings.py`` file in your application

::

	coolapp
	├── __init__.py
	├── admin.py
	├── models.py
	├── settings.py
	├── tests.py
	└── views.py

Basic Pattern with one setting
------------------------------

Inside the ``settings.py`` file, you will import Django's settings and use ``getattr()`` to retrieve the value, or use a default value. There are several parts to this:

* **Internal Name:** The name you will use within your application
* **Namespaced Name:** The name used in a project's ``settings.py``\ , with a prefix to avoid collisions.
* **Default Value:** The value for this setting if the namespaced name is not in the project's ``settings.py``\ .

**coolapp/settings.py**
	.. literalinclude:: configure_app1.py
	   :linenos:

Here, ``COOL_WORD`` is the *internal name,* ``COOLAPP_COOL_WORD`` is the *namespaced name,* and ``'cool'`` is the *default value.*

Requiring a value for a setting
-------------------------------

For something like an API key, you will want to draw attention if it's empty. You will do this by raising an ``ImproperlyConfigured`` exception.

**coolapp/settings.py**
	.. literalinclude:: configure_app2.py
	   :linenos:

Many settings for your application
----------------------------------

Django has internally began using dictionaries for groups of settings, such as ``DATABASES``\ . Django debug toolbar, for example, uses one dictionary to store all its configurations. 

**debug_toolbar/toolbar/loader.py**
	.. literalinclude:: configure_app3.py
	   :linenos:

It creates a standard set of configurations in line 13, and then uses the dictionaries ``update()`` method in line 18 to add or override current key/values.


Settings with nested dictionaries
---------------------------------


Turning the keys into attributes
--------------------------------

globals().update(USER_SETTINGS)


How to use it
=============

Sources
=======

Useful Links
============

Where is it used?
=================


