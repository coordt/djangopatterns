===================
Extend one template
===================

If all your templates extend a template that you assume exists, such as “base.html” *** You have to change each template when your project uses “site_base.html” instead.

If instead all your templates extend a known, base template in your name space and it extends the mythical “base.html” *** when the inevitable happens and the base template name changes *** changing one template makes all the others work.

If your coolapp/base.html defines all the blocks that you use, it is also trivial to *** change them to match the project’s template, just by enclosing your blocks in the appropriate base template blocks


``coolapp/base.html``

::

	{% extends "site_base.html" %}

	{% block extra_head %}
	    {% block head %}
	    {% endblock %}
	{% endblock %}

	{% block content %}
	    {% block body %}
	    {% endblock %}
	{% endblock %}

