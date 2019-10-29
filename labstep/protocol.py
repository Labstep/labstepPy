#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .constants import protocolEntityName
from .entity import getEntity, getEntities, newEntity, editEntity
from .helpers import getTime, createdAtFrom, createdAtTo, update
from .comment import addCommentWithFile
from .tag import tag


def getProtocol(user, protocol_id):
    """
    Retrieve a specific Labstep Protocol.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    protocol_id (int)
        The id of the Protocol to retrieve.

    Returns
    -------
    protocol
        An object representing a Labstep Protocol.
    """
    return getEntity(user, protocolEntityName, id=protocol_id)


def getProtocols(user, count=100, search_query=None,
                 created_at_from=None, created_at_to=None, tag_id=None):
    """
    Retrieve a list of a user's Protocols on Labstep.

    Parameters
    ----------
    user (obj)
        The Labstep user whose Protocols you want to retrieve.
        Must have property 'api_key'. See 'login'.
    count (int)
        The number of Protocols to retrieve.

    Returns
    -------
    protocols
        A list of Protocol objects.
    """
    metadata = {'search_query': search_query,
                'created_at_from': createdAtFrom(created_at_from),
                'created_at_to': createdAtTo(created_at_to),
                'tag_id': tag_id}
    return getEntities(user, protocolEntityName, count, metadata)


def newProtocol(user, name):
    """
    Create a new Labstep Protocol.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the Protocol.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your Protocol a name.

    Returns
    -------
    protocol
        An object representing the new Labstep Protocol.
    """
    metadata = {'name': name}
    return newEntity(user, protocolEntityName, metadata)


def editProtocol(user, protocol, name=None, deleted_at=None):
    """
    Edit an existing Protocol.

    Parameters
    ----------
    user (obj)
        The labstep user. Must have property 'api_key'. See 'login'.
    protocol (obj)
        The Protocol to edit.
    name (str)
        The new name of the Experiment.
    deleted_at (obj)
        The timestamp at which the Protocol is deleted/archived.

    Returns
    -------
    protocol
        An object representing the Protocol to edit.
    """
    metadata = {'name': name,
                'deleted_at': deleted_at}
    return editEntity(user, protocolEntityName, protocol.id, metadata)


class Protocol:
    def __init__(self, data, user):
        self.__user__ = user
        self.__entityName__ = protocolEntityName

        update(self, data)

    # functions()
    def edit(self, name=None):
        return editProtocol(self.__user__, self, name)

    def delete(self):
        return editProtocol(self.__user__, self, deleted_at=getTime())

    def comment(self, body, filepath=None):
        return addCommentWithFile(self.__user__, self, body, filepath)

    def addTag(self, name):
        return tag(self.__user__, self, name)
