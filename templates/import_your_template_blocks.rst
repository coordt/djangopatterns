===========================
Import your template blocks
===========================

.. warning::
   This is just a stub document. It will be fleshed out more. If you wish to comment on it, please e-mail coreyoordt at gmail.

If each template only focuses on one template block and imports other blocks, such as extra header information, you can selectively choose which template to modify: extra_head.html to add this functionality once for all templates, or detail.html to change the content.


::

	{% extends "coolapp/base.html" %}

	{% block extra_head %}
	    {{ block.super }}
	    {% import "coolapp/extra_head.html" %}
	{% endblock %}

	{% block content %}
	    {# Important content stuff here #}



	{% endblock %}