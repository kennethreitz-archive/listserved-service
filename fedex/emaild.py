# -*- coding: utf-8 -*-

from inbox import Inbox

inbox = Inbox()

@inbox.collate
def handle(to, sender, body):
    pass
