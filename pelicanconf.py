#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Metadata
AUTHOR = 'Eric Slenk'
SITENAME = 'Lucid Machinery'
TIMEZONE = 'America/Detroit'
DEFAULT_LANG = 'en'
GITHUB_URL = 'https://github.com/lucidmachine'
TWITTER_USERNAME = 'lucidmachinery'

# URLs and Paths
SITEURL = ''
PATH = 'content'
STATIC_PATHS = ['images']
ARTICLE_PATHS = ['blog']
#RELATIVE_URLS = True

# Feeds
FEED_DOMAIN = ''
FEED_MAX_ITEMS = None
FEED_ALL_ATOM = 'feeds/atom.xml'
FEED_ALL_RSS = 'feeds/rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
AUTHOR_FEED_ATOM = 'feeds/%s.atom.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_RSS = 'feeds/%s.rss.xml'

# Links
SOCIAL = (('Github', 'https://github.com/lucidmachine'),
        ('Twitter', 'https://twitter.com/lucidmachinery'),)

# Pagination
DEFAULT_PAGINATION = 10
