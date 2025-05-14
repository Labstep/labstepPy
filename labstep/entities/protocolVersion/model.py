#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import labstep.entities.file.repository as fileRepository
import labstep.entities.protocolInventoryField.repository as protocolInventoryFieldRepository
from labstep.constants import UNSPECIFIED
from labstep.entities.file.model import File
from labstep.entities.jupyterNotebook.model import JupyterNotebook
from labstep.entities.protocolDataField.model import ProtocolDataField
from labstep.entities.protocolInventoryField.model import \
    ProtocolInventoryField
from labstep.entities.protocolStep.model import ProtocolStep
from labstep.entities.protocolTable.model import ProtocolTable
from labstep.entities.protocolTimer.model import ProtocolTimer
from labstep.generic.entityList.model import EntityList
from labstep.generic.entityWithComments.model import EntityWithComments


class ProtocolVersion(EntityWithComments):
    __entityName__ = "protocol"
    __isLegacy__ = True

    def __init__(self, data, user):
        self.state = None
        super().__init__(data, user)
        self.name = f'{self.name} v{self.version + 1}'

    def edit(self, body=UNSPECIFIED, extraParams={}):
        """
        Edit an existing Protocol.

        Parameters
        ----------
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
            self, body=body, extraParams=extraParams
        )

    def setLive(self):
        """
        Set the protocol version as the live version.

        Example
        -------
        ::

            my_protocol = user.getProtocol(17000)
            my_protocol.setLive()
        """
        import labstep.entities.protocolVersion.repository as protocolVersionRepository

        return protocolVersionRepository.edit(self, is_draft=False)

    def getProtocol(self):
        """
        Returns the parent protocol
        """

        return self.__user__.getProtocol(self.protocol_collection['id'])

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
        return self.state

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
        import labstep.generic.entity.repository as entityRepository

        steps = [{"protocol_id": self.id}] * N
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
        if hasattr(self, "protocol_steps") is False:
            return []
        steps = self["protocol_steps"]
        return EntityList(steps, ProtocolStep, self.__user__)

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
        self.update()

        if "metadatas" not in self.metadata_thread:
            return []

        def addId(field):
            field['protocol_id'] = self.id
            return field

        return EntityList(map(addId, self.metadata_thread["metadatas"]), ProtocolDataField, self.__user__)

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
        import labstep.entities.protocolDataField.repository as protocolDataFieldRepository

        return protocolDataFieldRepository.addDataFieldTo(
            self,
            fieldName=fieldName,
            fieldType=fieldType,
            value=value,
            date=date,
            number=number,
            unit=unit,
            filepath=filepath,
            extraParams=extraParams,
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
        return protocolInventoryFieldRepository.newProtocolInventoryField(self.__user__,
                                                                          protocol_id=self.id,
                                                                          resource_id=resource_id, name=name,
                                                                          amount=amount,
                                                                          units=units,
                                                                          extraParams=extraParams)

    def getInventoryFields(self, count=UNSPECIFIED, extraParams={}):
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
        self.update()
        if hasattr(self, "protocol_values") is False:
            return []
        inventoryFields = self.protocol_values
        return EntityList(inventoryFields, ProtocolInventoryField, self.__user__)

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
        import labstep.generic.entity.repository as entityRepository

        params = {
            "protocol_id": self.id,
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
        if hasattr(self, "protocol_timers") is False:
            return []

        timers = self.protocol_timers
        return EntityList(timers, ProtocolTimer, self.__user__)

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
        import labstep.generic.entity.repository as entityRepository

        params = {
            "protocol_id": self.id, "name": name, "data": data}
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
        if hasattr(self, "protocol_tables") is False:
            return []

        tables = self.protocol_tables
        return EntityList(tables, ProtocolTable, self.__user__)

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
        params = {'protocol_id': self.id}
        return fileRepository.newFile(self.__user__,
                                      filepath=filepath,
                                      rawData=rawData,
                                      extraParams=params)

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
        self.update()
        if hasattr(self, "files") is False:
            return []

        files = self.files
        return EntityList(files, File, self.__user__)

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
        self.update()
        return EntityList(self.jupyter_notebooks, JupyterNotebook, self.__user__)

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
        import labstep.entities.jupyterNotebook.repository as jupyterNotebookRepository

        return jupyterNotebookRepository.newJupyterNotebook(self.__user__, name, data, extraParams={'protocol_id': self.id})

    def export(self, path):
        """
        Export the protocol version to the directory specified.

        Parameters
        -------
        path (str)
            The path to the directory to save the protocol version.

        Example
        -------
        ::

            experiment = user.getProtocol(17000)
            experiment.export('/my_folder')
        """
        import labstep.entities.protocolVersion.repository as protocolVersionRepository

        return protocolVersionRepository.exportProtocolVersion(self, path)

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
        from labstep.entities.protocolCondition.repository import \
            addProtocolConditions

        return addProtocolConditions(self, number_of_conditions)

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
        from labstep.entities.protocolCondition.repository import \
            getProtocolConditions

        return getProtocolConditions(self)
