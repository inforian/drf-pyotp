#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- pyotp.routers
~~~~~~~~~~~~~~

- This file contains pyotp routers
"""

# future
from __future__ import unicode_literals

# 3rd party


# Django
from django.conf.urls import url

# local

# own app
from app import views

UUID_REGEX = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
OTP_TYPE_REGEX = '(hotp|totp)'

verify_otp = views.PyotpViewset.as_view({
    'post': 'verify_otp',
})

generate_otp = views.PyotpViewset.as_view({
    'post': 'generate_otp',
})

urlpatterns = [
    url(r'^generate-otp/(?P<otp_type>{otp_type})/$'.format(otp_type=OTP_TYPE_REGEX),
        generate_otp,
        name='generate-otp'),
    url(r'^verify-otp/(?P<otp_type>{otp_type})/(?P<uuid>{uuid})/$'.format(otp_type=OTP_TYPE_REGEX, uuid=UUID_REGEX),
        verify_otp,
        name='verify-otp'),
]
