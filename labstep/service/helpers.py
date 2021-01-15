#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from datetime import datetime
from time import gmtime, strftime
from labstep.constants.version import VERSION


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


def handleError(response, *args, **kwargs):
    """
    Returns
    -------
        The error code and error message if the
        status code of the request is not 200.
    """
    if response.status_code != 200:
        print(
            """Get the latest version of the SDK by running:
        pip install labstep --upgrade"""
        )
        raise Exception(
            "Request Error {code}:{message}".format(
                code=response.status_code, message=response.content
            )
        )
    return


def getTime():
    """
    Returns
    -------
    timestamp
        The datetime at .now() in json serializable format.
    """
    timezone = strftime("%z", gmtime())
    tz_hour = timezone[:3]
    tz_minute = timezone[3:]
    timestamp = datetime.now().strftime(
        "%Y-%m-%d" + "T" + "%H:%M:%S" + "{}:{}".format(tz_hour, tz_minute)
    )
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
        datetime = datetime.replace(" ", "T") + ":00" + timezone
        return datetime


def handleString(string):
    """
    Returns
    -------
    string
        The string in lowercase, and any whitespace replaced with '_'.
    """
    if string is None:
        return None
    else:
        return string.lower().replace(" ", "_")


def update(entity, newData):
    """
    Returns
    -------
    the updated entity
    """
    entity.__data__ = newData
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


def getHeaders(user):
    return {"apikey": user.api_key, "User-Agent": f"Python SDK {VERSION}"}
