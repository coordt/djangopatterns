=============
Autodiscovery
=============

.. warning::
   This is just a stub document. It will be fleshed out more.

What problem does this pattern solve?
=====================================

An app provides a service that requires complex configuration or customization by other apps to properly use it.

When to use it
==============

Why should I use it?
====================

Implementation
==============

For each app, we need to look for an specific module inside that app's package. We can't use os.path here -- recall that modules may be imported different ways (think zip files) -- so we need to get the app's __path__ and look for the module on that path.

Step 1: find out the app's ``__path__`` Import errors here will (and should) bubble up, but a missing __path__ (which is legal, but weird) fails silently -- apps that do weird things with __path__ might need to roll their own index registration.

Step 2: use imp.find_module to find the app's search_indexes.py. For some reason imp.find_module raises ImportError if the app can't be found but doesn't actually try to import the module. So skip this app if its search_indexes.py doesn't exist

Step 3: import the app's search_index file. If this has errors we want them to bubble up.

.. rst-class:: caption

**Django Snippet 2404: Generic Autodiscovery**

.. literalinclude:: autodiscovery1.py
   :linenos:


How to use it
=============

Sources
=======

Useful Links
============

* `Generic Autodiscovery <http://djangosnippets.org/snippets/2404/>`_
* `Looking at registration patterns in Django <http://charlesleifer.com/blog/looking-registration-patterns-django/>`_
* `django-config-wizard autodiscover.py <http://code.google.com/p/django-config-wizard/source/browse/trunk/django_wizard/autodiscover.py?r=2>`_

Where is it used?
=================

