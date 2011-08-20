======================================
Introduction to decorator applications
======================================

**Contributors:** Corey Oordt

.. warning::
   This is just a stub document. It will be fleshed out more.

.. contents::
   :local:

What is a decorator app?
========================

A decorator app is an application that adds functionality to another application without the application's awareness. It is different than a Python decorator, rather it follows the idea from 
`Design Patterns: Elements of Reusable Object-Oriented Software <http://en.wikipedia.org/wiki/Design_Patterns>`_\ :

	**Intent:** Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality. 
	
	**Also Known As:** Wrapper
	
	**Motivation:** Sometimes we want to add responsibilities to individual objects, not to an entire class. A graphical user interface toolkit, for example, should let you add properties like borders or behaviors like scrolling to any user interface component.
	
	One way to add responsibilities is with inheritance. Inheriting a border from another class puts a border around every subclass instance. This is inflexible, however, because the choice of border is made statically. A client can't control how and when to decorate the component with a border.

It is different than a true decorator in that Django has no way to wrap models or applications. Instead of wrapping the model, and because we're using a dynamic language like Python, we will inject independent code into the model at runtime.

Benefits
========

Abstraction of metadata
-----------------------

When developing an application to manage data, images for example, you include data and metadata. The data is the image, or path to that image. Any other information is metadata.

For this image application, how much metadata do you include? Some metadata may seem straightforward enough to include: name, width, height, resolution and format come to mind. What about less common things such as author, usage license, categories, and tags? And some of that metadata might be shared across other data applications. A video application might also include usage license, categories and tags. Should each application store their metadata separately?

You can design data applications that store minimal amounts of metadata (metadata that is easily extracted from the image, for example) and leave other metadata to specialized decorator applications.

Metadata aggregation
--------------------

It is likely that you would want to manage taxonomy metadata like categories or tags the same way throughout a project. It's rather cumbersome if every third-party application allows for a different system for handling it. A decorator application can provide a single way to manage that metadata and aggregate it throughout a project. It is easy then to query all objects, across all applications, that are tagged *foo*\ , or are categorized as *bar*\ .

Metadata customization
----------------------

":ref:`no-two-projects-are-alike`\ " I always say, and that includes how they want to handle metadata. A checkbox stating you have reproduction rights might work in one project while another requires a much more specific licensing description. A decorator app for licensing allows the image application to ignore that bit of metadata in its code. When both apps are included in a project, however, the same image application can show different licensing options, depending on the project configuration.

Alternative data handling
-------------------------

Decorators aren't just good for metadata; they can also alter how the data is managed. Take an application to handle blog entries, for example. The primary data is the text of the entry. A good question for the application is "How does the user enter text into that field?" Most apps force a decision on the user, such as a markup language such as Textile, reStructuredText, or Markdown or a WYSIWYG editor like TinyMCE.

If no two projects are alike, might that also include text formatting? In one project, the users might want a WYSIWYG editor, while others prefer a specific markup language. A decorator app can manage that for the data app, especially if the data app includes some hooks to make it easier.


