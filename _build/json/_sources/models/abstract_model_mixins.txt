=====================
Abstract Model Mixins
=====================

.. warning::
   This is just a stub document. It will be fleshed out more. If you wish to comment on it, please e-mail coreyoordt at gmail.

What problem does this pattern solve?
=====================================

It creates a tool kit to build complex models.

When to use it
==============

For models that you will commonly build in projects but have many different potential features, and you want your models to only contain the features necessary. Blogs are a good example, where where are many potential options to include within a blog, but you don't need all of them all the time.

Why should I use it?
====================

This allows developers to fix bugs once, in the tool kit. Installing the new tool kit version will fix those bugs in each model created from it.

Where is it used?
=================

I first saw this in `GLAMkit <http://www.glamkit.com/>`_\ 's `blogtools <https://github.com/glamkit/glamkit-blogtools>`_ package. It is also used in Django 1.3's `class-based views <https://docs.djangoproject.com/en/1.3/topics/class-based-views/>`_\ .

Implementation
==============

Models
------

First isolate all the potential or optional features from core features. The core features and each isolated set of optional features will make up individual abstract Django models.

GLAMkit isolated the one base model (``EntryBase``\ ), and four optional features: add a *featured* flag, add a *status* field, add a tag field, and allow for the body and excerpt content to convert to HTML.

``EntryBase`` includes seven fields--author, title, pub_date, slug, enable_comments, excerpt, and body--as well as ``__unicode__()``\ , ``get_absolute_url()`` and ``excerpt_or_body()`` functions. The ``Meta`` class has ``abstract=True`` so that Django never tries to represent this model in a database. It must be subclassed.

``FeaturableEntryMixin`` is an abstract class that merely defines an ``is_featured`` field.

``StatusableEntryMixin`` is an abstract class that defines ``LIVE_STATUS``\ , ``DRAFT_STATUS``\ , and ``HIDDEN_STATUS`` values and choices. It defines a ``status`` field with those choices.

``TaggableEntryMixin`` is an abstract class that is only available if Django-Tagging is installed, as it uses the ``TagField`` for the ``tags`` field it defines.

``HTMLFormattableEntryMixin`` is a much more complex abstract class. It is only available if the ``template_utils`` package is available. It defines two text fields, ``excerpt_html`` and ``body_html``\ . It also overrides the ``save()`` method so it can convert the contents of ``exceprt`` and ``body`` into HTML for ``excerpt_html`` and ``body_html``\ , respectively. Finally it re-defines the ``excerpt_or_body()`` method to return the ``excerpt_html`` or ``body_html`` value.

Admin
-----

It is difficult to provide a really good ``ModelAdmin`` class when you aren't sure what fields or features are included in the final model. GLAMkit provides a ``EntryAdminBase`` which is subclassed from ``object`` (not ``ModelAdmin``\ ). Providing other admin mixins would make sense if there were admin-specific features to provide, such as adding a WYSIWYG editor, autocomplete lookups or special filtering.

URLs
----


Views
-----


Syndication Feeds
-----------------




How to use it
=============

Sources
=======

Useful Links
============


GLAMKit (Gallery, Library, Archive, Museum) an Australian group, tackles this situation with a set of abstract classes that provide very basic features. 

You create your model by subclassing the classes that provide the functionality you need.

And you don’t have to stop there. You can add your own fields as well.


.. code-block:: python

	class PRBlog(EntryBase, 
	             StatusableEntryMixin):
	    
	    subhead = models.CharField()
	    pdf = models.FileField()


