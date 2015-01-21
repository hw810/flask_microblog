# -*- coding: utf-8 -*-

__author__ = 'huaidong'

WTF_CSRF_ENABLED = True  # cross-site request forgery
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/account/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')  # path of db file
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')  # folder for migrate files


# mail server setting
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
# MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
# MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_USERNAME = 'mrhd.test@gmail.com'
MAIL_PASSWORD = 'senior00dgq'


# administrator list
ADMINS = ['mrhd.test@gmail.com']

# pagination
POSTS_PER_PAGE = 3

# whoosh
WHOOSE_BASE = os.path.join(basedir, 'search.db')

MAX_SEARCH_RESULTS = 50


# available languages
LANGUAGES = {
    'en': 'English',
    'zh_Hans': '简体中文',
    'zh_CN': '中文大陆'
}

# MS Translator
MS_TRANSLATOR_CLIENT_ID = 'mrhd_microblog'
MS_TRANSLATOR_CLIENT_SECRET = '5xwnnvasqPLDVB5POOrFq3y4nAKHJSA2Q3/2/95qPIY='


