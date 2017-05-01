#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- app.views
~~~~~~~~~~~

- This file contains API's for pyotp
"""

# future
from __future__ import unicode_literals

# 3rd party
import pyotp

# rest-framework
from rest_framework import viewsets, status
from rest_framework.response import Response

# Django
from django.conf import settings

# local

# own app
from app import serializers, models


class PyotpViewset(viewsets.GenericViewSet):
    """Pyotp Viewset, every pyotp http request handles by this class

    """
    queryset = models.PyOTP.objects.all()
    lookup_field = 'uuid'
    otp_type = None

    def _get_serializer_from_otp_type(self):
        """Select

        :return:
        """

    def get_serializer_class(self):
        """Here we will decide which serializer will be used.

        :return: serializer class
        """
        otp_type = self.kwargs.get('otp_type')
        if settings.PROVISION_URI is True:
            if otp_type == 'hotp':
                return serializers.HOTPProvisionUriSerializer
            elif otp_type == 'totp':
                return serializers.TOTPProvisionUriSerializer
        else:
            if otp_type == 'hotp':
                return serializers.HotpSerializer
            elif otp_type == 'totp':
                return serializers.TotpSerializer

    def generate_otp(self, request, otp_type):
        """

        :param request: Django request
        :param otp_type: otp_type  [hotp/totp]
        :return: otp uuid
        """
        self.otp_type = otp_type
        serializer =self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = serializer.save()

        return Response(response, status=status.HTTP_200_OK)

    def verify_otp(self, request, otp_type, uuid):
        """

        :param request: Django request
        :param otp_type: otp_type  [hotp/totp]
        :param uuid: OTP instance UUID
        :return: 200_ok OR 400_bad_request
        """
        obj = self.get_object()

        serializer = serializers.VerifyOtpSerilaizer(data=request.data)
        serializer.is_valid(raise_exception=True)

        valid_otp = serializer.verify_otp(serializer.data.get('otp'), obj, otp_type)
        if not valid_otp:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)




