===============================
URLs that live under any prefix
===============================

.. warning::
   This is just a stub document. It will be fleshed out more. If you wish to comment on it, please e-mail coreyoordt at gmail.

It’s bad practice to hard code url paths or assume certain paths, for example that my blog app is always going to be under the path /blogs/

Django provides an easy way to abstractly reference a url and its view. All you have to do ...

Is add a url function in front of the pattern and add a name parameter. This allows you to ...

::

	from django.conf.urls.defaults import *

	urlpatterns = patterns('',
	    url(r'^$', 'coolapp_app.views.index', name='coolapp_index'),
	)


::

	<p>Go to the <a href="{% url coolapp_index %}">Index</a></p>


Retrieve the url using the url template tag or use the reverse function within your code.


::

	from django.core.urlresolvers import reverse

::

	def myview(request):
	    return HttpResponseRedirect(reverse('coolapp_index', args=[]))