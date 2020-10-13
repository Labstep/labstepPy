#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from .config import API_ROOT
from .helpers import listToClass, update, url_join, handleError, getHeaders
import inspect
import pprint


def getLegacyEntity(user, entityClass, id):
    """
    *** LEGACY ***
    Parameters
    ----------
    user (obj)
        The Labstep user.
    entityClass (class)
        The Class of entity to retrieve.
    id (int)
        The id of the entity.

    Returns
    -------
    entity
        An object representing a Labstep Entity.
    """
    headers = getHeaders(user)
    url = url_join(API_ROOT, "/api/generic/",
                   entityClass.__entityName__, str(id))
    r = requests.get(url, headers=headers)
    handleError(r)
    return entityClass(json.loads(r.content), user)


def getEntity(user, entityClass, id, isDeleted='both'):
    """
    Parameters
    ----------
    user (obj)
        The Labstep user.
    entityClass (class)
        The Class of entity to retrieve.
    id (int)
        The id of the entity.
    isDeleted (str)
        Retrieve an entity that has been soft deleted.

    Returns
    -------
    entity
        An object representing a Labstep Entity.
    """
    if hasattr(entityClass, '__isLegacy__'):
        return getLegacyEntity(user, entityClass, id)
    else:
        params = {'is_deleted': isDeleted,
                  'get_single': 1,
                  'id': id
                  }
        headers = getHeaders(user)
        url = url_join(API_ROOT, "/api/generic/",
                       entityClass.__entityName__)
        r = requests.get(url, headers=headers, params=params)
        handleError(r)
        return entityClass(json.loads(r.content), user)


def getEntities(user, entityClass, count, filterParams={}):
    """
    Parameters
    ----------
    user (obj)
        The Labstep user.
    entityClass (class)
        The Class of the entity to retrieve.
    count (int)
        The amount to retrieve.
    filterParams (dict)
        The filterParams of the entity.

    Returns
    -------
    entity
        A list of Entity objects.
    """
    n = min(count, 50)
    search_params = {'search': 1,
                     'cursor': -1,
                     'count': n}

    params = {**search_params, **filterParams}

    headers = getHeaders(user)
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
    return listToClass(items, entityClass, user)


def newEntity(user, entityClass, fields):
    """
    Parameters
    ----------
    user (obj)
        The Labstep user.
    entityClass (class)
        The Class of the entity to retrieve.
    fields (dict)
        The fields to set on the new entity.

    Returns
    -------
    entity
        An object representing the new Labstep Entity.
    """
    headers = getHeaders(user)
    url = url_join(API_ROOT, "/api/generic/", entityClass.__entityName__)
    fields = dict(
        filter(lambda field: field[1] is not None, fields.items()))

    if 'group_id' not in fields and getattr(entityClass,
                                            '__hasParentGroup__', False):
        fields['group_id'] = user.activeWorkspace

    r = requests.post(url, headers=headers, json=fields)
    handleError(r)
    return entityClass(json.loads(r.content), user)


def newEntities(user, entityClass, items):
    """
    Parameters
    ----------
    user (obj)
        The Labstep user.
    entityClass (class)
        The Class of the entity to retrieve.
    items (List[])
        List of info on entities to create.

    Returns
    -------
    entities
        List of Labstep Entities created.
    """
    headers = getHeaders(user)
    url = url_join(API_ROOT,
                   "/api/generic/",
                   entityClass.__entityName__,
                   'batch')
    r = requests.post(url, headers=headers, json={"items": items})
    handleError(r)
    entities = json.loads(r.content)
    return list(map(lambda entity: entityClass(entity, user), entities))


def editEntity(entity, fields):
    """
    Parameters
    ----------
    entity (obj)
        The entity to edit.
    fields (dict)
        The fields being edited.

    Returns
    -------
    entity
        An object representing the edited Entity.
    """
    # Filter the 'fields' dictionary by removing {'fields': None}
    # to preserve the existing data in the 'fields', otherwise
    # the 'fields' will be overwritten to 'None'.
    new_fields = dict(
        filter(lambda field: field[1] is not None, fields.items()))
    headers = getHeaders(entity.__user__)
    url = url_join(API_ROOT, '/api/generic/',
                   entity.__entityName__, str(entity.id))
    r = requests.put(url, json=new_fields, headers=headers)
    handleError(r)
    return entity.__init__(json.loads(r.content), entity.__user__)


class Entity:
    def __init__(self, data, user):
        self.__user__ = user
        update(self, data)

    def __repr__(self):
        all_attributes = inspect.getmembers(
            self, lambda a: not(inspect.isroutine(a)))
        entity_attributes = {k: v for k,
                             v in all_attributes if not (k.startswith('__'))}
        pp = pprint.PrettyPrinter(indent=1)
        return pp.pformat(entity_attributes)

    def update(self):
        """
        Fetches the most up-to-date version of the entity from Labstep.
        """
        data = getEntity(self.__user__, type(self), self.id).__data__
        self.__init__(data, self.__user__)
        return self
