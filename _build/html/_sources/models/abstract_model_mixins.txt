=====================
Abstract Model Mixins
=====================

.. warning::
   This is just a stub document. It will be fleshed out more. Please don't comment on it.


GLAMKit (Gallery, Library, Archive, Museum) an Australian group, tackles this situation with a set of abstract classes that provide very basic features. 

You create your model by subclassing the classes that provide the functionality you need.

And you don’t have to stop there. You can add your own fields as well.


.. code-block:: python

	class PRBlog(EntryBase, 
	             StatusableEntryMixin):
	    
	    subhead = models.CharField()
	    pdf = models.FileField()


