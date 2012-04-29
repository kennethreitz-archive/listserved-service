#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flaskext.script import Manager
from flask.ext.celery import install_commands as install_celery

from fedex import app
# from springcreek.core import db


manager = Manager(app)
install_celery(manager)

# @manager.command
# def syncdb():
#     """Initializes the database."""
#     db.create_all()


if __name__ == "__main__":
    manager.run()