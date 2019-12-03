#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .entity import getEntity, getEntities, newEntity, editEntity
from .helpers import (getTime, createdAtFrom, createdAtTo, update,
                      showAttributes)
from .comment import addCommentWithFile, getComments
from .tag import tag, getAttachedTags


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
                 created_at_from=None, created_at_to=None, tag_id=None,
                 extraParams={}):
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
        The id of the Tag to filter by.
    extraParams (dict)
        Dictionary of extra filter parameters.

    Returns
    -------
    protocols
        A list of Protocol objects.
    """
    filterParams = {'search_query': search_query,
                    'created_at_from': createdAtFrom(created_at_from),
                    'created_at_to': createdAtTo(created_at_to),
                    'tag_id': tag_id}
    params = {**filterParams, **extraParams}
    return getEntities(user, Protocol, count, params)


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
    fields = {'name': name}
    return newEntity(user, Protocol, fields)


def editProtocol(protocol, name=None, deleted_at=None):
    """
    Edit an existing Protocol.

    Parameters
    ----------
    protocol (obj)
        The Protocol to edit.
    name (str)
        The new name of the Protocol.
    deleted_at (str)
        The timestamp at which the Protocol is deleted/archived.

    Returns
    -------
    protocol
        An object representing the edited Protocol.
    """
    fields = {'name': name,
              'deleted_at': deleted_at}
    return editEntity(protocol, fields)


class ProtocolMaterial:
    __entityName__ = 'protocol_value'

    def __init__(self, data, user):
        self.__user__ = user
        update(self, data)

    def edit(self, label=None, value=None, unit=None, resource=None):
        fields = {'label': label,
                  'value': value,
                  'unit': unit}
        if resource is not None:
            fields['resource_id'] = resource.id

        return editEntity(self, fields)


class Protocol:
    __entityName__ = 'protocol-collection'

    def __init__(self, fields, user):
        self.__user__ = user
        update(self, fields)

    # functions()
    def attributes(self):
        """
        Show all attributes of a Protocol.

        Example
        -------
        .. code-block::

            my_protocol = user.getProtocol(17000)
            my_protocol.attributes()

        The output should look something like this:

        .. program-output:: python ../labstep/attributes/protocol_attributes.py

        To inspect specific attributes of a protocol,
        for example, the protocol 'name', 'id', etc.:

        .. code-block::

            print(my_protocol.name)
            print(my_protocol.id)
        """
        return showAttributes(self)

    def edit(self, name):
        """
        Edit an existing Protocol.

        Parameters
        ----------
        name (str)
            The new name of the Protocol.

        Returns
        -------
        :class:`~labstep.protocol.Protocol`
            An object representing the edited Protocol.

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
        Add a comment and/or file to a Labstep Protocol.

        Parameters
        ----------
        body (str)
            The body of the comment.
        filepath (str)
            A Labstep File entity to attach to the comment,
            including the filepath.

        Returns
        -------
        :class:`~labstep.comment.Comment`
            The comment added.

        Example
        -------
        .. code-block::

            my_protocol = user.getProtocol(17000)
            my_protocol.addComment(body='I am commenting!',
                                   filepath='pwd/file_to_upload.dat')
        """
        return addCommentWithFile(self, body, filepath)
    
    def getComments(self,count=100):
        """
        Gets the comments attached to this entity.

        Returns
        -------
        List[:class:`~labstep.comment.Comment`]
            List of the comments attached.

        Example
        -------
        .. code-block::

            entity = user.getResource(17000)
            comments = entity.getComments()
            print(comments[0].body)
        """
        return getComments(self,count)

    def addTag(self, name):
        """
        Add a tag to the Protocol (creates a
        new tag if none exists).

        Parameters
        ----------
        name (str)
            The name of the tag to create.

        Returns
        -------
        :class:`~labstep.protocol.Protocol`
            The Protocol that was tagged.

        Example
        -------
        .. code-block::

            my_protocol = user.getProtocol(17000)
            my_protocol.addTag(name='My Tag')
        """
        tag(self, name)
        return self

    def getTags(self):
        return getAttachedTags(self)
        