============================================
Automatically Filling in a User in the Admin
============================================

What problem does this pattern solve?
=====================================

* Easily keep track of the last user who modified a record
* Automatically set the "author" of a record

Why should I use it?
====================

It is a safe way to save the user time and still keep track of the information.

Implementation
==============

The important parts of the implementation are:

1. The :py:class:`ForeignKey` to :py:class:`User` field needs ``blank=True``
2. Create a :py:class:`ModelForm` that assigns a fake :py:class:`User` to the field.
3. Override the :py:func:`ModelAdmin.save_model()` function to assign the ``request.user`` to the field.


For discussion we'll use this model with two relations to the :py:class:`User` model:

.. rst-class:: caption

**coolblog/models.py**

.. literalinclude:: automatically_filling_user_model.py
   :linenos:

This :py:class:`Entry` model has two fields that we want to fill automatically: ``author`` and ``last_modified_by``\ . Notice both fields have ``blank=True``\ . This is important so we can get past some initial Django validation.

Faking validation
-----------------

Whenever you save a model, Django attempts to validate it. Validation will fail without special validation tomfoolery. The first stage of validation fakery was setting ``blank=True`` on the fields. The next stage involves setting a temporary value for each field.

.. rst-class:: caption

**coolblog/forms.py**

.. literalinclude:: automatically_filling_user_form.py
   :linenos:


The lower-level Django model validation actually checks if the value of a related field is an instance of the correct class. Since a form's validation happens before any attempt to save the model, we create a new :py:class:`ModelForm`, called ``EntryForm``\ . The :py:func:`clean_author()` and :py:func:`clean_last_modified_by()` methods check for an empty value and assigns it an unsaved and empty instance of :py:class:`User`\ , and Django is happy.


Saving the model
----------------

In the model's :py:class:`ModelAdmin`\ , we make a few adjustments.

.. rst-class:: caption

**coolblog/admin.py**

.. literalinclude:: automatically_filling_user_admin.py
   :linenos:

First, we set the ``form`` attribute to the ``EntryForm`` we just created.

Then, since we don't want the author to worry about selecting themselves in the ``author`` field, we left it out of the ``fieldsets``\ . We left in the ``last_modified_by`` field for reference and made it a read-only field.

The final magic comes in the overridden :py:func:`save_model()` method on line 17. We check to see if the ``author`` attribute actually has an ``id``\ . If it doesn't, it must be the empty instance we set in ``EntryForm``\ , so we assign the ``author`` field to the current user. Since we always want to assign or re-assign the user modifying this record, the ``last_modified_by`` field is set every time.


Sources
=======

`ModelAdmin.save_model documentation <https://docs.djangoproject.com/en/1.3/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model>`_

`Audit Fields <http://agiliq.com/books/djangodesignpatterns/models.html#auditfields>`_

`Users and the admin <http://www.b-list.org/weblog/2008/dec/24/admin/>`_
