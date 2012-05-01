# -*- coding: utf-8 -*-

import os

from flask import Flask
app = Flask(__name__)

from flask import Flask, render_template, request, redirect, url_for


from flask_debugtoolbar import DebugToolbarExtension
from flask_heroku import Heroku
from flask_sslify import SSLify
from raven.contrib.flask import Sentry
from flask.ext.celery import Celery

app = Flask(__name__)
app.secret_key = os.environ.get('APP_SECRET', 'some-secret-key')
app.debug = 'DEBUG' in os.environ
# app.debug = False

# Use gevent workers for celery.
app.config['CELERYD_POOL'] = 'gevent'
app.config['DEBUG_TB_ENABLED'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# Bootstrap Heroku environment variables.
heroku = Heroku(app)

# Redirect urls to https
sslify = SSLify(app)

# Setup error collection
sentry = Sentry(app)

# Task queue
celery = Celery(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


