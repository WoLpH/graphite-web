# Django settings for graphite project.
# DO NOT MODIFY THIS FILE DIRECTLY - use local_settings.py instead
from __future__ import absolute_import
import os

# Get defaults from default_settings
from default_settings import *

# Pull in overrides from local_settings.py
try:
    from local_settings import *
except ImportError:
    print >> sys.stderr, ('Could not import graphite.local_settings, '
        'using defaults!')

# Set config dependent on flags set in local_settings
# Path configuration
if not CONTENT_DIR:
    CONTENT_DIR = os.path.join(WEBAPP_DIR, 'content')

if not CSS_DIR:
    CSS_DIR = os.path.join(CONTENT_DIR, 'css')

if not CONF_DIR:
    CONF_DIR = os.environ.get(
        'GRAPHITE_CONF_DIR',
        os.path.join(GRAPHITE_ROOT, 'conf'),
    )

if not DASHBOARD_CONF:
    DASHBOARD_CONF = os.path.join(CONF_DIR, 'dashboard.conf')

if not GRAPHTEMPLATES_CONF:
    GRAPHTEMPLATES_CONF = os.path.join(CONF_DIR, 'graphTemplates.conf')

if not STORAGE_DIR:
    STORAGE_DIR = os.environ.get(
        'GRAPHITE_STORAGE_DIR',
        os.path.join(GRAPHITE_ROOT, 'storage'),
    )

if not WHITELIST_FILE:
    WHITELIST_FILE = os.path.join(STORAGE_DIR, 'lists', 'whitelist')

if not INDEX_FILE:
    INDEX_FILE = os.path.join(STORAGE_DIR, 'index')

if not LOG_DIR:
    LOG_DIR = os.path.join(STORAGE_DIR, 'log', 'webapp')

if not WHISPER_DIR:
    WHISPER_DIR = os.path.join(STORAGE_DIR, 'whisper/')

if not RRD_DIR:
    RRD_DIR = os.path.join(STORAGE_DIR, 'rrd/')

if not DATA_DIRS:
    if rrdtool and os.path.exists(RRD_DIR):
        DATA_DIRS = [WHISPER_DIR, RRD_DIR]
    else:
        DATA_DIRS = [WHISPER_DIR]
# Default sqlite db file
# This is set here so that a user-set STORAGE_DIR is available

if 'sqlite3' in DATABASE_ENGINE \
        and not DATABASE_NAME:
    DATABASE_NAME = os.path.join(STORAGE_DIR, 'graphite.db')
# Caching shortcuts

if MEMCACHE_HOSTS:
    CACHE_BACKEND = 'memcached://%s/?timeout=%d' % (
        ';'.join(MEMCACHE_HOSTS),
        DEFAULT_CACHE_DURATION,
    )
# Authentication shortcuts

if USE_LDAP_AUTH and LDAP_URI is None:
    LDAP_URI = 'ldap://%s:%d/' % (LDAP_SERVER, LDAP_PORT)

if USE_REMOTE_USER_AUTHENTICATION:
    MIDDLEWARE_CLASSES += (
        'django.contrib.auth.middleware.RemoteUserMiddleware',)
    AUTHENTICATION_BACKENDS.insert(0,
        'django.contrib.auth.backends.RemoteUserBackend')

if USE_LDAP_AUTH:
    AUTHENTICATION_BACKENDS.insert(0,
        'graphite.account.ldapBackend.LDAPBackend')

