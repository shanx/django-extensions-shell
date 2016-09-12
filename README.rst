=========================
 Django Extensions Shell
=========================

.. image:: https://img.shields.io/pypi/l/django-extensions-shell.svg
   :target: https://raw.githubusercontent.com/django-extensions-shell/django-extensions-shell/master/LICENSE

.. image:: https://secure.travis-ci.org/django-extensions-shell/django-extensions-shell.svg?branch=master
    :alt: Build Status
    :target: http://travis-ci.org/django-extensions-shell/django-extensions-shell

.. image:: https://img.shields.io/pypi/v/django-extensions-shell.svg
    :target: https://pypi.python.org/pypi/django-extensions-shell/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/django-extensions-shell.svg
    :target: https://pypi.python.org/pypi/django-extensions-shell/
    :alt: Number of PyPI downloads

.. image:: https://img.shields.io/pypi/wheel/django-extensions-shell.svg
    :target: https://pypi.python.org/pypi/django-extensions-shell/
    :alt: Supports Wheel format

.. image:: https://coveralls.io/repos/django-extensions-shell/django-extensions-shell/badge.svg?branch=master
   :target: https://coveralls.io/r/django-extensions-shell/django-extensions-shell?branch=master
   :alt: Coverage

Django Extensions Shell is the `shell_plus` command extracted from the excellent Django Extensions project into its
own project. In most projects I've been only using the `shell_plus` command and to me it feels much better to
introduce a dependency on this specific code in projects then to depend on the whole Django Extensions project.


Requirements
============

Django Extensions Shell requires Django 1.8 or later.


Getting It
==========

You can get Django Extensions by using pip or easy_install::

    $ pip install django-extensions-shell
    or
    $ easy_install django-extensions-shell

If you want to install it from source, grab the git repository from GitHub and run setup.py::

    $ git clone git://github.com/shanx/django-extensions-shell.git
    $ cd django-extensions-shell
    $ python setup.py install


Installing It
=============

To enable `django_extensions` in your project you need to add it to `INSTALLED_APPS` in your projects
`settings.py` file::

    INSTALLED_APPS = (
        ...
        'django_extensions_shell',
        ...
    )


Using It
========

Run the enhanced django shell::

    $ python manage.py shell_plus


Documentation
=============

You can view documentation online at:

- https://django-extensions-shell.readthedocs.io

Or you can look at the docs/ directory in the repository.
