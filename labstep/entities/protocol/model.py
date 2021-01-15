#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.metadata.model import Metadata
from labstep.generic.primaryEntity.model import PrimaryEntity
from labstep.entities.protocolMaterial.model import ProtocolMaterial
from labstep.entities.protocolStep.model import ProtocolStep
from labstep.entities.protocolTable.model import ProtocolTable
from labstep.entities.protocolTimer.model import ProtocolTimer
from labstep.entities.protocolVersion.model import ProtocolVersion
from labstep.entities.protocolMaterial.repository import protocolMaterialRepository
from labstep.service.helpers import (
    listToClass,
    getTime,
    handleDate,
)


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

    __entityName__ = "protocol-collection"

    def edit(self, name=None, body=None, extraParams={}):
        """
        Edit an existing Protocol.

        Parameters
        ----------
        name (str)
            The name of the Protocol.
        body (dict):
            JSON representing the the protocol document.

        Returns
        -------
        :class:`~labstep.entities.protocol.model.Protocol`
            An object representing the edited Protocol.

        Example
        -------
        ::

            my_protocol = user.getProtocol(17000)
            my_protocol.edit(name='A New Protocol Name')
        """
        from labstep.entities.protocol.repository import protocolRepository

        return protocolRepository.editProtocol(
            self, name=name, body=body, extraParams=extraParams
        )

    def delete(self):
        """
        Delete an existing Protocol.

        Example
        -------
        ::

            my_protocol = user.getProtocol(17000)
            my_protocol.delete()
        """
        from labstep.entities.protocol.repository import protocolRepository

        return protocolRepository.editProtocol(self, deleted_at=getTime())

    def newVersion(self):
        """
        Start a new version of the Protocol.

        Example
        -------
        ::

            my_protocol = user.getProtocol(17000)
            new_version = my_protocol.newVersion()
        """
        from labstep.generic.entity.repository import entityRepository

        entityRepository.newEntity(
            self.__user__, ProtocolVersion, {"collection_id": self.id}
        )
        return self.update()

    def getBody(self):
        """
        Returns the body of the protocol as a JSON document

        Example
        -------
        ::

            my_protocol = user.newProtocol('My API Protocol')

            my_protocol.edit(body={
                "type": "doc",
                "content": [
                    {
                        "type": "paragraph",
                        "attrs": {"align": None},
                        "content": [
                            {
                                "type": "text",
                                "text": "This is the the body of my protocol"
                            }
                        ]
                    },
                    {
                        "type": "paragraph",
                        "attrs": {"align": None}
                    }
                ]
            })

            my_protocol.getBody()
        """
        self.update()
        if "state" not in self.last_version:
            return None
        return self.last_version["state"]

    def addSteps(self, N):
        """
        Add steps to the protocol

        Parameters
        ----------
        N (int)
            The number of steps to add.

        Example
        -------
        ::

            my_protocol = user.newProtocol('My API Protocol')
            my_protocol.addSteps(5)
        """
        from labstep.generic.entity.repository import entityRepository

        steps = [{"protocol_id": self.last_version["id"]}] * N
        return entityRepository.newEntities(self.__user__, ProtocolStep, steps)

    def getSteps(self):
        """
        Returns a list of the steps in a Protocol.

        Returns
        -------
        List[:class:`~labstep.entities.protocolStep.model.ProtocolStep`]
            List of the steps in Protocol.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            protocol_steps = protocol.getSteps()
            protocol_steps[0].attributes()
        """
        self.update()
        if "protocol_steps" not in self.last_version:
            return []
        steps = self.last_version["protocol_steps"]
        return listToClass(steps, ProtocolStep, self.__user__)

    def getDataElements(self):
        """
        Retrieve the Data Elements of a Protocol.

        Returns
        -------
        :class:`~labstep.entities.metadata.model.Metadata`
            An array of objects representing the Labstep Data Elements
            on a Protocol.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            metadata = exp_protocol.getDataElements()
        """
        self.update()
        if "metadatas" not in self.last_version["metadata_thread"]:
            return []

        return listToClass(
            self.last_version["metadata_thread"]["metadatas"], Metadata, self.__user__
        )

    def addDataElement(
        self,
        fieldName,
        fieldType="default",
        value=None,
        date=None,
        number=None,
        unit=None,
        extraParams={},
    ):
        """
        Add a Data Element to a Protocol.

        Parameters
        ----------
        fieldName (str)
            The name of the field.
        fieldType (str)
            The field type. Options are: "default", "date",
            "quantity", or "number". The "default" type is "Text".
        value (str)
            The value accompanying the fieldName entry.
        date (str)
            The date and time accompanying the fieldName entry. Must be
            in the format of "YYYY-MM-DD HH:MM".
        number (float)
            The quantity.
        unit (str)
            The unit accompanying the number entry.

        Returns
        -------
        :class:`~labstep.entities.metadata.model.Metadata`
            An object representing the new Labstep Data Element.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            dataElement = protocol.addDataElement("Refractive Index",
                                               value="1.73")
        """
        from labstep.generic.entity.repository import entityRepository

        metadataThread = self.last_version["metadata_thread"]
        params = {
            "metadata_thread_id": metadataThread["id"],
            "type": fieldType,
            "label": fieldName,
            "value": value,
            "date": handleDate(date),
            "number": number,
            "unit": unit,
            **extraParams,
        }
        return entityRepository.newEntity(self.__user__, Metadata, params)

    def addMaterial(
        self, name=None, amount=None, units=None, resource_id=None, extraParams={}
    ):
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
        resource_id (int)
            The id of the :class:`~labstep.entities.resource.model.Resource` recommended for
            use with the protocol.

        Returns
        -------
        :class:`~labstep.entities.protocolMaterial.model.ProtocolMaterial`
            The newly added material entity.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            resource = user.getResources(search_query='Sample A')[0]
            protocol.addMaterial(name='Sample A', amount='2', units='ml',
                                 resource_id=resource.id)
        """
        from labstep.generic.entity.repository import entityRepository

        params = {
            "protocol_id": self.last_version["id"],
            "resource_id": resource_id,
            "name": name,
            "value": amount,
            "units": units,
            **extraParams,
        }

        if params["value"] is not None:
            params["value"] = str(params["value"])

        return entityRepository.newEntity(self.__user__, ProtocolMaterial, params)

    def getMaterials(self, count=100, extraParams={}):
        """
        Returns a list of the materials in a Protocol.

        Returns
        -------
        List[:class:`~labstep.entities.protocolMaterial.model.ProtocolMaterial`]
            List of the materials in a Protocol.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            protocol_materials = protocol.getMaterials()
            protocol_materials[0].attributes()
        """
        return protocolMaterialRepository.getProtocolMaterials(self.__user__,
                                                               protocol_id=self.last_version['id'],
                                                               count=count,
                                                               extraParams=extraParams)

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
        :class:`~labstep.entities.protocolTimer.model.ProtocolTimer`
            The newly added timer entity.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            protocol.addTimer(name='Refluxing', hours='4', minutes='30')
        """
        from labstep.generic.entity.repository import entityRepository

        params = {
            "protocol_id": self.last_version["id"],
            "name": name,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
        }
        return entityRepository.newEntity(self.__user__, ProtocolTimer, params)

    def getTimers(self):
        """
        Returns a list of the timers in a Protocol.

        Returns
        -------
        List[:class:`~labstep.entities.protocolTimer.model.ProtocolTimer`]
            List of the timers in a Protocol.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            protocol_timers = protocol.getTimers()
            protocol_timers[0].attributes()
        """
        self.update()
        if "protocol_timers" not in self.last_version:
            return []

        timers = self.last_version["protocol_timers"]
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
        :class:`~labstep.entities.protocolTable.model.ProtocolTable`
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
        from labstep.generic.entity.repository import entityRepository

        params = {
            "protocol_id": self.last_version["id"], "name": name, "data": data}
        return entityRepository.newEntity(self.__user__, ProtocolTable, params)

    def getTables(self):
        """
        Returns a list of the tables in a Protocol.

        Returns
        -------
        List[:class:`~labstep.entities.protocolTable.model.ProtocolTable`]
            List of the tables in a Protocol.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            protocol_tables = protocol.getTables()
            protocol_tables[0].attributes()
        """
        self.update()
        if "protocol_tables" not in self.last_version:
            return []

        tables = self.last_version["protocol_tables"]
        return listToClass(tables, ProtocolTable, self.__user__)

    def addToCollection(self, collection_id):
        """
        Add the protocol to a collection.

        Parameters
        ----------
        collection_id (int)
            The id of the collection to add to

        Returns
        -------
        None
        """
        from labstep.entities.collection.repository import collectionRepository

        return collectionRepository.addToCollection(self, collection_id=collection_id)

    def getCollections(self):
        """
        Returns the list of collections the protocol is in.
        """
        from labstep.entities.collection.repository import collectionRepository

        return collectionRepository.getAttachedCollections(self)

    def removeFromCollection(self, collection_id):
        """
        Remove the protocol from a collection.

        Parameters
        ----------
        collection_id (int)
            The id of the collection to remove from

        """
        from labstep.entities.collection.repository import collectionRepository

        return collectionRepository.removeFromCollection(self, collection_id)
