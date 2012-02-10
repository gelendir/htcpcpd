# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='htcpcpd',
      version=version,
      description="HTCPCP Server",
      long_description="""\
An HTTP Server that implements the HTCPCP Protocol""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Frédérik Paradis, Gregory Eric Sanderson',
      author_email='gzou2000@gmail.com, fredy_14@live.fr',
      url='http://gelendir.github.com/htcpcpd',
      license='GPL v3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'python-daemon>=1.5.5',
          'pyserial',
      ],
      entry_points={
          'console_scripts': [
              'htcpcpd = htcpcpd.main:main',
          ]
        }
      )
