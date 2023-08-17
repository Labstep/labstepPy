#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
from deprecated import deprecated
from ..jupyterNotebook.model import JupyterNotebook
from labstep.entities.protocolDataField.model import ProtocolDataField
from labstep.generic.entityPrimary.model import EntityPrimary
from labstep.entities.protocolStep.model import ProtocolStep
from labstep.entities.protocolTable.model import ProtocolTable
from labstep.entities.protocolTimer.model import ProtocolTimer
from labstep.entities.protocolVersion.model import ProtocolVersion
from labstep.entities.protocolInventoryField.model import ProtocolInventoryField
import labstep.entities.protocolInventoryField.repository as protocolInventoryFieldRepository
from labstep.generic.entityList.model import EntityList
from labstep.entities.file.model import File
import labstep.entities.file.repository as fileRepository
from labstep.service.helpers import getTime
from labstep.constants import UNSPECIFIED


class Protocol(EntityPrimary):
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
    __searchKey__ = 'label'

    def __init__(self, data, user):
        super().__init__(data, user)
        if "last_version" in data:
            self.last_version = ProtocolVersion(
                data['last_version'], user)

    def edit(self, name=UNSPECIFIED, body=UNSPECIFIED, extraParams={}):
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
        import labstep.entities.protocol.repository as protocolRepository

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
        import labstep.entities.protocol.repository as protocolRepository

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
        import labstep.generic.entity.repository as entityRepository

        entityRepository.newEntity(
            self.__user__, ProtocolVersion, {"protocol_collection_id": self.id}
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
        return self.last_version.getBody()

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
        return self.last_version.addSteps(N)

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
        return self.last_version.getSteps()

    def getDataFields(self):
        """
        Retrieve the Data Fields of a Protocol.

        Returns
        -------
        :class:`~labstep.entities.metadata.model.Metadata`
            An array of objects representing the Labstep Data Fields
            on a Protocol.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            metadata = protocol.getDataFields()
        """
        return self.last_version.getDataFields()

    def addDataField(
        self,
        fieldName,
        fieldType="default",
        value=UNSPECIFIED,
        date=UNSPECIFIED,
        number=UNSPECIFIED,
        unit=UNSPECIFIED,
        filepath=UNSPECIFIED,
        extraParams={},
    ):
        """
        Add a Data Field to a Protocol.

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
            An object representing the new Labstep Data Field.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            dataField = protocol.addDataField("Refractive Index",
                                               value="1.73")
        """
        return self.last_version.addDataField(
            fieldName=fieldName,
            fieldType=fieldType,
            value=value,
            date=date,
            number=number,
            unit=unit,
            filepath=filepath,
            extraParams=extraParams
        )

    def addInventoryField(
        self, name=UNSPECIFIED, amount=UNSPECIFIED, units=UNSPECIFIED, resource_id=UNSPECIFIED, extraParams={}
    ):
        """
        Add a new inventory field to the Protocol.

        Parameters
        ----------
        name (str)
            The name of the inventory field to add.
        amount (str)
            The amount required by the protocol.
        units (str)
            The units for the amount.
        resource_id (int)
            The id of the :class:`~labstep.entities.resource.model.Resource` recommended for
            use with the protocol.

        Returns
        -------
        :class:`~labstep.entities.protocolInventoryField.model.ProtocolInventoryField`
            The newly added inventory field entity.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            resource = user.getResources(search_query='Sample A')[0]
            protocol.addInventoryField(name='Sample A', amount='2', units='ml',
                                 resource_id=resource.id)
        """
        return self.last_version.addInventoryField(
            resource_id=resource_id, name=name,
            amount=amount,
            units=units,
            extraParams=extraParams)

    def getInventoryFields(self, count=100, extraParams={}):
        """
        Returns a list of the inventory fields in a Protocol.

        Returns
        -------
        List[:class:`~labstep.entities.protocolInventoryField.model.ProtocolInventoryField`]
            List of the inventory fields in a Protocol.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            protocol_inventoryFields = protocol.getInventoryFields()
            protocol_inventory_fields[0]
        """
        return self.last_version.getInventoryFields(count=count, extraParams=extraParams)

    def addTimer(self, name=UNSPECIFIED, hours=UNSPECIFIED, minutes=UNSPECIFIED, seconds=UNSPECIFIED):
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
        return self.last_version.addTimer(name=name, hours=hours, minutes=minutes, seconds=seconds)

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
        return self.last_version.getTimers()

    def addTable(self, name=UNSPECIFIED, data=UNSPECIFIED):
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
        return self.last_version.addTable(name=name, data=data)

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
        return self.last_version.getTables()

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
        import labstep.entities.collection.repository as collectionRepository

        return collectionRepository.addToCollection(self, collection_id=collection_id)

    def getCollections(self):
        """
        Returns the list of collections the protocol is in.
        """
        import labstep.entities.collection.repository as collectionRepository

        return collectionRepository.getAttachedCollections(self)

    def removeFromCollection(self, collection_id):
        """
        Remove the protocol from a collection.

        Parameters
        ----------
        collection_id (int)
            The id of the collection to remove from

        """
        import labstep.entities.collection.repository as collectionRepository

        return collectionRepository.removeFromCollection(self, collection_id)

    def addFile(self, filepath=UNSPECIFIED, rawData=UNSPECIFIED):
        """
        Add a file to a Protocol.

        Parameters
        ----------
        filepath (str)
            The path to the file to upload.

        Returns
        -------
        :class:`~labstep.file.File`
            The newly added file entity.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            protocol.addFile(filepath='./my_file.csv')
        """
        return self.last_version.addFile(filepath=filepath, rawData=rawData)

    def getFiles(self):
        """
        Returns a list of the files in a Protocol.

        Returns
        -------
        List[:class:`~labstep.file.File`]
            List of the files in a Protocol.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            protocol_files = protocol.getFiles()
        """
        return self.last_version.getFiles()

    def export(self, path):
        """
        Export the protocol to the directory specified.

        Parameters
        -------
        path (str)
            The path to the directory to save the protocol.

        Example
        -------
        ::

            experiment = user.getProtocol(17000)
            experiment.export('/my_folder')
        """
        import labstep.entities.protocol.repository as protocolRepository

        return protocolRepository.exportProtocol(self, path)

    def getJupyterNotebooks(self, count=100):
        """
        Retrieve the Jupyter Notebooks attached to this Labstep Entity.

        Returns
        -------
        List[:class:`~labstep.entities.jupyterNotebook.model.JupyterNotebook`]
            List of the Jupyter Notebooks attached.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            jupyter_notebooks = protocol.getJupyterNotebooks()
            print(jupyter_notebooks[0])
        """
        return self.last_version.getJupyterNotebooks()

    def addJupyterNotebook(self, name=UNSPECIFIED, data=UNSPECIFIED):
        """
        Add a Jupyter Notebook to an protocol entry.

        Parameters
        ----------
        name (str)
            Name of Jupyter Notebook
        data (JSON)
            JSON Jupyter Notebook structure

        Returns
        -------
        :class:`~labstep.entities.jupyterNotebook.model.JupyterNotebook`
            The newly added file entity.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            protocol.addJupyterNotebook()
        """
        return self.last_version.addJupyterNotebook(name=name, data=data)
    

    def addConditions(self, number_of_conditions):
        """
        Add conditions to the protocol
        Parameters
        ----------
        number_of_conditions (int)
            The number of conditions to add
        Returns
        -------
        List[:class:`~labstep.entities.protocolCondition.model.ProtocolCondition`]
            A list of the protocol conditions added to the protocol.
        Example
        -------
        ::
            protocol = user.getProtocol(17000)
            conditions = protocol.addConditions(5)
        """

        return self.last_version.addConditions(number_of_conditions)

    def getConditions(self):
        """
        Retrieve a list of the different conditions associated with this protocol.
        Returns
        -------
        List[:class:`~labstep.entities.protocolCondition.model.ProtocolCondition`]
            A list of the protocol conditions associated with the protocol.
        Example
        -------
        ::
            protocol = user.getProtocol(17000)
            conditions = protocol.getConditions()
        """

        return self.last_version.getConditions()

    @deprecated(version='3.3.2', reason="You should use experiment.addDataField instead")
    def addDataElement(self, *args, **kwargs):
        return self.addDataField(*args, **kwargs)

    @deprecated(version='3.3.2', reason="You should use experiment.getDataFields instead")
    def getDataElements(self):
        return self.getDataFields()

    @deprecated(version='3.12.0', reason="You should use getInventoryFields instead")
    def getMaterials(self, *args, **kwargs):
        return self.getInventoryFields(*args, **kwargs)

    @deprecated(version='3.12.0', reason="You should use addInventoryField instead")
    def addMaterial(self, *args, **kwargs):
        return self.addInventoryField(*args, **kwargs)
