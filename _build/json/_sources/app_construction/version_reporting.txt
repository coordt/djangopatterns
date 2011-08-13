:Author: Corey Oordt

=================
Version Reporting
=================

**Contributors:** Corey Oordt

.. contents::
   :local:


What problem does this pattern solve?
=====================================

It provides a flexible method of recording and reporting your application's version.

When to use it
==============

You should use it with any application or project that has specific releases.

Why should I use it?
====================

1. It is easy to see which version is currently installed somewhere.

2. It is easy to import the version into other places, like documentation or packaging.

3. It is easy for others to test the version of your code to better handle backwards-compatibility.


Implementation
==============

`PEP 386 <http://www.python.org/dev/peps/pep-0386/#the-new-versioning-algorithm>`_ defines the standard way to specify versions within the Python community. The most common scenario is the ``Major.Minor.Micro`` with a possible ``alpha/beta/release candidate`` suffix.

Examples::

	1.0
	0.6.1
	2.1.1b1
	0.3rc2

When recording your version number you should:

* Put it within the code, so it's accessible after the package is installed

* Easily retrieve all the individual parts of the version

* Record the individual version parts as integers (where appropriate) for easy comparison

* Have a properly formatted string version available

Putting the version information in your application's ``__init__.py`` is a great, out-of-the-way place.

Here is an example that I use:

.. rst-class:: caption

**coolapp/__index__.py**

.. literalinclude:: version_reporting.py
   :linenos:

This sets up a ``__version_info__`` dictionary to hold the version fields, a ``get_version()`` function to format the ``__version_info__`` into a string, and ``__version__``\ , which is the formatted string version. It is similar to Django's method:

**django/__init__.py**
	.. literalinclude:: version_reporting_django.py
	   :linenos:


How to use it
=============

Inside your setup.py file
-------------------------

The ``setup.py`` file needs a version for your application and you can import it directly from your application, ass seen in this example taken from `django-app-skeleton <https://github.com/callowayproject/django-app-skeleton>`_\ 's ``setup.py`` file:

.. rst-class:: caption

**django-app-skeleton/skel/setup.py**

.. literalinclude:: version_reporting_appskel.py
   :linenos:


Inside your Sphinx documentation's conf.py
------------------------------------------

Sphinx also likes to have the version of your application in the formatted documentation. Since the ``conf.py`` configuration file is just Python, you can import your version.

.. rst-class:: caption

**coolapp/docs/conf.py**

.. literalinclude:: version_reporting_sphinx.py
   :linenos:
