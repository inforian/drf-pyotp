"""
WSGI config for veris project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, re, sys
from django.core.wsgi import get_wsgi_application


def read_env():
    """reads local default  environment variables from a env_file located in the project root
    directory.
    """
    try:
        with open('env_file') as f:
            content = f.read()
    except IOError:
        content = ''

    for line in content.splitlines():
        m1 = re.match(r'\A([A-Za-z_0-9]+)=(.*)\Z', line)
        if m1:
            key, val = m1.group(1), m1.group(2)
            m2 = re.match(r"\A'(.*)'\Z", val)
            if m2:
                val = m2.group(1)
            m3 = re.match(r'\A"(.*)"\Z', val)
            if m3:
                val = re.sub(r'\\(.)', r'\1', m3.group(1))

            os.environ.setdefault(key, val)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.local")

read_env()
application = get_wsgi_application()
