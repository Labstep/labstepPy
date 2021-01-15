#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.repository import entityRepository


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
    return entityRepository.getLegacyEntity(user, entityClass, id)


def getEntity(user, entityClass, id, isDeleted="both"):
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
    return entityRepository.getEntity(user, entityClass, id, isDeleted)


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
    return entityRepository.getEntities(user, entityClass, count, filterParams)


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
    return entityRepository.newEntity(user, entityClass, fields)


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
    return entityRepository.newEntities(user, entityClass, items)


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
    return entityRepository.editEntity(entity, fields)
