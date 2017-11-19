PyOTP extension for DRF (Django Rest Framework) !
=================================================

.. image:: https://readthedocs.org/projects/drf-pyotp/badge/?version=latest
    :target: http://drf-pyotp.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://badge.fury.io/py/drf-pyotp.svg
    :target: https://badge.fury.io/py/drf-pyotp

.. image:: https://travis-ci.org/inforian/drf-pyotp.svg?branch=master
    :target: https://travis-ci.org/inforian/drf-pyotp

.. image:: https://coveralls.io/repos/github/inforian/drf-pyotp/badge.svg?branch=master
    :target: https://coveralls.io/github/inforian/drf-pyotp?branch=master


- This library uses `PyOTP`_ library for generating and verifying one-time passwords.Here OTP generation and Verification is done via DRF APIs.

- The main focus is to open an API for OTP Generation & Verification.

- Supports Python2.7+, Django 1.8+


Installation
------------
::

    pip install drf-pyotp

Usage
-----
- Add `rest_pyotp` app in your installed apps::

   INSTALLED_APPS = (
        ...
        'rest_pyotp',
    )

- Run migrations using::

   python manage.py migrate

- Add Urls in your url file::

   url(r'', include('rest_pyotp.routers', namespace='rest-pyotp-urls')),


APIs
----
- I have used swagger-spec for documenting APIs. You can find out APIs swagger docs `here`_


Documentation
-------------
- Docs : http://drf-pyotp.readthedocs.io/en/latest/

- swagger specs :  https://app.swaggerhub.com/apis/inforian/PyOTP-REST-APIs/1.1.0

Contribution
------------
- If anyone wish to contribute in improving this library then he is most welcome, due credit will be given to every individual.

.. _PyOTP: https://github.com/pyotp/pyotp
.. _here: https://app.swaggerhub.com/apis/inforian/PyOTP-REST-APIs/1.0.0
