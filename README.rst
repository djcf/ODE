ODE - Open Data Events
======================

.. image:: https://travis-ci.org/makinacorpus/ODE.png?branch=master
    :target: https://travis-ci.org/makinacorpus/ODE

.. image:: https://coveralls.io/repos/makinacorpus/ODE/badge.png?branch=master
    :target: https://coveralls.io/r/makinacorpus/ODE

===========
THIS VERSION
===========
What is the difference between this version and makinacorpus' upstream?

* This version fixes a bug wherein a PostgreSQL server must be initialized and listening for event storage. In particular, the PostreSQL server is now replaced by an SQLite file which is faster and allows the server to be deployed with minimal administrative interaction.

* This version bundles a Dockerfile for deployment using Docker.

* This version fixes a bug wherein GET requests to /v1/sources/ fail unless an X-ODE-Provider-Id is provided. This bug occluded another bug where it was not possible to view all sources by sending a GET request to /v1/sources which made it impossible to retrieve all sources at once.


===========
DEVELOPMENT
===========

We ship a Makefile with a few useful targets to setup a development
environment.

Install in development mode (you probably want to do that in a `virtual environment <http://www.virtualenv.org>`_)::

    $ make develop

Run the test suite::

    $ make test


=============
DOCUMENTATION
=============


Full documentation is available at https://ode.readthedocs.org/


=======
AUTHORS
=======

|makinacom|_

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com


=======
LICENSE
=======

    * BSD New
