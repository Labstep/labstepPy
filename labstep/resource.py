#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .constants import resourceEntityName
from .entity import getEntity, getEntities, newEntity, editEntity
from .helpers import getTime, update
from .comment import addCommentWithFile
from .tag import tag


def getResource(user, resource_id):
    """
    Retrieve a specific Labstep Resource.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    resource_id (int)
        The id of the Resource to retrieve.

    Returns
    -------
    resource
        An object representing a Labstep Resource.
    """
    return getEntity(user, resourceEntityName, id=resource_id)


def getResources(user, count=100, search_query=None, tag_id=None):
    """
    Retrieve a list of a user's Resources on Labstep.

    Parameters
    ----------
    user (obj)
        The Labstep user whose Resources you want to retrieve.
        Must have property 'api_key'. See 'login'.
    count (int)
        The number of Resources to retrieve.
    tag_id (obj/int)
        Retrieve Resources that have a specific tag.

    Returns
    -------
    resources
        A list of Resource objects.
    """
    metadata = {'search_query': search_query,
                'tag_id': tag_id}
    return getEntities(user, resourceEntityName, count, metadata)


def newResource(user, name):
    """
    Create a new Labstep Resource.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the Resource.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your resource a name.

    Returns
    -------
    protocol
        An object representing the new Labstep Resource.
    """
    metadata = {'name': name}
    return newEntity(user, resourceEntityName, metadata)


def editResource(user, resource, name=None, deleted_at=None):
    """
    Edit an existing Resource.

    Parameters
    ----------
    user (obj)
        The labstep user. Must have property 'api_key'. See 'login'.
    resource (obj)
        The Resource to edit.
    name (str)
        The new name of the Experiment.
    deleted_at (obj)
        The timestamp at which the Resource is deleted/archived.

    Returns
    -------
    resource
        An object representing the Resource to edit.
    """
    metadata = {'name': name,
                'deleted_at': deleted_at}
    return editEntity(user, resourceEntityName, resource.id, metadata)


class Resource:
    def __init__(self, data, user):
        self.__user__ = user
        self.__entityName__ = resourceEntityName
        update(self, data)

    # functions()
    def edit(self, name=None):
        return editResource(self.__user__, self, name)

    def delete(self):
        return editResource(self.__user__, self, deleted_at=getTime())

    def comment(self, body, filepath=None):
        return addCommentWithFile(self.__user__, self, body, filepath)

    def addTag(self, name):
        return tag(self.__user__, self, name)
