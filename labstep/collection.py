#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from .config import API_ROOT
from .entity import Entity, getEntities, newEntity, editEntity, getHeaders
from .helpers import (url_join, handleError, getTime)


def getCollections(user, count=1000,
                   type=None, search_query=None, extraParams={}):
    """
    Retrieve a list of the user's collections.

    Parameters
    ----------
    user (obj)
        The Labstep user.
        Must have property 'api_key'. See 'login'.
    count (int)
        The number of Collections to retrieve.
    type (str)
        Return only collections of a certain type. Options are:
       'experiment', 'protocol'.
    search_query (str)
        Search for Collections with this 'name'.
    extraParams (dict)
        Dictionary of extra filter parameters.

    Returns
    -------
    collections
        A list of collection objects.
    """
    types = {
        'experiment': 'experiment_workflow',
        'protocol': 'protocol_collection',
        None: None
    }
    params = {'search_query': search_query,
              'type': types[type],
              **extraParams}
    return getEntities(user, Collection, count, params)


def getAttachedCollections(entity, count=100):
    """
    Retrieve the Collections attached to a Labstep Entity.

    Parameters
    ----------
    entity (obj)
        The entity to retrieve Collections from.

    Returns
    -------
    collections
        List of the collections attached.
    """
    key = entity.__entityName__.replace('-', '_')+'_id'
    filterParams = {
        key: entity.id,
        'group_id': entity.__user__.activeWorkspace
    }
    return getEntities(entity.__user__, Collection, count=count,
                       filterParams=filterParams)


def newCollection(user, name, type, extraParams={}):
    """
    Create a new Collection.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the Collection.
        Must have property 'api_key'. See 'login'.
    name (str)
        Name of the new Collection.
    type (str)
      Create collections from either protocols or experiments. Options are:
     'experiments', 'protocols'.

    Returns
    -------
    collection
        An object representing the new Labstep Collection.
    """
    types = {
        'experiment': 'experiment_workflow',
        'protocol': 'protocol_collection'
    }
    params = {'name': name,
              'type': types[type],
              **extraParams}
    return newEntity(user, Collection, params)


def addToCollection(entity, collection_id):
    """
    Attach a Labstep Entity to an existing collection.

    Parameters
    ----------
    entity (obj)
        The Labstep entity to collection. Can be
        Experiment or Protocol. Must have 'id'.
    collection_id (obj)
        The id of the collection to add to.

    Returns
    -------
    entity
        An object representing the entity to add to collections.
    """
    entityName = entity.__entityName__

    headers = getHeaders(entity.__user__)
    url = url_join(API_ROOT, "api/generic/",
                   entityName,
                   str(entity.id),
                   Collection.__entityName__,
                   str(collection_id))
    r = requests.put(url, headers=headers)
    handleError(r)
    return json.loads(r.content)


def removeFromCollection(entity, collection_id):
    """
    Remove a Labstep Entity from an existing collection.

    Parameters
    ----------
    entity (obj)
        The Labstep entity to collection. Can be
        Experiment or Protocol. Must have 'id'.
    collection_id (obj)
        The id of the collection to remove from.
    """
    entityName = entity.__entityName__

    headers = getHeaders(entity.__user__)
    url = url_join(API_ROOT, "api/generic/",
                   entityName,
                   str(entity.id),
                   Collection.__entityName__,
                   str(collection_id))
    r = requests.delete(url, headers=headers)
    handleError(r)
    return json.loads(r.content)


def editCollection(collection, name, extraParams={}):
    """
    Edit the name of an existing Collection.

    Parameters
    ----------
    collection (obj)
        The Collection to edit.
    name (str)
        The new name of the Collection.

    Returns
    -------
    collection
        An object representing the edited Collection.
    """
    params = {'name': name, **extraParams}
    return editEntity(collection, params)


class Collection(Entity):
    """
    Represents a Collection on Labstep.

    To see all attributes of a collection run
    ::
        print(my_collection)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(my_collection.name)
        print(my_collection.id)
    """
    __entityName__ = 'folder'
    __hasParentGroup__ = True

    def edit(self, name=None, extraParams={}):
        """
        Edit the name of an existing Collection.

        Parameters
        ----------
        name (str)
            The new name of the Collection.

        Returns
        -------
        :class:`~labstep.collection.Collection`
            An object representing the edited Collection.

        Example
        -------
        ::

            # Get all collections, since there is no function
            # to get one collection.
            collections = user.getCollections()

            # Select the collection by using python index.
            collections[1].edit(name='A New Collection Name')
        """
        return editCollection(self, name, extraParams=extraParams)

    def delete(self):
        """
        Delete an existing collection.

        Parameters
        ----------
        collection (obj)
            The collection to delete.

        Returns
        -------
        collection
            An object representing the collection to delete.
        """
        return self.edit(extraParams={'deleted_at': getTime()})
