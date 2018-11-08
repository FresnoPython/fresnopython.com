#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Fresno Python User Group'
SITENAME = 'fresno.py'
SITEURL = 'http://localhost:8000'

SITESUBTITLE = SITEDESCRIPTION = AUTHOR

PATH = 'content'
STATIC_PATHS = ['static']

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['assets']

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
MENUITEMS = LINKS = (
    ('Meetings', 'https://meetup.com/FresnoPython'),
    ('What is Python?', '/pages/python.html'),
    ('Resources', '/pages/resources.html'),
    ('Code of Conduct', '/pages/code-of-conduct.html'),
)

# Social links
SOCIAL = (
    ('meetup', 'https://meetup.com/FresnoPython'),
    ('twitter', 'https://twitter.com/FresnoPython'),
    ('facebook', 'https://www.facebook.com/groups/fresno.py'),
    ('github', 'https://github.com/FresnoPython'),
    ('slack', 'http://slack.rootaccess.space'),
)

DEFAULT_PAGINATION = 10

THEME = 'Flex'

SITELOGO = '/static/img/fresnopy-logo-dark.png'

BROWSER_COLOR = '#3A6687'

CUSTOM_CSS = 'static/css/custom.css'

FAVICON = '/static/img/favicon.ico'

DISPLAY_PAGES_ON_MENU = False
MAIN_MENU = False

COPYRIGHT_YEAR = 2018
