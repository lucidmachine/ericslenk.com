#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Dates
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Feeds
AUTHOR_FEED_ATOM = 'feeds/%s.atom.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
FEED_ALL_ATOM = 'feeds/atom.xml'
FEED_ALL_RSS = 'feeds/rss.xml'
FEED_DOMAIN = SITEURL
FEED_MAX_ITEMS = None
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_RSS = 'feeds/%s.rss.xml'

# Links
SOCIAL = (('Github', 'https://github.com/lucidmachine'),
        ('Twitter', 'https://twitter.com/lucidmachinery'),)

# Metadata
AUTHOR = 'Eric Slenk'
DEFAULT_LANG = 'en'
GITHUB_URL = 'https://github.com/lucidmachine'
SITENAME = 'Lucid Machinery'
TIMEZONE = 'America/Detroit'
TWITTER_USERNAME = 'lucidmachinery'

# Pagination
DEFAULT_PAGINATION = 10

# Plugins
PLUGINS = ['sitemap', 'w3c_validate', 'yuicompressor']

# URLs and Paths
ARTICLE_PATHS = ['blog']
PATH = 'content'
#RELATIVE_URLS = True
SITEURL = 'http://www.ericslenk.com'
STATIC_PATHS = ['images']
