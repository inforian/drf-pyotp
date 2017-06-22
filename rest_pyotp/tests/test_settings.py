#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- rest_pyotp.tests.test_settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- This file includes test-cases of settings which are required for PyOTP micro-service

"""

# future
from __future__ import unicode_literals

# Django
from django.conf import settings
from django.test import TestCase


class SettingsTestCase(TestCase):
    """Settings Test Case

    """

    def setUp(self):
        """

        """
        self.env_settings = ('SECRET_KEY', )

    def test_environment_variables(self):
        """makes sure settings which are necessary for running Member micro-service are defined in settings.

        """

        for env_setting in self.env_settings:
            if not getattr(settings, env_setting,):
                self.assertFalse('{0} environment settings is not defined.'.format(env_setting))

        self.assertTrue('Environment settings test passed.')


