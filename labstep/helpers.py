#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from time import gmtime, strftime
import inspect
import pprint


def url_join(*args):
    """
    Join a set of args with a slash (/) between them. Instead of
    checking for the presence of a slash, the slashes from both sides
    of each arg will be .strip() and then args .join() together.

    Returns
    -------
        returns "/".join(arg.strip("/") for arg in args)

    """
    return "/".join(arg.strip("/") for arg in args)


def handleError(r):
    """
    Returns
    -------
        The error code and error message if the
        status code of the request is not 200.
    """
    if r.status_code != 200:
        raise Exception('Request Error {code}:{message}'.format(
            code=r.status_code, message=r.content))
    return


def getTime():
    """
    Returns
    -------
    timestamp
        The datetime at .now() in json serializable format.
    """
    timezone = strftime('%z', gmtime())
    tz_hour = timezone[:3]
    tz_minute = timezone[3:]
    timestamp = datetime.now().strftime("%Y-%m-%d" + "T" + "%H:%M:%S" +
                                        "{}:{}".format(tz_hour, tz_minute))
    return timestamp


def createdAtFrom(created_at_from):
    """
    Returns
    -------
        The datetime for 'created_at_from' in json serializable format.
    """
    if created_at_from is None:
        return None
    else:
        timezone = getTime()[-6:]
        created_at_from = created_at_from + "T00:00:00" + timezone
        return created_at_from


def createdAtTo(created_at_to):
    """
    Returns
    -------
        The datetime for 'created_at_to' in json serializable format.
    """
    if created_at_to is None:
        return None
    else:
        timezone = getTime()[-6:]
        created_at_to = created_at_to + "T23:59:59" + timezone
        return created_at_to


def handleDate(datetime):
    """
    Returns
    -------
        The datetime in json serializable format.
    """
    if datetime is None:
        return None
    else:
        timezone = getTime()[-6:]
        datetime = datetime.replace(' ', 'T') + ":00" + timezone
        return datetime


def handleStatus(status):
    """
    Returns
    -------
    status
        The status of the Resource in lowercase.
    """
    if status is None:
        return None
    else:
        return status.lower().replace(' ', '_')


def update(entity, newData):
    """
    Returns
    -------
    entity
        for key in newData:
            setattr(entity, key, newData[key])
        return entity
    """
    for key in newData:
        setattr(entity, key, newData[key])
    return entity


def listToClass(items, entityClass, user):
    """
    Returns
    -------
    return list(map(lambda x: entityClass(x, user), items))
    """
    return list(map(lambda x: entityClass(x, user), items))


def showAttributes(entity):
    """
    Returns
    -------
    Return all members of an object as {key: value} pairs, but only
    return keys that do not start with '__'.
    """
    all_attributes = inspect.getmembers(
        entity, lambda a: not(inspect.isroutine(a)))
    entity_attributes = {k: v for k,
                         v in all_attributes if not (k.startswith('__'))}
    pp = pprint.PrettyPrinter(indent=1)
    return pp.pprint(entity_attributes)
