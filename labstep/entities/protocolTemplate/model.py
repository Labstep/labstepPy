#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
from labstep.constants import UNSPECIFIED
from labstep.entities.protocolVersion.model import ProtocolVersion
from labstep.generic.entity.repository import getEntityProperty
from labstep.generic.entityPrimary.model import EntityPrimary
from labstep.service.helpers import getTime

class ProtocolTemplate(EntityPrimary):
    """
    Represents a Protocol Template on Labstep.

    To see all attributes of a protocol template run
    ::
        print(my_protocol_template)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(my_protocol_template.name)
        print(my_protocol_template.id)
    """

    __entityName__ = "protocol-collection"
    __searchKey__ = 'label'

    @property
    def draft_version(self):
        return getEntityProperty(self, 'draft_version', ProtocolVersion)

    @property
    def last_version(self):
        return getEntityProperty(self, 'last_version', ProtocolVersion)

    def getCurrentVersion(self):
        """
        Returns the current version of the protocol template.

        Returns
        -------
        :class:`~labstep.entities.protocolVersion.model.ProtocolVersion`
            The current version of the protocol template.
        """
        if self.draft_version:
            return self.draft_version
        return self.last_version

    def edit(self, name=UNSPECIFIED, body=UNSPECIFIED, extraParams={}):
        """
        Edit an existing Protocol Template.

        Parameters
        ----------
        name (str)
            The name of the Protocol Template.
        body (dict):
            JSON representing the the protocol template document.

        Returns
        -------
        :class:`~labstep.entities.protocolTemplate.model.ProtocolTemplate`
            An object representing the edited Protocol Template.

        Example
        -------
        ::

            my_protocol_template = user.getProtocolTemplate(17000)
            my_protocol_template.edit(name='A New Protocol Template Name')
        """
        import labstep.entities.protocolTemplate.repository as protocolTemplateRepository
        return protocolTemplateRepository.editProtocolTemplate(
            self, name=name, body=body, extraParams=extraParams
        )

    def delete(self):
        """
        Delete an existing Protocol Template.

        Example
        -------
        ::

            my_protocol_template = user.getProtocolTemplate(17000)
            my_protocol_template.delete()
        """
        import labstep.entities.protocolTemplate.repository as protocolTemplateRepository
        return protocolTemplateRepository.editProtocolTemplate(self, deleted_at=getTime())

    def newVersion(self):
        """
        Start a new version of the Protocol Template.

        Example
        -------
        ::

            my_protocol_template = user.getProtocolTemplate(17000)
            new_version = my_protocol_template.newVersion()
        """
        import labstep.generic.entity.repository as entityRepository
        entityRepository.newEntity(
            self.__user__, ProtocolVersion, {"protocol_collection_id": self.id}
        )
        return self.update()

    def getBody(self):
        """
        Returns the body of the protocol template as a JSON document

        Example
        -------
        ::

            my_protocol_template = user.newProtocolTemplate('My API Protocol Template')

            my_protocol_template.edit(body={
                "type": "doc",
                "content": [
                    {
                        "type": "paragraph",
                        "attrs": {"align": None},
                        "content": [
                            {
                                "type": "text",
                                "text": "This is the the body of my protocol template"
                            }
                        ]
                    },
                    {
                        "type": "paragraph",
                        "attrs": {"align": None}
                    }
                ]
            })

            my_protocol_template.getBody()
        """
        return self.getCurrentVersion().getBody()


    def getSteps(self):
        """
        Returns a list of the steps in a Protocol Template.

        Returns
        -------
        List[:class:`~labstep.entities.protocolStep.model.ProtocolStep`]
            List of the steps in Protocol Template.

        Example
        -------
        ::

            protocol_template = user.getProtocolTemplate(17000)
            protocol_template_steps = protocol_template.getSteps()
        """
        return self.getCurrentVersion().getSteps()

    def getDataFields(self):
        """
        Retrieve the Data Fields of a Protocol Template.

        Returns
        -------
        :class:`~labstep.entities.metadata.model.Metadata`
            An array of objects representing the Labstep Data Fields
            on a Protocol Template.

        Example
        -------
        ::

            protocol_template = user.getProtocolTemplate(17000)
            metadata = protocol_template.getDataFields()
        """
        return self.getCurrentVersion().getDataFields()

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
        Add a Data Field to a Protocol Template.

        Parameters
        ----------
        fieldName (str)
            The name of the field.
        fieldType (str)
            The field type. Options are: "default", "date",
            "datetime", or "numeric". The "default" type is "Text".
        value (str)
            The value accompanying the fieldName entry.
        date (str)
            The date and time accompanying the fieldName entry. Must be
            in the format of "YYYY-MM-DD HH:MM".
        number (float)
            The quantity.
        unit (str)
            The unit accompanying the numeric entry.

        Returns
        -------
        :class:`~labstep.entities.metadata.model.Metadata`
            An object representing the new Labstep Data Field.

        Example
        -------
        ::

            protocol_template = user.getProtocolTemplate(17000)
            dataField = protocol_template.addDataField("Refractive Index",
                                               value="1.73")
        """
        return self.getCurrentVersion().addDataField(
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
        self, name=UNSPECIFIED, amount=UNSPECIFIED, units=UNSPECIFIED, resource_id=UNSPECIFIED, category_id=UNSPECIFIED,extraParams={}
    ):
        """
        Add a new inventory field to the Protocol Template.

        Parameters
        ----------
        name (str)
            The name of the inventory field to add.
        amount (str)
            The amount required by the protocol template.
        units (str)
            The units for the amount.
        resource_id (int)
            The id of the :class:`~labstep.entities.resource.model.Resource`. Items must be from this resource.
        category_id (int)
            The id of the :class:`~labstep.entities.resourceCategory.model.ResourceCategory`.
            Items must be from this resource category.

        Returns
        -------
        :class:`~labstep.entities.protocolInventoryField.model.ProtocolInventoryField`
            The newly added inventory field entity.

        Example
        -------
        ::

            protocol_template = user.getProtocolTemplate(17000)
            resource = user.getResources(search_query='Sample A')[0]
            protocol_template.addInventoryField(name='Sample A', amount='2', units='ml',
                                 resource_id=resource.id)
        """
        return self.getCurrentVersion().addInventoryField(
            resource_id=resource_id, name=name,
            amount=amount,
            units=units,
            category_id=category_id,
            extraParams=extraParams)

    def getInventoryFields(self, count=100, extraParams={}):
        """
        Returns a list of the inventory fields in a Protocol Template.

        Returns
        -------
        List[:class:`~labstep.entities.protocolInventoryField.model.ProtocolInventoryField`]
            List of the inventory fields in a Protocol Template.

        Example
        -------
        ::

            protocol_template = user.getProtocolTemplate(17000)
            protocol_template_inventoryFields = protocol_template.getInventoryFields()
            protocol_template_inventory_fields[0]
        """
        return self.getCurrentVersion().getInventoryFields(count=count, extraParams=extraParams)

    def addTimer(self, name=UNSPECIFIED, hours=UNSPECIFIED, minutes=UNSPECIFIED, seconds=UNSPECIFIED):
        """
        Add a new timer to the Protocol Template.

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

            protocol_template = user.getProtocolTemplate(17000)
            protocol_template.addTimer(name='Refluxing', hours='4', minutes='30')
        """
        return self.getCurrentVersion().addTimer(name=name, hours=hours, minutes=minutes, seconds=seconds)

    def getTimers(self):
        """
        Returns a list of the timers in a Protocol Template.

        Returns
        -------
        List[:class:`~labstep.entities.protocolTimer.model.ProtocolTimer`]
            List of the timers in a Protocol Template.

        Example
        -------
        ::

            protocol_template = user.getProtocolTemplate(17000)
            protocol_template_timers = protocol_template.getTimers()
        """
        return self.getCurrentVersion().getTimers()

    def addTable(self, name=UNSPECIFIED, data=UNSPECIFIED):
        """
        Add a new table to the Protocol Template.

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

            protocol_template = user.getProtocolTemplate(17000)
            protocol_template.addTable(name='Calibration', data=data)
        """
        return self.getCurrentVersion().addTable(name=name, data=data)

    def getTables(self):
        """
        Returns a list of the tables in a Protocol Template.

        Returns
        -------
        List[:class:`~labstep.entities.protocolTable.model.ProtocolTable`]
            List of the tables in a Protocol Template.

        Example
        -------
        ::

            protocol_template = user.getProtocolTemplate(17000)
            protocol_template_tables = protocol_template.getTables()
        """
        return self.getCurrentVersion().getTables()

    def addFile(self, filepath=UNSPECIFIED, rawData=UNSPECIFIED):
        """
        Add a file to a Protocol Template.

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

            protocol_template = user.getProtocolTemplate(17000)
            protocol_template.addFile(filepath='./my_file.csv')
        """
        return self.getCurrentVersion().addFile(filepath=filepath, rawData=rawData)

    def getFiles(self):
        """
        Returns a list of the files in a Protocol Template.

        Returns
        -------
        List[:class:`~labstep.file.File`]
            List of the files in a Protocol Template.

        Example
        -------
        ::

            protocol_template = user.getProtocolTemplate(17000)
            protocol_template_files = protocol_template.getFiles()
        """
        return self.getCurrentVersion().getFiles()

    def export(self, path):
        """
        Export the protocol template to the directory specified.

        Parameters
        -------
        path (str)
            The path to the directory to save the protocol template.

        Example
        -------
        ::

            protocol_template = user.getProtocolTemplate(17000)
            protocol_template.export('/my_folder')
        """
        import labstep.entities.protocolTemplate.repository as protocolTemplateRepository

        return protocolTemplateRepository.exportProtocolTemplate(self, path)

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

            protocol_template = user.getProtocolTemplate(17000)
            jupyter_notebooks = protocol_template.getJupyterNotebooks()
            print(jupyter_notebooks[0])
        """
        return self.getCurrentVersion().getJupyterNotebooks()

    def addJupyterNotebook(self, name=UNSPECIFIED, data=UNSPECIFIED):
        """
        Add a Jupyter Notebook to a protocol template entry.

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

            protocol_template = user.getProtocolTemplate(17000)
            protocol_template.addJupyterNotebook()
        """
        return self.getCurrentVersion().addJupyterNotebook(name=name, data=data)

    def addConditions(self, number_of_conditions):
        """
        Add conditions to the protocol template
        Parameters
        ----------
        number_of_conditions (int)
            The number of conditions to add
        Returns
        -------
        List[:class:`~labstep.entities.protocolCondition.model.ProtocolCondition`]
            A list of the protocol conditions added to the protocol template.
        Example
        -------
        ::

            protocol_template = user.getProtocolTemplate(17000)
            conditions = protocol_template.addConditions(5)
        """
        if not self.draft_version:
            raise ValueError("Cannot add conditions to a protocol template that is not in draft state. Please create a new version first.")

        return self.draft_version.addConditions(number_of_conditions)


    def getVersions(self):
        """
        Retrieve a list of the different versions associated with this protocol template.
        Returns
        -------
        List[:class:`~labstep.entities.protocolVersion.model.ProtocolVersion`]
            A list of the protocol versions associated with the protocol template.
        Example
        -------
        ::

            protocol_template = user.getProtocolTemplate(17000)
            versions = protocol_template.getVersions()
        """
        from labstep.generic.entity.repository import getEntities


        return getEntities(self.__user__, ProtocolVersion, UNSPECIFIED,filterParams={"protocol_collection_id": self.id})

