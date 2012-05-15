"""Copyright 2008 Orbitz WorldWide

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License."""
# Django settings for graphite project.
# DO NOT MODIFY THIS FILE DIRECTLY - use local_settings.py instead

# Import all defaults from Django so we will never break imports in
# local_settings
from django.conf.global_settings import *

import os
import sys
from django import VERSION as DJANGO_VERSION

try:
  import rrdtool
except ImportError:
  rrdtool = False

WEBAPP_VERSION = '0.9.10-pre1'
DEBUG = False
JAVASCRIPT_DEBUG = False

# Filesystem layout
WEB_DIR = os.path.dirname(os.path.abspath(__file__))
WEBAPP_DIR = os.path.dirname(WEB_DIR)
GRAPHITE_ROOT = os.path.dirname(WEBAPP_DIR)
THIRDPARTY_DIR = os.path.join(WEB_DIR, 'thirdparty')
# Initialize additional path variables
# Defaults for these are set after local_settings is imported
CONTENT_DIR = ''
CSS_DIR = ''
CONF_DIR = ''
DASHBOARD_CONF = ''
GRAPHTEMPLATES_CONF = ''
STORAGE_DIR = ''
WHITELIST_FILE = ''
INDEX_FILE = ''
LOG_DIR = ''
WHISPER_DIR = ''
RRD_DIR = ''
DATA_DIRS = []

CLUSTER_SERVERS = []

sys.path.insert(0, WEBAPP_DIR)
# Allow local versions of the libs shipped in thirdparty to take precedence
sys.path.append(THIRDPARTY_DIR)

# Memcache settings
MEMCACHE_HOSTS = []
DEFAULT_CACHE_DURATION = 60 #metric data and graphs are cached for one minute by default
LOG_CACHE_PERFORMANCE = False

# Remote store settings
REMOTE_STORE_FETCH_TIMEOUT = 6
REMOTE_STORE_FIND_TIMEOUT = 2.5
REMOTE_STORE_RETRY_DELAY = 60
REMOTE_FIND_CACHE_DURATION = 300

#Remote rendering settings
REMOTE_RENDERING = False #if True, rendering is delegated to RENDERING_HOSTS
RENDERING_HOSTS = []
REMOTE_RENDER_CONNECT_TIMEOUT = 1.0
LOG_RENDERING_PERFORMANCE = False

#Miscellaneous settings
CARBONLINK_HOSTS = ["127.0.0.1:7002"]
CARBONLINK_TIMEOUT = 1.0
SMTP_SERVER = "localhost"
DOCUMENTATION_URL = "http://graphite.readthedocs.org/"
ALLOW_ANONYMOUS_CLI = True
LOG_METRIC_ACCESS = False
LEGEND_MAX_ITEMS = 10

#Authentication settings
USE_LDAP_AUTH = False
LDAP_SERVER = "" # "ldapserver.mydomain.com"
LDAP_PORT = 389
LDAP_SEARCH_BASE = "" # "OU=users,DC=mydomain,DC=com"
LDAP_BASE_USER = "" # "CN=some_readonly_account,DC=mydomain,DC=com"
LDAP_BASE_PASS = "" # "my_password"
LDAP_USER_QUERY = "" # "(username=%s)"  For Active Directory use "(sAMAccountName=%s)"
LDAP_URI = None

#Set this to True to delegate authentication to the web server
USE_REMOTE_USER_AUTHENTICATION = False

# Override to link a different URL for login (e.g. for django_openid_auth)
LOGIN_URL = '/account/login'

#Additional authentication backends to prepend
ADDITIONAL_AUTHENTICATION_BACKENDS = []

#Initialize database settings - Old style (pre 1.2)
DATABASE_ENGINE = 'django.db.backends.sqlite3'	# 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = ''				# Or path to database file if using sqlite3.
DATABASE_USER = ''				# Not used with sqlite3.
DATABASE_PASSWORD = ''				# Not used with sqlite3.
DATABASE_HOST = ''				# Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''				# Set to empty string for default. Not used with sqlite3.

ADMINS = ()
MANAGERS = ADMINS

TEMPLATE_DIRS = (
  os.path.join(WEB_DIR, 'templates'),
)

# If using rrdcached, set to the address or socket of the daemon
FLUSHRRDCACHED = ''

#Django settings below, do not touch!
APPEND_SLASH = False
TEMPLATE_DEBUG = DEBUG
CACHE_BACKEND = "dummy:///"

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# Absolute path to the directory that holds media.

MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
#XXX Compatibility for Django 1.1. To be removed after 0.9.10
if DJANGO_VERSION < (1,2):
  TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
  )
else:
  TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
  )

MIDDLEWARE_CLASSES = (
  'django.middleware.common.CommonMiddleware',
  'django.middleware.gzip.GZipMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'graphite.urls'

INSTALLED_APPS = (
  'graphite.metrics',
  'graphite.render',
  'graphite.cli',
  'graphite.browser',
  'graphite.composer',
  'graphite.account',
  'graphite.dashboard',
  'graphite.whitelist',
  'graphite.events',
  'django.contrib.auth',
  'django.contrib.sessions',
  'django.contrib.admin',
  'django.contrib.contenttypes',
  'tagging',
)

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']

