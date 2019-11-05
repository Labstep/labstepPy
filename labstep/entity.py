#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from .config import API_ROOT
from .helpers import update, url_join, handleError


def getEntity(user, entityClass, id):
    """
    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    entityClass (class)

    id (obj)
        The id of the entity.

    Returns
    -------
    returns?
        ?.
    """
    params = {'is_deleted': 'both'}
    headers = {'apikey': user.api_key}
    url = url_join(API_ROOT, "/api/generic/",
                   entityClass.__entityName__, str(id))
    r = requests.get(url, headers=headers, params=params)
    handleError(r)
    return entityClass(json.loads(r.content), user)


def getEntities(user, entityClass, count, metadata=None):
    """
    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    entityClass (class)
        The Class of entity to get
    count
        ??
    metadata
        ??

    Returns
    -------
    returns?
        ?.
    """
    n = min(count, 1000)
    search_params = {'search': 1,
                     'cursor': -1,
                     'count': n}
    params = {**search_params, **metadata}

    headers = {'apikey': user.api_key}
    url = url_join(API_ROOT, "/api/generic/", entityClass.__entityName__)
    r = requests.get(url, params=params, headers=headers)
    handleError(r)
    resp = json.loads(r.content)
    items = resp['items']
    expected_results = min(resp['total'], count)
    while len(items) < expected_results:
        params['cursor'] = resp['next_cursor']
        r = requests.get(url, headers=headers, params=params)
        resp = json.loads(r.content)
        items.extend(resp['items'])
    return list(map(lambda x: entityClass(x, user), items))


def newEntity(user, entityClass, data):
    """
    Parameters
    ----------
    user (User)
        The Labstep user.
    entityClass (Class)
        Currents options for entity name are: experimentEntityName,
        resourceEntityName, protocolEntityName, tagEntityName,
        workspaceEntityName.
    data
        The name of the entity.

    Returns
    -------
    returns?
        ?.
    """
    headers = {'apikey': user.api_key}
    url = url_join(API_ROOT, "/api/generic/", entityClass.__entityName__)
    r = requests.post(url, headers=headers, json=data)
    handleError(r)
    return entityClass(json.loads(r.content), user)


def editEntity(entity, metadata):
    """
    Parameters
    ----------
    user (User)
        The Labstep user.
    entityClass (Class)
        Currents options for entity name are: experimentEntityName,
        resourceEntityName, protocolEntityName, tagEntityName,
        workspaceEntityName, commentEntityName
    id
        The id of the entity.
    metadata (dict)
        The metadata being editted.

    Returns
    -------
    returns?
        ?.
    """
    # Filter the 'metadata' dictionary by removing {'fields': None}
    # to preserve the existing data in the 'fields', otherwise
    # the 'fields' will be overwritten to 'None'.
    new_metadata = dict(
        filter(lambda field: field[1] is not None, metadata.items()))
    headers = {'apikey': entity.__user__.api_key}
    url = url_join(API_ROOT, '/api/generic/',
                   entity.__entityName__, str(entity.id))
    r = requests.put(url, json=new_metadata, headers=headers)
    handleError(r)
    return update(entity, json.loads(r.content))
