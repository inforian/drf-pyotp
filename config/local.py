"""Development settings and globals."""

from __future__ import absolute_import


from os.path import join
from os.path import normpath
from os import environ



# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(key):
    """
    Get the environment setting or return exception,
    if default is not set

    :param key:
    """
    try:
        return environ[key]
    except KeyError:
        error_msg = 'Set the {0} env variable'.format(key)
        raise ImproperlyConfigured(error_msg)

# ######### DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
########## END DEBUG CONFIGURATION

########## SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See: https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    '*'
]
########## END SITE CONFIGURATION
