========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |travis| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |travis| image:: https://api.travis-ci.org/vgoehler/python-random-book-names.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/vgoehler/python-random-book-names

.. |requires| image:: https://requires.io/github/vgoehler/python-random-book-names/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/vgoehler/python-random-book-names/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/vgoehler/python-random-book-names/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/vgoehler/python-random-book-names

.. |version| image:: https://img.shields.io/pypi/v/random-book-names.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/random-book-names

.. |wheel| image:: https://img.shields.io/pypi/wheel/random-book-names.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/random-book-names

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/random-book-names.svg
    :alt: Supported versions
    :target: https://pypi.org/project/random-book-names

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/random-book-names.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/random-book-names

.. |commits-since| image:: https://img.shields.io/github/commits-since/vgoehler/python-random-book-names/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/vgoehler/python-random-book-names/compare/v0.0.0...master



.. end-badges

A small programm to generate book names from dictionaries.

* Free software: BSD 3-Clause License

Installation
============

::

    pip install random-book-names

You can also install the in-development version with::

    pip install https://github.com/vgoehler/python-random-book-names/archive/master.zip


Documentation
=============


To use the project:

.. code-block:: python

    import random_book_names
    random_book_names.longest()


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
