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
from rest_pyotp import views


UUID_REGEX = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
OTP_TYPE_REGEX = '(hotp|totp)'

verify_otp = views.PyotpViewset.as_view({
    'post': 'verify_otp',
})

generate_hotp = views.PyotpViewset.as_view({
    'post': 'generate_hotp',
})

generate_totp = views.PyotpViewset.as_view({
    'post': 'generate_totp',
})

generate_hotp_provision_uri = views.PyotpViewset.as_view({
    'post': 'generate_hotp_provision_uri',
})

generate_totp_provision_uri = views.PyotpViewset.as_view({
    'post': 'generate_totp_provision_uri',
})

urlpatterns = [
    url(r'^generate-otp/hotp/$',
        generate_hotp,
        name='generate-hotp'),
    url(r'^generate-otp/totp/$',
        generate_totp,
        name='generate-totp'),
    url(r'^generate-otp/hotp/provision-uri/$',
        generate_hotp_provision_uri,
        name='generate-totp-provision-uri'),
    url(r'^generate-otp/totp/provision-uri/$',
        generate_totp_provision_uri,
        name='generate-totp-provision-uri'),
    url(r'^verify-otp/(?P<otp_type>(hotp|totp))/(?P<uuid>{uuid})/$'.format(otp_type=OTP_TYPE_REGEX, uuid=UUID_REGEX),
        verify_otp,
        name='verify-otp'),
]
