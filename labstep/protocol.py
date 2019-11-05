#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
    return getEntity(user, Protocol, id=protocol_id)


def getProtocols(user, count=100, search_query=None,
                 created_at_from=None, created_at_to=None, tag_id=None):
    """
    Retrieve a list of a user's Protocols on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    count (int)
        The number of Protocols to retrieve.
    search_query (str)
        Search for Protocols with this 'name'.
    created_at_from (str)
        The start date of the search range, must be
        in the format of 'YYYY-MM-DD'.
    created_at_to (str)
        The end date of the search range, must be
        in the format of 'YYYY-MM-DD'.
    tag_id (int)
        The id of the Tag to retrieve.

    Returns
    -------
    protocols
        A list of Protocol objects.
    """
    metadata = {'search_query': search_query,
                'created_at_from': createdAtFrom(created_at_from),
                'created_at_to': createdAtTo(created_at_to),
                'tag_id': tag_id}
    return getEntities(user, Protocol, count, metadata)


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
    return newEntity(user, Protocol, metadata)


def editProtocol(protocol, name=None, deleted_at=None):
    """
    Edit an existing Protocol.

    Parameters
    ----------
    user (obj)
        The labstep user. Must have property 'api_key'. See 'login'.
    protocol (obj)
        The Protocol to edit.
    name (str)
        The new name of the Protocol.
    deleted_at (str)
        The timestamp at which the Protocol is deleted/archived.

    Returns
    -------
    protocol
        An object representing the Protocol to edit.
    """
    metadata = {'name': name,
                'deleted_at': deleted_at}
    return editEntity(protocol, metadata)


class Protocol:
    __entityName__ = 'protocol-collection'

    def __init__(self, data, user):
        self.__user__ = user
        update(self, data)

    # functions()
    def edit(self, name=None):
        """
        Edit an existing Protocol.

        Parameters
        ----------
        name (str)
            The new name of the Protocol.

        Example
        -------
        .. code-block::

            my_protocol = user.getProtocol(17000)
            my_protocol.edit(name='A New Protocol Name')
        """
        return editProtocol(self, name)

    def delete(self):
        """
        Delete an existing Protocol.

        Example
        -------
        .. code-block::

            my_protocol = user.getProtocol(17000)
            my_protocol.delete()
        """
        return editProtocol(self, deleted_at=getTime())

    def addComment(self, body, filepath=None):
        """
        Add a comment to a Labstep Protocol.

        Parameters
        ----------
        body (str)
            The body of the comment.
        filepath (str)
            A Labstep File entity to attach to the comment,
            including the filepath.

        Example
        -------
        .. code-block::

            my_protocol = user.getProtocol(17000)
            my_protocol.addComment(body='I am commenting!',
                                filepath='pwd/file_to_upload.dat')
        """
        return addCommentWithFile(self, body, filepath)

    def addTag(self, name):
        """
        Add a tag to the Protocol (creates a
        new tag if none exists).

        Parameters
        ----------
        name (str)
            The name of the tag to create.

        Example
        -------
        .. code-block::

            my_protocol = user.getProtocol(17000)
            my_protocol.addTag(name='My Tag')
        """
        tag(self, name)
        return self
