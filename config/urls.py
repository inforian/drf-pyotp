#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Veris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_swagger.views import get_swagger_view


API_TITLE = 'Rest PyOTP APIs'

urlpatterns = [
    url(r'^pyotp-swagger/$', get_swagger_view(title=API_TITLE)),

    url(r'^admin/', admin.site.urls),

    # pyotp routers
    url(r'', include('rest_pyotp.routers', namespace='drf-pyotp')),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
