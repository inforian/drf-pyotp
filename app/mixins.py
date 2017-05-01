#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- apps.mixins
~~~~~~~~~~~~~~

- This file includes custom mixins to customize Behaviour of any existing class
"""

# future
from __future__ import unicode_literals

# 3rd party
import pyotp

# Django
from django.conf import settings

# local

# own app
from app.models import PyOTP


class OTPMixin(object):
    """
    Apply this mixin to Perform Various operations of PyOTP.
    """

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
        if settings.PROVISION_URI is True:
            fields.update(**data)

        return PyOTP.objects.create(**fields)

    def _generate_hotp(self, count, data={}):
        """Generates counter-based OTPs

        """
        base32string = self._get_random_base32_string()
        hotp = pyotp.HOTP(base32string)
        otp = hotp.at(count)

        # save data into db
        obj = self._insert_into_db(otp, secret=base32string, count=count, data=data)
        return self._create_response(otp, obj, hotp, data)

    def _generate_totp(self, interval, data={}):
        """Generates time-based OTPs

        """
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
        if settings.PROVISION_URI is True:
            provisioning_uri = otp_type_obj.provisioning_uri(**data)
            response.update({
                'provisioning_uri': provisioning_uri
            })

        return response
