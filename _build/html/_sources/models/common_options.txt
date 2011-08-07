==========================================
Configurable Options for Common Situations
==========================================
.. warning::
   This is just a stub document. It will be fleshed out more. Please don't comment on it.

A few, well-known of variations
(e.g. Use django.contrib.sites?)

**models.py**
	.. literalinclude:: common_options_1.py
	   :linenos:


Another example:


**models.py**
	.. literalinclude:: common_options_2.py
	   :linenos:


You can provide for optional field settings. 

Import the setting from your own apps settings 

Based on that setting, you can optionally import classes. And in your model definition... 

Optionally declare fields. The only drawback of this depends on the type of field. Changing your mind after the initial table creation might require you to either manually add the field or drop the table and syncdb again.

Link to way to do migration with south if field is added.