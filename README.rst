PyOTP extension for DRF (Django Rest Framework) !
=================================================

- This library uses `PyOTP`_ library for generating and verifying one-time passwords.Here OTP generation and Verification is done via DRF APIs.

- The main focus is to open an API for OTP Generation & Verification.

Installation
------------
::

    pip install rest_pyotp

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

   url(r'', rest_pyotp.urls, name='rest-pyotp-urls')


APIs
----
- I have used swagger-spec for documenting APIs. You can find out APIs swagger docs at::

   http://{your-base-path}/pyotp-swagger/

Contribution
------------
- If anyone wish to contribute in improving this library then he is most welcome, due credit will be given to every individual.


.. _PyOTP: https://github.com/pyotp/pyotp
