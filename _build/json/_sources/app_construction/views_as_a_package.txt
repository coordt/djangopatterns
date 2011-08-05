==================
Views as a package
==================

.. warning::
   This is just a stub document. It will be fleshed out more. Please don't comment on it.

What problem does this pattern solve?
=====================================



When to use it
==============

Why should I use it?
====================

How to use it
=============


Convert views.py into

::

    views
    ├── __init__.py
    ├── foo.py
    ├── bar.py
    └── baz.py

Where __init__.py contains

::

    from foo import *
    from bar import *
    from baz import *

Sources
=======

http://stackoverflow.com/questions/2675722/django-breaking-up-views

Useful Links
============


Code Examples
=============

Where is it used?
=================

