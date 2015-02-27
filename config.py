# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' + os.path.join(basedir, 'app.db') +
                               '?check_same_thread=False')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_RECORD_QUERIES = True
WHOOSH_BASE = os.path.join(basedir, 'search.db')

# Whoosh does not work on Heroku
WHOOSH_ENABLED = os.environ.get('HEROKU') is None

# slow database query threshold (in seconds)
DATABASE_QUERY_TIMEOUT = 0.5

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' },
    { 'name': 'STEAM', 'url': 'http://steamcommunity.com/openid'},
    ]

# mail server settings
MAIL_SERVER = 'smtp.126.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# administrator list
ADMINS = ['zhangzhennan01@126.com']

# pagination
POSTS_PER_PAGE = 3

MAX_SEARCH_RESULTS = 50

STEAM_API_KEY = '090B8FBA169177A04FFB10777A0C2F41'

# microsoft translation service
MS_TRANSLATOR_CLIENT_ID = 'microblog_77' # enter your MS translator app id here
MS_TRANSLATOR_CLIENT_SECRET = '7AqZLHs3y/dspi2mWWN2Mmwd2qHZTXqTG2Rjtb0wbmY=' # enter your MS translator app secret here

# available languages
LANGUAGES = {
			'en': 'English',
			'zh': '√Ê ∏'
			}
