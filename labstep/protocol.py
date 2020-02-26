#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .primaryEntity import PrimaryEntity
from .entity import Entity, getEntity, getEntities, newEntity, editEntity
from .helpers import (listToClass, getTime, createdAtFrom, createdAtTo)


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


def newProtocol(user, name, extraParams={}):
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
    filterParams = {'name': name}
    params = {**filterParams, **extraParams}
    return newEntity(user, Protocol, params)


def editProtocol(protocol, name=None, deleted_at=None, extraParams={}):
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
    filterParams = {'name': name,
                    'deleted_at': deleted_at}
    params = {**filterParams, **extraParams}
    return editEntity(protocol, params)


class ProtocolMaterial(Entity):
    __entityName__ = 'protocol-value'

    def edit(self, name=None, amount=None, units=None, resource=None,
             extraParams={}):
        """
        Edit an existing Protocol Material.

        Parameters
        ----------
        name (str)
            The name of the Protocol Material.
        amount (str)
            The amount of the Protocol Material.
        units (str)
            The units of the amount.
        resource (Resource)
            The :class:`~labstep.resource.Resource` of the Protocol Material.

        Returns
        -------
        :class:`~labstep.protocol.ProtocolMaterial`
            An object representing the edited Protocol Material.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            protocol_materials = exp_protocol.getMaterials()
            protocol_materials[0].edit(value=1.7, units='ml')
        """
        fields = {'name': name,
                  'value': amount,
                  'units': units}

        if resource is not None:
            fields['resource_id'] = resource.id

        return editEntity(self, fields, extraParams=extraParams)


class ProtocolStep(Entity):
    __entityName__ = 'protocol-step'


class ProtocolTable(Entity):
    __entityName__ = 'protocol-table'

    def edit(self, name=None, data=None, extraParams={}):
        """
        Edit an existing Protocol Table.

        Parameters
        ----------
        name (str)
            The name of the Protocol Table.
        data (str)
            The data of the table in json format.

        Returns
        -------
        :class:`~labstep.protocol.ProtocolTable`
            An object representing the edited Protocol Table.

        Example
        -------
        ::

            data = {
                "rowCount": 6,
                "columnCount": 6,
                "colHeaderData": {},
                "data": {
                    "dataTable": {
                        0: {
                            0: {
                                "value": 'Cell A1'
                            },
                            1: {
                                "value": 'Cell B1'
                            }
                        }
                    }
                }
            }

            protocol = user.getProtocol(17000)
            protocol_tables = protocol.getTables()
            protocol_tables[0].edit(name='New Table Name', data=data)
        """

        filterParams = {'name': name,
                        'data': data}
        params = {**filterParams, **extraParams}
        return editEntity(self, params)


class ProtocolTimer(Entity):
    __entityName__ = 'protocol-timer'

    def edit(self, name=None, hours=None, minutes=None, seconds=None,
             extraParams={}):
        """
        Edit an existing Protocol Timer.

        Parameters
        ----------
        name (str)
            The name of the timer.
        hours (int)
            The hours of the timer.
        minutes (int)
            The minutes of the timer.
        seconds (int)
            The seconds of the timer.

        Returns
        -------
        :class:`~labstep.protocol.ProtocolTimer`
            An object representing the edited Protocol Timer.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            protocol_timers = protocol.getTimers()
            protocol_timers[0].edit(name='New Timer Name',
                                    minutes=1, seconds=17)
        """
        filterParams = {'name': name}

        if hours is not None:
            filterParams['hours'] = hours
        if minutes is not None:
            filterParams['minutes'] = minutes
        if seconds is not None:
            filterParams['seconds'] = seconds

        params = {**filterParams, **extraParams}
        return editEntity(self, params)


