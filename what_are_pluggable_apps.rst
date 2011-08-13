========================
What are pluggable apps?
========================

.. warning::
   This is just a stub document. It will be fleshed out more. If you wish to comment on it, please e-mail coreyoordt at gmail.

Confusion between the "web app" the user sees and the Django apps that power it.

Pluggable apps are:

* Focused: focused use cases and include nothing that isn’t required. "Write programs that do one thing and do it well." — Doug McIlroy (inventor of UNIX pipes)"

* Self-contained: Everything someone needs to get the app working is declared or included. 

* Easily adaptable: A focused application can inevitably find new uses, if it doesn’t take too much for granted or make too many assumptions.

* Easily installed: Pluggable applications are installed and not modified. Applications are wired together and configured in the project. The only “Apps” in your project codebase are apps that are so specific to the project that they can’t be used elsewhere.

