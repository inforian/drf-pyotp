#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- rest_pyotp.admin
~~~~~~~~~~~~~~

- This file contains admin models of pyotp app
"""

# future
from __future__ import unicode_literals

# 3rd party

# Django
from django.contrib import admin

# local

# own app
from rest_pyotp import models


class PyOTPAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('id', 'uuid', 'secret', 'count', 'interval', 'otp', 'created_at',)
    list_display_links = ('uuid',)
    search_fields = ('uuid', 'secret', 'otp', )
    list_per_page = 20
    ordering = ('-id',)

admin.site.register(models.PyOTP, PyOTPAdmin)


