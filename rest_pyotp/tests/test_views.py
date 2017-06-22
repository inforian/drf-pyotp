#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- rest_pyotp.tests.test_views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- This file includes Test cases for Views .

"""

# future
from __future__ import unicode_literals

# 3rd party

# Django
from django.test import TestCase
from django.core.urlresolvers import reverse

# local
from rest_pyotp.models import PyOTP


class PyOTPTestCase(TestCase):
    """Handles PyOTP Views Test Cases

    """

    def setUp(self):
        """

        """
        self.hotp = {
            'count': 1000
        }

        self.totp = {
            "time": 1000
        }

        self.totp_uri = {
            "time": 1000,
            "name": "local.test/.inm",
            "issuer_name": "test"

        }

        self.hotp_uri = {
            "count": 1000,
            "name": "local.test/.inm",
            "issuer_name": "test"

        }

    def _create_otp(self, data):
        """

        :return: otp instance
        """
        return PyOTP.objects.create(**data)

    def _verify_otp(self, otp_type, otp_uuid, otp):
        """

        :param otp_type: otp type
        :param otp_uuid: otp uuid
        :param data: verify post data
        """
        url = reverse('drf-pyotp:verify-otp-w-uuid', args=(otp_type, otp_uuid))
        return self.client.post(url, data={'otp': otp})

    def test_totp_create(self):
        """Test TOTP create & verify

        """
        url = reverse('drf-pyotp:generate-totp')

        create_response = self.client.post(url, data=self.totp)

        if create_response.status_code == 201:
            otp_uuid = create_response.json().get('otp_uuid')
            otp = create_response.json().get('otp')
            verify_response = self._verify_otp('totp', otp_uuid, otp)

            self.assertEqual(verify_response.status_code, 200)

        self.assertEqual(create_response.status_code, 201)

    def test_hotp_create(self):
        """Test HOTP create & verify

        """
        url = reverse('drf-pyotp:generate-hotp')
        create_response = self.client.post(url, data=self.hotp)

        if create_response.status_code == 201:
            otp_uuid = create_response.json().get('otp_uuid')
            otp = create_response.json().get('otp')
            verify_response = self._verify_otp('hotp', otp_uuid, otp)

            self.assertEqual(verify_response.status_code, 200)

        self.assertEqual(create_response.status_code, 201)

    def test_totp_uri_create(self):
        """Test Create TOTP + Provisional URI

        """
        url = reverse('drf-pyotp:generate-totp-provision-uri')

        response = self.client.post(url, data=self.totp_uri)

        self.assertEqual(response.status_code, 201)

    def test_hotp_uri_create(self):
        """Test Create HOTP + Provisional URI

        """
        url = reverse('drf-pyotp:generate-hotp-provision-uri')

        response = self.client.post(url, data=self.hotp_uri)

        self.assertEqual(response.status_code, 201)

    def test_totp_with_unique_identifier(self):
        """Test TOTP create & verify with unique Identifier sent from client

        """
        url = reverse('drf-pyotp:generate-otp')
        data = {
          "unique_identifier": "test-identifier",
          "time": 100
        }
        create_response = self.client.post(url, data=data)

        if create_response.status_code == 201:
            otp = create_response.json().get('otp')
            verify_url = reverse('drf-pyotp:verify-otp-w-unique-identifier-v3')
            verify_response = self.client.post(verify_url, data={'unique_identifier': 'test-identifier', 'otp': otp})

            self.assertEqual(verify_response.status_code, 200)

        self.assertEqual(create_response.status_code, 201)

    def test_wrong_hotp(self):
        """Test Wrong HOTP

        """
        hotp_obj = self._create_otp(self.hotp)

        response = self._verify_otp('hotp', hotp_obj.uuid, hotp_obj.otp)
        self.assertNotEqual(response.status_code, 200)

    def test_wrong_totp(self):
        """Test Wrong TOTP

        """
        totp_obj = self._create_otp({'interval': 1000})

        response = self._verify_otp('totp', totp_obj.uuid, totp_obj.otp)

        self.assertNotEqual(response.status_code, 200, )
