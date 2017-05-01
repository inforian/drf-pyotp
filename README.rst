PyOTP extension for DRF (Django Rest Framework) !
=================================================

- This library uses `PyOTP`_ library for generating and verifying one-time passwords.Here OTP generation and Verification is done via DRF APIs.

- The main focus is to open an API for OTP Generation & Verification.

Installation
------------
::

    pip install {install_pkg_name}

Usage
-----

- **Genertae TOTP :**
   - API : http://{upstream_url}/generate-otp/totp/
   - Method : POST
   - Body : { "time":60 }
   - Response :

{
  "otp": "839750",
  "otp_uuid": "3289eee9-fb10-46dc-bf8c-e0d06eccef72"
}


Status code : 200




.. _PyOTP: https://github.com/pyotp/pyotp
