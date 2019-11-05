#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from .config import API_ROOT
from .helpers import url_join, handleError


def getEntity(user, entityName, id):
    """
    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    entityName (str)
        Options for the entity name are:
        experimentEntityName, resourceEntityName,
        protocolEntityName, tagEntityName
    id (int)
        The id of the entity.

    Returns
    -------
    entity
        An object representing a Labstep Entity.
    """
    params = {'is_deleted': 'both'}
    headers = {'apikey': user.api_key}
    url = url_join(API_ROOT, "/api/generic/", entityName, str(id))
    r = requests.get(url, headers=headers, params=params)
    handleError(r)
    return json.loads(r.content)


def getEntities(user, entityName, count, metadata=None):
    """
    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    entityName (str)
        Options for entity name are: experimentEntityName,
        resourceEntityName, protocolEntityName, tagEntityName,
        workspaceEntityName
    count (int)
        The number of Tags to retrieve.
    metadata
        The metadata of the entity.

    Returns
    -------
    entity
        A list of Entity objects.
    """
    n = min(count, 1000)
    search_params = {'search': 1,
                     'cursor': -1,
                     'count': n}
    params = {**search_params, **metadata}

    headers = {'apikey': user.api_key}
    url = url_join(API_ROOT, "/api/generic/", entityName)
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
    return items


def newEntity(user, entityName, metadata):
    """
    Parameters
    ----------
    user (str)
        The Labstep user.
    entityName (str)
        Currents options for entity name are: experimentEntityName,
        resourceEntityName, protocolEntityName, tagEntityName,
        workspaceEntityName.
    metadata (dict)
        The metadata of the entity.

    Returns
    -------
    entity
        An object representing the new Labstep Entity.
    """
    headers = {'apikey': user.api_key}
    url = url_join(API_ROOT, "/api/generic/", entityName)
    r = requests.post(url, headers=headers, json=metadata)
    handleError(r)
    return json.loads(r.content)


def editEntity(user, entityName, id, metadata):
    """
    Parameters
    ----------
    user (obj)
        The Labstep user.
    entityName (str)
        Currents options for entity name are: experimentEntityName,
        resourceEntityName, protocolEntityName, tagEntityName,
        workspaceEntityName, commentEntityName
    id (int)
        The id of the entity.
    metadata (dict)
        The metadata being editted.

    Returns
    -------
    entity
        An object representing the editted Entity.
    """
    # Filter the 'metadata' dictionary by removing {'fields': None}
    # to preserve the existing data in the 'fields', otherwise
    # the 'fields' will be overwritten to 'None'.
    new_metadata = dict(
        filter(lambda field: field[1] is not None, metadata.items()))
    headers = {'apikey': user.api_key}
    url = url_join(API_ROOT, '/api/generic/', entityName, str(id))
    r = requests.put(url, json=new_metadata, headers=headers)
    handleError(r)
    return json.loads(r.content)
