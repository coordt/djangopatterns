:Author: Corey Oordt

=========================
Configurable Applications
=========================

**Contributors:** Corey Oordt

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

.. rst-class:: caption

**coolapp/settings.py**

.. literalinclude:: configure_app1.py
   :linenos:

Here, ``COOL_WORD`` is the *internal name,* ``COOLAPP_COOL_WORD`` is the *namespaced name,* and ``'cool'`` is the *default value.*

Requiring a value for a setting
-------------------------------

For something like an API key, you will want to draw attention if it's empty. You will do this by raising an ``ImproperlyConfigured`` exception.

.. rst-class:: caption

**coolapp/settings.py**

.. literalinclude:: configure_app2.py
   :linenos:

Many settings for your application
----------------------------------

Django has internally began using dictionaries for groups of settings, such as ``DATABASES``\ . Django debug toolbar, for example, uses one dictionary to store all its configurations. 

.. rst-class:: caption

**debug_toolbar/toolbar/loader.py**

.. literalinclude:: configure_app3.py
   :linenos:

It creates a standard set of configurations in line 13, and then uses the dictionaries ``update()`` method in line 18 to add or override current key/values.


Settings with nested dictionaries
---------------------------------

If your settings dictionary has a dictionary as a value, you need to take a slightly different approach. ``dict.update()`` will completely overwrite the nested dictionaries, not merge them. To make things trickier, ``dict.update()`` doesn't return a value, so

.. code-block:: python
   :linenos:

	DEFAULT_SETTINGS.update(getattr(settings, 'FOOBAR_SETTINGS', {}))
	DEFAULT_SETTINGS['FOO'] = DEFAULT_FOO.update(DEFAULT_SETTINGS.get('FOO', {}))

leaves ``DEFAULT_SETTINGS['FOO']`` with a value of ``None``\ . So lets try something else.

.. rst-class:: caption

**supertagging/settings.py**

.. literalinclude:: configure_app4.py
   :linenos:


In this example taken from django-supertagging, line 8 shows the default values for ``SUPERTAGGING_SETTINGS['MARKUP']``\ . Line 16 retrieves the ``SUPERTAGGING_SETTINGS`` dictionary into a temporary variable using ``getattr``\ .

Line 17 merges the ``DEFAULT_SETTINGS`` dictionary with the dictionary retrieved in line 16 into a new copy. By converting each dictionary into a list of tuple-pairs with the ``items()`` method, it can combine them using the ``+`` operator. When this list is converted back into a dictionary, it uses the last found key-value pair.

Lines 18-20 merge the defaults for ``MARKUP`` with whatever the user has specified.

Turning the keys into attributes
--------------------------------
Having one dictionary for all your applications settings is all well and good, but requires more typing. Instead of typing:

.. code-block:: python
   :linenos:

   from settings import USER_SETTINGS
   if USER_SETTINGS['ENABLED']:
       # do something
       pass

it would be nice to type:

.. code-block:: python
   :linenos:

   from settings import ENABLED
   if ENABLED:
       # do something
       pass

What we want to do is convert the first set of keys into variables. Python has a built-in function called `globals() <http://docs.python.org/library/functions.html#globals>`_ that returns a dictionary of the symbol table of the current module.

If you printed the value of ``globals()`` in an empty Python script, you would see something like:

.. code-block:: python

   >>> print globals()
   {'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}

Since ``globals()`` returns a dictionary, you can use its ``update()`` method to alter its contents in place.

.. code-block:: python

   >>> d = {'foo': 1, 'bar': 2}
   >>> globals().update(d)
   >>> print globals()
   {'bar': 2, 'd': {'foo': 1, 'bar': 2}, '__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', 'foo': 1, '__doc__': None, '__package__': None}

.. warning::

   While the effect of this is localized to this module, you must be careful with the names of the dictionary keys. If there is a naming conflict, your dictionary wins. That is probably not what you want.

Using the suppertagging example above, adding:

.. code-block:: python
   :linenos:

   globals().update(USER_SETTINGS)

to the bottom of the ``supertagging/settings.py`` file, gives you access to all the top-level keys of ``USER_SETTINGS`` as attributes of ``settings.py``


How to use it
=============

Access to your settings is a simple import. As shown in the previous section, you can import the entire dictionary of settings or, if you added them to the settings module, you can import them individually.
