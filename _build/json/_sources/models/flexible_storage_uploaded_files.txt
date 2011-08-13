==================================
Flexible storage of uploaded files
==================================

.. warning::
   This is just a stub document. It will be fleshed out more. If you wish to comment on it, please e-mail coreyoordt at gmail.

::

	from django.conf import settings
	from django.core.files.storage import get_storage_class

	DEFAULT_STORAGE = get_storage_class(
	getattr(settings, "MMEDIA_DEFAULT_STORAGE", settings.DEFAULT_FILE_STORAGE)
	)


::

	from massmedia.settings import IMAGE_UPLOAD_TO, DEFAULT_STORAGE

	class Image(models.Model):
	    file = models.FileField(
	        upload_to = IMAGE_UPLOAD_TO,
	        blank = True, 
	        null = True,
	        storage=DEFAULT_STORAGE())