class Protocol(PrimaryEntity):
    """
    Represents a Protocol on Labstep.

    To see all attributes of a protocol run
    ::
        print(my_protocol)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(my_protocol.name)
        print(my_protocol.id)
    """
    __entityName__ = 'protocol-collection'

    def edit(self, name, extraParams={}):
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
        ::

            my_protocol = user.getProtocol(17000)
            my_protocol.edit(name='A New Protocol Name')
        """
        return editProtocol(self, name, extraParams=extraParams)

    def delete(self):
        """
        Delete an existing Protocol.

        Example
        -------
        ::

            my_protocol = user.getProtocol(17000)
            my_protocol.delete()
        """
        return editProtocol(self, deleted_at=getTime())

    def getSteps(self):
        """
        Returns a list of the steps in a Protocol.

        Returns
        -------
        List[:class:`~labstep.protocol.ProtocolStep`]
            List of the steps in Protocol.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            protocol_steps = protocol.getSteps()
            protocol_steps[0].attributes()
        """
        steps = self.last_version['protocol_steps']
        return listToClass(steps, ProtocolStep, self.__user__)

    def addMaterial(self, name=None, amount=None, units=None, resource=None,
                    extraParams={}):
        """
        Add a new material to the Protocol.

        Parameters
        ----------
        name (str)
            The name of the material to add.
        amount (str)
            The amount required by the protocol.
        units (str)
            The units for the amount.
        resource (Resource)
            The specific :class:`~labstep.resource.Resource` recommended for
            use with the protocol.

        Returns
        -------
        :class:`~labstep.protocol.ProtocolMaterial`
            The newly added material entity.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            resource = user.getResources(search_query='Sample A')[0]
            protocol.addMaterial(name='Sample A', amount='2', units='ml',
                                 resource=resource)
        """
        filterParams = {'protocol_id': self.last_version['id'],
                        'name': name,
                        'value': amount,
                        'units': units}

        if resource is not None:
            filterParams['resource_id'] = resource.id

        params = {**filterParams, **extraParams}
        return newEntity(self.__user__, ProtocolMaterial, params)

    def getMaterials(self):
        """
        Returns a list of the materials in a Protocol.

        Returns
        -------
        List[:class:`~labstep.protocol.ProtocolMaterial`]
            List of the materials in a Protocol.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            protocol_materials = protocol.getMaterials()
            protocol_materials[0].attributes()
        """
        materials = self.last_version['protocol_values']
        return listToClass(materials, ProtocolMaterial, self.__user__)

    def addTimer(self, name=None, hours=None, minutes=None, seconds=None):
        """
        Add a new timer to the Protocol.

        Parameters
        ----------
        name (str)
            The name of the timer.
        hours (int)
            The hours of the timer.
        minutes (int)
            The minutes of the timer.
        seconds (int)
            The seconds of the timer.

        Returns
        -------
        :class:`~labstep.protocol.ProtocolTimer`
            The newly added timer entity.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            protocol.addTimer(name='Refluxing', hours='4', minutes='30')
        """
        fields = {'protocol_id': self.last_version['id'],
                  'name': name,
                  'hours': hours,
                  'minutes': minutes,
                  'seconds': seconds
                  }
        return newEntity(self.__user__, ProtocolTimer, fields)

    def getTimers(self):
        """
        Returns a list of the timers in a Protocol.

        Returns
        -------
        List[:class:`~labstep.protocol.ProtocolTimer`]
            List of the timers in a Protocol.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            protocol_timers = protocol.getTimers()
            protocol_timers[0].attributes()
        """
        timers = self.last_version['protocol_timers']
        return listToClass(timers, ProtocolTimer, self.__user__)

    def addTable(self, name=None, data=None):
        """
        Add a new table to the Protocol.

        Parameters
        ----------
        name (str)
            The name of the table.
        data (json)
            The data of the table in json format.

        Returns
        -------
        :class:`~labstep.protocol.ProtocolTable`
            The newly added table entity.

        Example
        -------
        ::

            data = {
                "rowCount": 12,
                "columnCount": 12,
                "colHeaderData": {},
                "data": {
                    "dataTable": {
                        0: {
                            0: {
                                "value": 'Cell A1'
                            },
                            1: {
                                "value": 'Cell B1'
                            }
                        }
                    }
                }
            }

            protocol = user.getProtocol(17000)
            protocol.addTable(name='Calibration', data=data)
        """

        fields = {'protocol_id': self.last_version['id'],
                  'name': name,
                  'data': data,
                  }
        return newEntity(self.__user__, ProtocolTable, fields)

    def getTables(self):
        """
        Returns a list of the tables in a Protocol.

        Returns
        -------
        List[:class:`~labstep.protocol.ProtocolTable`]
            List of the tables in a Protocol.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            protocol_tables = protocol.getTables()
            protocol_tables[0].attributes()
        """
        tables = self.last_version['protocol_tables']
        return listToClass(tables, ProtocolTable, self.__user__)
