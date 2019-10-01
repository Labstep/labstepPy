#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from time import gmtime, strftime


####################        helperFunctions()
def url_join(*args):
    '''
    Join a set of args with a slash (/) between them. Instead of
    checking for the presence of a slash, the slashes from both sides
    of each arg will be .strip() and then args .join() together.
    '''
    return "/".join(arg.strip("/") for arg in args)

def handleError(r):
    if r.status_code != 200:
        raise Exception('Request Error {code}:{message}'.format(code=r.status_code,message=r.content))
    return

def getTime():
    timezone = strftime('%z', gmtime())
    tz_hour = timezone[:3]
    tz_minute = timezone[3:]
    timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S{}:{}'.format(tz_hour,tz_minute))
    return timestamp

def createdAtFrom(created_at_from):
    if created_at_from == None:
        return None
    else:
        timezone = getTime()[-6:]
        created_at_from = created_at_from + "T00:00:00{}".format(timezone)
        return created_at_from

def createdAtTo(created_at_to):
    if created_at_to == None:
        return None
    else:
        timezone = getTime()[-6:]
        created_at_to = created_at_to + "T00:00:00{}".format(timezone)
        return created_at_to
