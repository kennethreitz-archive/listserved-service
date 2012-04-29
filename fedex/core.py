# -*- coding: utf-8 -*-

import os

from flask import Flask
app = Flask(__name__)

from flask import Flask, render_template, request, redirect, url_for


from flask_debugtoolbar import DebugToolbarExtension
from flask_heroku import Heroku
from raven.contrib.flask import Sentry
from flask.ext.celery import Celery

app = Flask(__name__)
app.secret_key = os.environ.get('APP_SECRET', 'some-secret-key')

# Use gevent workers for celery.
app.config['CELERYD_POOL'] = 'gevent'

app.config['DEBUG_TB_ENABLED'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


# Bootstrap Heroku environment variables.
heroku = Heroku(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


# if not any((settings.DEBUG, request.is_secure(), request.META.get('HTTP_X_FORWARDED_PROTO', '') == 'https')):
#             url = request.build_absolute_uri(request.get_full_path())
#             secure_url = url.replace('http://', 'https://')
#             return HttpResponseRedirect(secure_url)

import sys
class SSLifyMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):

        print environ

        sys.stdout.flush()
        # if not
        # is_secure
        # if 'METHOD_OVERRIDE' in environ.get('QUERY_STRING', ''):
        #     args = url_decode(environ['QUERY_STRING'])
        #     method = args.get('__METHOD_OVERRIDE__')
        #     if method:
        #         method = method.encode('ascii', 'replace')
        #         environ['REQUEST_METHOD'] = method
        return self.app(environ, start_response)


app = SSLifyMiddleware(app)