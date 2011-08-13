============================
Easily overridable templates
============================

.. warning::
   This is just a stub document. It will be fleshed out more. If you wish to comment on it, please e-mail coreyoordt at gmail.

Templates are an important part of your pluggable app. They demonstrate how your app works. The more complex your app, the more important templates are. Following a few practices can make your templates very useful. We have two goals: 1. Get demonstrable functionality in as short a time as possible, and 2. modify the fewest templates to do so.

Instead of putting your templates loose in your templates directory where they can conflict with other apps templates, *** put them in a directory within templates, named after your app to name space them. *** Then you reference them as the relative path from templates, in this case: coolapp/base.html

::

	coolapp
	+-templates
	  +-coolapp
	    +-base.html

