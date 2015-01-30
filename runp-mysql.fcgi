#!/usr/bin/env python

# use mysql
os.environ['DATABASE_URL'] = 'mysql://apps:apps@localhost/apps'

from flug.server.fcgi import WSGIServer
from app import app

if __name__ = '__main__':

    WSGIServer(app).run()