:Author: Corey Oordt

==================
Views as a package
==================

**Contributors:** Corey Oordt

What problem does this pattern solve?
=====================================

Code in ``views.py`` has become unmanageable.

When to use it
==============

You want to refactor your views into several files.

Why should I use it?
====================

This pattern allows for refactoring the view code into several files without effecting the import process in other files. In other words ``from coolapp.views import foo`` still works.

Implementation
==============

.. note::

   When refactoring your code into multiple files, look deeper and see if there are better ways to accomplish the tasks, such as using generic views.

Python ``import``\ s briefly
----------------------------

This pattern takes advantage of the way that Python handles importing items into the local namespace. The statement ``from foo import views`` will work with code organized as:

.. rst-class:: caption

**Example 1**

::

	foo
	├── __init__.py
	└── views.py

as well as:

.. rst-class:: caption

**Example 2**

::

	foo
	├── __init__.py
	└── views
	    └── __init__.py

In the case of Example 2, the contents of ``foo/views/__init__.py`` is executed. The ``__init__.py`` file is going to be important in the switch from a `module  <http://docs.python.org/tutorial/modules.html#modules>`_ (one file) to a `package <http://docs.python.org/tutorial/modules.html#packages>`_ (directory with ``__init__.py``\ ).

First rename ``views.py`` to something like ``old_views.py`` to prevent name confusion. Second create the ``views`` directory and add an ``__init__.py`` file. Then refactor the ``old_views.py`` into two or more files. See Example 3.

.. rst-class:: caption

**Example 3**

::

	foo
	├── __init__.py
	├── old_views.py
	└── views
	    ├── __init__.py
	    ├── bar.py
	    └── baz.py

.. note::

   When refactoring your views, you will probably need to change imports from other modules in your app, such as models. The statement ``from models import Foo`` will no longer work since the ``models.py`` file is not in the same directory.
   
   Instead, you will need to use a full path import: ``from foo.models import Foo``\ .

Now, to make imports such as ``from views import bar_detail_view`` work, we need to add a couple of lines to ``views/__init__.py``

.. rst-class:: caption

**views/__init__.py**

.. code-block:: python
   :linenos:

    from bar import *
    from baz import *

These statements import all the contents of ``views.bar`` and ``views.baz`` into ``views``\ . You can limit what is imported with ``*`` defining a list named ``__all__`` (see `Importing * from a Package <http://docs.python.org/tutorial/modules.html#importing-from-a-package>`_\ ) within the module.

``__all__`` it is taken to be the list of names that should be imported when ``from module import *`` is encountered. Django uses this often, such as in ``django.conf.urls.defaults``\ .

.. attention::

   It is up to you to maintain the ``__all__`` list as you update the file.


Sources
=======

http://stackoverflow.com/questions/2675722/django-breaking-up-views


