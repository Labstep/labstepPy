#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .entity import getEntity, getEntities, newEntity, editEntity
from .helpers import (listToClass, getTime, createdAtFrom, createdAtTo, update,
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


class ProtocolStep:
    __entityName__ = 'protocol-step'

    def __init__(self, data, user):
        self.__user__ = user
        update(self, data)


class ProtocolTable:
    __entityName__ = 'protocol-table'

    def __init__(self, data, user):
        self.__user__ = user
        update(self, data)

    def edit(self, name=None, data=None):
        fields = {
            'name': name,
            'data': data
        }
        return editEntity(self, fields)


class ProtocolTimer:
    __entityName__ = 'protocol-timer'

    def __init__(self, data, user):
        self.__user__ = user
        update(self, data)

    def edit(self, name=None, hours=None, minutes=None, seconds=None):
        fields = {
            'name': name,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        }
        return editEntity(self, fields)


class ProtocolMaterial:
    __entityName__ = 'protocol-value'

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
        self.last_version = {}
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
        for example, the Protocol 'name', 'id', etc.:

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

    def getComments(self, count=100):
        """
        Retrieve the Comments attached to this Labstep Entity.

        Returns
        -------
        List[:class:`~labstep.comment.Comment`]
            List of the comments attached.

        Example
        -------
        .. code-block::

            entity = user.getProtocol(17000)
            comments = entity.getComments()
            comments[0].attributes()
        """
        return getComments(self, count)

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
        """
        Retrieve the Tags attached to a this Labstep Entity.

        Returns
        -------
        List[:class:`~labstep.tag.Tag`]
            List of the tags attached.

        Example
        -------
        .. code-block::

            entity = user.getProtocol(17000)
            tags = entity.getTags()
            tags[0].attributes()
        """
        return getAttachedTags(self)

    def getSteps(self):
        """
        Returns a list of the steps in the protocol.

        Returns
        -------
        List[:class:`~labstep.protocol.ProtocolStep`]
            List of the steps in the protocol.

        Example
        -------
        .. code-block::

            entity = user.getProtocol(17000)
            steps = entity.getSteps()
            steps[0].complete()
        """
        steps = self.last_version['protocol_steps']
        return listToClass(steps, ProtocolStep, self.__user__)

    def addMaterial(self, name=None, amount=None, unit=None, resource=None):
        """
        Add a new material to the protocol.

        Parameters
        ----------
        name (str)
            The name of the material to add.
        amount (str)
            The amount required by the protocol.
        units (str)
            The units for the amount.
        resource (:class:`~labstep.resource.Resource`)
            The specific Resource recommended for use with the protocol.

        Returns
        -------
        :class:`~labstep.protocolMaterial.ProtocolMaterial`
            The newly added material entity.

        Example
        -------
        .. code-block::

            entity = user.getProtocol(17000)
            material = entity.addMaterial()
            material.edit(name='Test Material')
        """
        fields = {
            'protocol_id': self.last_version['id'],
            'name': name,
            'value': amount,
            'units': unit,
        }
        return newEntity(self.__user__, ProtocolMaterial, fields)

    def getMaterials(self):
        """
        Returns a list of the materials specified in the protocol.

        Returns
        -------
        List[:class:`~labstep.protocol.ProtocolMaterial`]
            List of the materials in the protocol.

        Example
        -------
        .. code-block::

            entity = user.getProtocol(17000)
            materials = entity.getMaterials()
            materials[0].edit(name='Test Material')
        """
        materials = self.last_version['protocol_values']
        return listToClass(materials, ProtocolMaterial, self.__user__)

    def addTimer(self, name=None, hours=None, minutes=None, seconds=None):
        """
        Add a new timer to the protocol.

        Parameters
        ----------
        name (str)
            The name of the timer.
        hours (int)
            The hours.
        minutes (int)
            The minutes.
        seconds (int)
            The seconds.

        Returns
        -------
        :class:`~labstep.protocolTimer.ProtocolTimer`
            The newly added timer entity.

        Example
        -------
        .. code-block::

            entity = user.getProtocol(17000)
            timer = entity.addTimer()
            timer.edit(name='Test Timer')
        """
        fields = {
            'protocol_id': self.last_version['id'],
            'name': name,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        }
        return newEntity(self.__user__, ProtocolTimer, fields)

    def getTimers(self):
        """
        Returns a list of the timers specified in the protocol.

        Returns
        -------
        List[:class:`~labstep.protocol.ProtocolTimer`]
            List of the timers in the protocol.

        Example
        -------
        .. code-block::

            entity = user.getProtocol(17000)
            timers = entity.getTimers()
            timers[0].edit()
        """
        timers = self.last_version['protocol_timers']
        return listToClass(timers, ProtocolTimer, self.__user__)

    def addTable(self, name=None):
        """
        Add a new timer to the protocol.

        Parameters
        ----------
        name (str)
            The name of the timer.
        data (json)
            The json data of the table.

        Returns
        -------
        :class:`~labstep.protocolTable.ProtocolTable`
            The newly added table entity.

        Example
        -------
        .. code-block::

            entity = user.getProtocol(17000)
            table = entity.addTable()
            table.edit(name='Test Table')
        """
        fields = {
            'protocol_id': self.last_version['id'],
            'name': name,
        }
        return newEntity(self.__user__, ProtocolTimer, fields)

    def getTables(self):
        """
        Returns a list of the tables in the protocol.

        Returns
        -------
        List[:class:`~labstep.protocol.ProtocolTable`]
            List of the talbes in the protocol.

        Example
        -------
        .. code-block::

            entity = user.getProtocol(17000)
            timers = entity.getTimers()
            timers[0].edit()
        """
        tables = self.last_version['protocol_tables']
        return listToClass(tables, ProtocolTable, self.__user__)
