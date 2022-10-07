from distutils.core import setup
from setuptools import find_packages

setup(
  name='drf-pyotp',
  packages=find_packages(exclude=['example']),
  version='0.6.0',
  description='Rest extension of PyOTP python library, Here OTP generation and Verification is done via DRF APIs.',
  author='Neeraj Dhiman',
  author_email='ndhiman08@gmail.com',
  license='GPL',
  url='https://github.com/inforian/drf-pyotp',
  download_url='https://github.com/inforian/drf-pyotp/archive/v0.5.5.tar.gz',
  keywords=['otp', 'pyotp', 'totp', 'hotp', 'drf-pyotp'],
  classifiers=[],
  install_requires=[
    'Django>=2.2.28',
    'djangorestframework>=3.11.2',
    'pyotp>=2.2.4',
  ]
)
