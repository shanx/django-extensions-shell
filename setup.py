# -*- coding: utf-8 -*-
"""
Based entirely on Django's own ``setup.py``.
"""
import sys

from setuptools import find_packages, setup

try:
    from setuptools.command.test import test as TestCommand

    class PyTest(TestCommand):
        user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

        def initialize_options(self):
            TestCommand.initialize_options(self)
            self.pytest_args = []

        def finalize_options(self):
            TestCommand.finalize_options(self)
            self.test_args = []
            self.test_suite = True

        def run_tests(self):
            import pytest

            errno = pytest.main(self.pytest_args)
            sys.exit(errno)

except ImportError:
    PyTest = None


version = __import__('django_extensions_shell').__version__

setup(
    name='django-extensions-shell',
    version=version,
    description="Isolated shell_plus command from django-extensions",
    long_description="""Django Extensions Shell is the `shell_plus` command extracted from the excellent Django Extensions project into its
own project. In most projects I've been only using the `shell_plus` command and to me it feels much better to
only introduce a dependency on this specific code in projects then to depend on the whole Django Extensions project.
For more information: http://github.com/shanx/django-extensions-shell""",
    author='Michael Trier',
    author_email='mtrier@gmail.com',
    maintainer='Remco Wendt',
    maintainer_email='remco.wendt@gmail.com',
    url='http://github.com/shanx/django-extensions-shell',
    license='MIT License',
    platforms=['any'],
    packages=find_packages(),
    cmdclass={'test': PyTest},
    install_requires=['six>=1.2'],
    tests_require=[
        'Django',
        'pytest',
        'pytest-django',
        'pytest-cov',
        'tox',
        'mock',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
)
