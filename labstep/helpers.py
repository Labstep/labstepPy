#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from time import gmtime, strftime


####################        helperFunctions()
def url_join(*args):
    """
    Join a set of args with a slash (/) between them. Instead of
    checking for the presence of a slash, the slashes from both sides
    of each arg will be .strip() and then args .join() together.
    """
    return "/".join(arg.strip("/") for arg in args)

def handleError(r):
    """
    If the status code of the request (r) is not 200,
    return the error code and error message.
    """
    if r.status_code != 200:
        raise Exception('Request Error {code}:{message}'.format(code=r.status_code,message=r.content))
    return

def getTime():
    """
    Get the datetime at .now() in json serializable format.
    """
    timezone = strftime('%z', gmtime())
    tz_hour = timezone[:3]
    tz_minute = timezone[3:]
    timestamp = datetime.now().strftime("%Y-%m-%d" + "T" + "%H:%M:%S" +
                                        "{}:{}".format(tz_hour,tz_minute))
    return timestamp

def createdAtFrom(created_at_from):
    """
    Get the datetime of 'created_at_from' in json serializable format.
    """
    if created_at_from == None:
        return None
    else:
        timezone = getTime()[-6:]
        created_at_from = created_at_from + "T00:00:00{tz}".format(tz=timezone)
        return created_at_from

def createdAtTo(created_at_to):
    """
    Get the datetime of 'created_at_to' in json serializable format.
    """
    if created_at_to == None:
        return None
    else:
        timezone = getTime()[-6:]
        created_at_to = created_at_to + "T00:00:00{tz}".format(tz=timezone)
        return created_at_to
