Hotel Krone HKB
===============

Virtual exhibition for HKB Master's Theses

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django

:License: GPLv3


About
-----

Welcome! Hotel Krone is a metaphorical space accommodating the collective efforts and phantasies of this years fine arts graduates and has been developed in long conversations and extended experiments. The unique occurrence not only comprehends the thesis of each one of the fourteen graduates and what it is about, but unexpectedly shows how their artwork can be thought about or looked at from new perspectives. Some of the work easily adapts to digital space. Some of it stubbornly resists a transformation, keeping its analog appearance even online. Being open to future developments, variants of the common have become the center of the manifold appearances in Hotel Krone.

The exhibition is open from June 28th 2020 until June 2021 and can be accessed online: https://hotelkrone.be

Creating Your Own Exhibition
----------------------------

Warning, all contents (images and sounds) are copyrighted! This project only contains the software running the exhibition. Artworks are not included.

Setting Up Your Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Checkout the repository

* Start the containers::

    $ docker-compose -f local.py up -d
    
* Create a **superuser account**::

    $ docker-compose -f local.py exec django /entrypoint python manage.py createsuperuser

* Visit the admin backend:

    http://localhost:8000

Deploy On Production
^^^^^^^^^^^^^^^^^^^^

* To use HotelKroneHKB in production, you first need to replace the domains in the file compose/production/traefix/traefix.yml

* You can start the containers::

    $ docker-compose -f production.py up -d

* This will start Django/Postgresql/Redis for the backend, Nginx to serve assets, Restreamer to capture RTMP streams, Traefix for loadbalancing and SSL and finally MangoDB/Matomo for the stats.
