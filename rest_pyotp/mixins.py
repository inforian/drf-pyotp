#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- rest_pyotp.mixins
~~~~~~~~~~~~~~

- This file includes custom mixins to customize Behaviour of any existing class
"""

# future
from __future__ import unicode_literals

# 3rd party
import pyotp

# Django

# local

# own app
from rest_pyotp.models import PyOTP


class OTPMixin(object):
    """
    Apply this mixin to Perform Various operations of PyOTP.
    """
    provision_uri = False

    def _get_random_base32_string(self):
        """Generate Random Base32 string

        """
        return pyotp.random_base32()

    def _insert_into_db(self, otp, secret=None, count=None, interval=None, data={}):
        """

        :param secret: otp secret.
        :param count: hotp count.
        :param interval: totp interval
        :param data: other data (related to provisioning uri)
        :return: otp object
        """
        fields = {
            'otp': otp,
            'secret': secret,
            'count': count,
            'interval': interval
        }

        # is provision settings is True only then save data into db
        if self.provision_uri is True:
            fields.update(**data)

        return PyOTP.objects.create(**fields)

    def _generate_hotp(self, count, provision_uri=False, data={}):
        """Generates counter-based OTPs

        """
        self.provision_uri = provision_uri
        base32string = self._get_random_base32_string()
        hotp = pyotp.HOTP(base32string)
        otp = hotp.at(count)

        # save data into db
        obj = self._insert_into_db(otp, secret=base32string, count=count, data=data)
        return self._create_response(otp, obj, hotp, data)

    def _generate_totp(self, interval, provision_uri=False, data={}):
        """Generates time-based OTPs

        """
        self.provision_uri = provision_uri
        base32string = self._get_random_base32_string()
        totp = pyotp.TOTP(base32string, interval=interval)
        otp = totp.now()

        # save data into db
        obj = self._insert_into_db(otp, secret=base32string, interval=interval, data=data)
        return self._create_response(otp, obj, totp, data)

    def _create_response(self, otp, instance, otp_type_obj, data):
        """Create Response

        :param instance: pytop model instance
        :param otp_type_obj: hotp/totp object
        :param data: other data (related to provisioning uri)
        :return: response dict
        """
        response = {
            'otp_uuid': str(instance.uuid),
            'otp': otp
        }

        # Generate provision uri if settings is True
        if self.provision_uri is True:
            provisioning_uri = otp_type_obj.provisioning_uri(**data)
            response = {
                'provisioning_uri': provisioning_uri
            }

        return response
