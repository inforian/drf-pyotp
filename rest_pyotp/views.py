#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- rest_pyotp.views
~~~~~~~~~~~

- This file contains API's for rest_pyotp
"""

# future
from __future__ import unicode_literals

# 3rd party

# rest-framework
from rest_framework import viewsets, status
from rest_framework.response import Response

# Django

# local

# own app
from rest_pyotp import serializers, models


class PyotpViewset(viewsets.GenericViewSet):
    """Pyotp Viewset, every pyotp http request handles by this class

    """
    queryset = models.PyOTP.objects.all()
    lookup_field = 'uuid'
    otp_type = None

    def get_serializer_class(self):
        if self.action == 'generate_hotp':
            return serializers.HotpSerializer
        elif self.action == 'generate_totp':
            return serializers.TotpSerializer
        elif self.action == 'generate_hotp_provision_uri':
            return serializers.HOTPProvisionUriSerializer
        elif self.action == 'generate_totp_provision_uri':
            return serializers.TOTPProvisionUriSerializer
        elif self.action == 'verify_otp':
            return serializers.VerifyOtpSerilaizer
        return serializers.NoneSerializer

    def _validate(self, serializer, data):
        """
        :param serializer: serializer against which data to ve validated
        :param data: data to ve validated
        :return: serializer instance.
        """

        serializer_instance = serializer(data=data)
        serializer_instance.is_valid(raise_exception=True)
        return serializer_instance.save()

    def generate_hotp(self, request):
        """
        """
        serializer = self.get_serializer_class()
        serializer = self._validate(serializer, request.data)

        return Response(serializer, status=status.HTTP_201_CREATED)

    def generate_totp(self, request):
        """
        """
        serializer = self.get_serializer_class()
        serializer = self._validate(serializer, request.data)
        return Response(serializer, status=status.HTTP_201_CREATED)

    def generate_hotp_provision_uri(self, request):
        """
        """
        serializer = self.get_serializer_class()
        serializer = self._validate(serializer, request.data)

        return Response(serializer, status=status.HTTP_201_CREATED)

    def generate_totp_provision_uri(self, request):
        """
        """
        serializer = self.get_serializer_class()
        serializer = self._validate(serializer, request.data)
        
        return Response(serializer, status=status.HTTP_201_CREATED)

    def verify_otp(self, request, otp_type, uuid):
        """

        :param request: Django request
        :param otp_type: otp_type  [hotp/totp]
        :param uuid: OTP instance UUID
        :return: 200_ok OR 400_bad_request
        """
        obj = self.get_object()
        serializer = self.get_serializer_class()

        serializer = serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        valid_otp = serializer.verify_otp(serializer.data.get('otp'), obj, otp_type)
        if not valid_otp:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)




