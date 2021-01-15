#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.collection.repository import collectionRepository


def getCollections(user, count=1000, type=None, search_query=None, extraParams={}):
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
    return collectionRepository.getCollections(
        user, count, type, search_query, extraParams
    )


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
    return collectionRepository.getAttachedCollections(entity, count)


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
    return collectionRepository.newCollection(user, name, type, extraParams)


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
    return collectionRepository.addToCollection(entity, collection_id)


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
    return collectionRepository.removeFromCollection(entity, collection_id)


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
    return collectionRepository.editCollection(collection, name, extraParams)
