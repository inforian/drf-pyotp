PyOTP extension for DRF (Django Rest Framework) !
=================================================

- This library uses `PyOTP`_ library for generating and verifying one-time passwords.Here OTP generation and Verification is done via DRF APIs.

- The main focus is to open an API for OTP Generation & Verification.

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

Contribution
------------
- If anyone wish to contribute in improving this library then he is most welcome, due credit will be given to every individual.

Swagger Specs
-------------
 https://app.swaggerhub.com/apis/inforian/PyOTP-REST-APIs/1.1.0

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _PyOTP: https://github.com/pyotp/pyotp
.. _here: https://app.swaggerhub.com/apis/inforian/PyOTP-REST-APIs/1.0.0