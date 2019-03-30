#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Metadata
AUTHOR = 'Eric Slenk'
DEFAULT_LANG = 'en'
GITHUB_URL = 'https://github.com/lucidmachine'
SITELOGO = "https://avatars1.githubusercontent.com/u/213561"
SITETITLE = "Lucid Machinery"
SITESUBTITLE = "A Blog by Eric Slenk"
SITENAME = SITETITLE
SITEDESCRIPTION = SITESUBTITLE
TIMEZONE = 'America/Detroit'
TWITTER_USERNAME = 'lucidmachinery'


# Dates
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Email
EMAIL = 'slenk.eric@gmail.com'
EMAIL_LINK = ''.join(('mailto:', EMAIL))
OBFUSCATED_EMAIL = ''.join(['&#{0:s};'.format(str(ord(char))) for char in EMAIL_LINK])

# Google
GOOGLE_ANALYTICS = "UA-101906012-1"
GOOGLE_TAG_MANAGER = "GTM-NW29DZR"


# Pagination
DEFAULT_PAGINATION = 10

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap']

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Theme
THEME = 'themes/Flex'

# URLs and Paths
ARTICLE_PATHS = ['blog']
PATH = 'content'
RELATIVE_URLS = True
SITEURL = 'https://www.ericslenk.com'
STATIC_PATHS = ['images', '.htaccess']

# Feeds
AUTHOR_FEED_ATOM = 'feeds/{slug}.atom.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'
FEED_ALL_ATOM = 'feeds/atom.xml'
FEED_ALL_RSS = 'feeds/rss.xml'
FEED_DOMAIN = SITEURL
FEED_MAX_ITEMS = None
TAG_FEED_ATOM = 'feeds/{slug}.atom.xml'
TAG_FEED_RSS = 'feeds/{slug}.rss.xml'

# Links
SOCIAL = (
    ('envelope-open', OBFUSCATED_EMAIL),
    ('twitter', 'https://twitter.com/lucidmachinery'),
    ('github', 'https://github.com/lucidmachine'),
    ('rss', FEED_ALL_RSS),
)
