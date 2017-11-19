#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- rest_pyotp.serializer
~~~~~~~~~~~~~~

- This file contains pyotp app serializers
"""

# future
from __future__ import unicode_literals

# 3rd party
import pyotp

# DRF
from rest_framework import serializers

# Django

# local

# own app
from rest_pyotp import mixins


class NoneSerializer(serializers.Serializer):
    pass


class TotpSerializer(mixins.OTPMixin, serializers.Serializer):
    """TOTP serializer

    """
    time = serializers.IntegerField(required=True, help_text="OTP Validity-Time (in seconds).")

    def create(self, validated_data):
        """

        :param validated_data: valid data
        :return: pyotp object
        """
        interval = validated_data.pop('time')
        return self._generate_totp(interval, data=validated_data)


class HotpSerializer(mixins.OTPMixin, serializers.Serializer):
    """HOTP serializer

    """
    count = serializers.IntegerField(required=True, help_text="OTP Counter.")

    def create(self, validated_data):
        """

        :param validated_data: valid data
        :return: pyotp object
        """
        count = validated_data.pop('count')
        return self._generate_hotp(count, data=validated_data)


class ProvisionUriSerializer(serializers.Serializer):
    """Serializer for provisioning serializer.

    """
    name = serializers.CharField(required=True, help_text="name of the account")
    issuer_name = serializers.CharField(help_text="name of the OTP issuer")


class TOTPProvisionUriSerializer(TotpSerializer, ProvisionUriSerializer):
    """Serializer for provisioning serializer + TOTP.

    """

    def create(self, validated_data):
        """

        :param validated_data: valid data
        :return: pyotp object
        """
        interval = validated_data.pop('time')
        return self._generate_totp(
            interval, provision_uri=True, data=validated_data)


class HOTPProvisionUriSerializer(HotpSerializer, ProvisionUriSerializer):
    """Serializer for provisioning serializer + HOTP.

    """
    initial_count = serializers.CharField(default=0, help_text="starting counter value, defaults to 0")

    def create(self, validated_data):
        """

        :param validated_data: valid data
        :return: pyotp object
        """
        count = validated_data.pop('count')
        return self._generate_hotp(count, provision_uri=True, data=validated_data)


class VerifyOtpSerilaizer(serializers.Serializer):
    """Serializer used to verify OTP

    """
    otp = serializers.CharField(required=True)

    def verify_otp(self, otp, obj, otp_type):
        """

        :param otp_type:
        :return:
        """
        if otp_type == 'hotp' and obj.count:
            hotp = pyotp.HOTP(obj.secret)
            return hotp.verify(otp, obj.count)
        elif otp_type == 'totp' and obj.interval:
            totp = pyotp.TOTP(obj.secret, interval=obj.interval)
            return totp.verify(otp)
        return False
