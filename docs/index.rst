.. django-extensions documentation master file, created by
   sphinx-quickstart on Wed Apr  1 20:39:40 2009.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the django-extensions-shell documentation!
=====================================================

Django Extensions Shell is the `shell_plus` command extracted from the excellent Django Extensions project into its
own project. In most projects I've been only using the `shell_plus` command and to me it feels much better to
only introduce a dependency on this specific code in projects then to depend on the whole Django Extensions project.

Quickstart
==========

You can get Django Extensions Shell by using pip or easy_install::

 $ pip install django-extensions-shell
 or
 $ easy_install django-extensions-shell

If you want to install it from source, grab the git repository and run setup.py::

 $ git clone git://github.com/shanx/django-extensions-shell.git
 $ cd django-extensions-shell
 $ python setup.py install

Now you will need to add the *django_extensions_shell* application to the INSTALLED_APPS
setting of your Django project *settings.py* file.::

  INSTALLED_APPS = (
      ...
      'django_extensions_shell',
  )


For more detailed instructions check out our :doc:`installation_instructions`. Enjoy.

Compatibility with versions of Python and Django
=================================================

This command will periodically follow updates done within Django Extensions so please check at:
`the Django Extensions page <https://django-extensions.readthedocs.io/en/latest/#compatibility-with-versions-of-python-and-django>`_

Contents
========

.. toctree::
   :maxdepth: 3

   shell_plus

