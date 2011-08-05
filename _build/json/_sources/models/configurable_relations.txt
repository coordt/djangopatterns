=========================
Configurable Foreign Keys
=========================

.. warning::
   This is just a stub document. It will be fleshed out more. Please don't comment on it.

We had a staff model that we wanted to related it to in some projects, but not all. So in the application settings we use a django function called get_model. This allows you to specify the model in an app-dot-model format in the project settings and then dynamically import it

.. code-block:: python

	from django.conf import settings
	from django.db.models import get_model
	
	model_string = getattr(settings, 'VIEWPOINT_AUTHOR_MODEL', 'auth.User')
	AUTHOR_MODEL = get_model(*model_string.split('.'))

Now we simply import the AUTHOR_MODEL setting, which is a django model. And use it as the parameter for the ForeignKey field.

.. code-block:: python

	from viewpoint.settings import AUTHOR_MODEL
	
	class Entry(models.Model):
	    title = models.CharField(max_length=100)
	    author = models.ForeignKey(AUTHOR_MODEL)
	    ...