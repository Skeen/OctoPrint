#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
import os

import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "src"))

#-----------------------------------------------------------------------------------------------------------------------

# Requirements for our application
INSTALL_REQUIRES = [
	"flask>=0.9,<0.11",
	"werkzeug==0.8.3",
	"tornado==4.0.1",
	"sockjs-tornado==1.0.1",
	"PyYAML==3.10",
	"Flask-Login==0.2.2",
	"Flask-Principal==0.3.5",
	"Flask-Babel==0.9",
	"Flask-Assets==0.10",
	"pyserial==2.7",
	"netaddr==0.7.17",
	"watchdog==0.8.3",
	"sarge==0.1.4",
	"netifaces==0.10",
	"pylru==1.0.9",
	"rsa==3.2",
	"pkginfo==1.2.1",
	"requests==2.7.0",
	"semantic_version==2.4.2",
	"psutil==3.2.1"
]

# Additional requirements for optional install options
EXTRA_REQUIRES = dict(
	# Dependencies for developing OctoPrint
	develop=[
		# Testing dependencies
		"mock>=1.0.1",
		"nose>=1.3.0",
		"ddt",

		# Documentation dependencies
		"sphinx>=1.3",
		"sphinxcontrib-httpdomain",
		"sphinx_rtd_theme",

		# PyPi upload related
		"pypandoc"
	],

	# Dependencies for developing OctoPrint plugins
	plugins=[
		"cookiecutter"
	]
)

# Additional requirements for setup
SETUP_REQUIRES = []

# Dependency links for any of the aforementioned dependencies
DEPENDENCY_LINKS = []

#-----------------------------------------------------------------------------------------------------------------------
# Anything below here is just command setup and general setup configuration

def params():
	name = "OctoPrint"
	version = "API"

	description = "A snappy web interface for 3D printers"
	install_requires = INSTALL_REQUIRES
	extras_require = EXTRA_REQUIRES
	dependency_links = DEPENDENCY_LINKS
	setup_requires = SETUP_REQUIRES

	classifiers = [
		"Development Status :: 4 - Beta",
		"Environment :: Web Environment",
		"Framework :: Flask",
		"Intended Audience :: Education",
		"Intended Audience :: End Users/Desktop",
		"Intended Audience :: Manufacturing",
		"Intended Audience :: Science/Research",
		"License :: OSI Approved :: GNU Affero General Public License v3",
		"Natural Language :: English",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: JavaScript",
		"Topic :: Internet :: WWW/HTTP",
		"Topic :: Internet :: WWW/HTTP :: Dynamic Content",
		"Topic :: Internet :: WWW/HTTP :: WSGI",
		"Topic :: Printing",
		"Topic :: System :: Networking :: Monitoring"
	]
	author = "Gina Häußge"
	author_email = "osd@foosel.net"
	url = "http://octoprint.org"
	license = "AGPLv3"

	packages = find_packages(where="src")
	package_dir = {
		"": "src"
	}

	include_package_data = True
	zip_safe = False

	if os.environ.get('READTHEDOCS', None) == 'True':
		# we can't tell read the docs to please perform a pip install -e .[develop], so we help
		# it a bit here by explicitly adding the development dependencies, which include our
		# documentation dependencies
		install_requires = install_requires + extras_require['develop']

	entry_points = {
		"console_scripts": [
			"octoprint = octoprint:main"
		]
	}

	return locals()

setup(**params())
