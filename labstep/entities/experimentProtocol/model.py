#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.experimentMaterial.repository import experimentMaterialRepository
from labstep.entities.file.repository import fileRepository
from labstep.entities.file.model import File
from labstep.generic.entity.model import Entity
from labstep.service.helpers import (
    listToClass,
)
from labstep.entities.experimentStep.model import ExperimentStep
from labstep.entities.experimentTable.model import ExperimentTable
from labstep.entities.experimentTimer.model import ExperimentTimer


class ExperimentProtocol(Entity):
    __entityName__ = "experiment"

    __isLegacy__ = True

    def edit(
        self, name=None, body=None, started_at=None, ended_at=None, extraParams={}
    ):
        """
        Edit an existing ExperimentProtocol.

        Parameters
        ----------
        name (str)
            The new name of the ExperimentProtocol.
        body (dict)
            A JSON object representing the new body of the ExperimentProtocol.
        started_at (str)
            The date the ExperimentProtocol was started
            in the format of "YYYY-MM-DD HH:MM".
        ended_at (str)
            The date the ExperimentProtocol was finished
            in the format of "YYYY-MM-DD HH:MM".

        Returns
        -------
        :class:`~labstep.entities.experimentProtocol.model.ExperimentProtocol`
            An object representing the edited ExperimentProtocol.

        Example
        -------
        ::

            my_experiment = user.getExperiment(17000)
            protocols = my_experiment.getProtocols()
            protocols[0].edit(name='A New Experiment Name',
                               started_at='2018-06-06 12:05')
        """
        from labstep.generic.entity.repository import entityRepository

        fields = {
            "name": name,
            "state": body,
            "started_at": started_at,
            "ended_at": ended_at,
            **extraParams,
        }
        return entityRepository.editEntity(self, fields)

    def getBody(self):
        """
        Returns the body of the protocol as a JSON document

        Example
        -------
        ::

            my_experiment = user.getExperiment(17000)
            protocols = my_experiment.getProtocols()
            protocols[0].getBody()
        """
        self.update()
        return getattr(self, "state", None)

    def getMaterials(self, count=100, extraParams={}):
        """
        Returns a list of the materials in a Protocol within an Experiment.

        Returns
        -------
        List[:class:`~labstep.entities.experimentMaterial.model.ExperimentMaterial`]
            List of the materials in an Experiment's Protocol.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_protocol_materials = exp_protocol.getMaterials()
            exp_protocol_materials[0].attributes()
        """
        return experimentMaterialRepository.getExperimentMaterials(self.__user__,
                                                                   experiment_id=self.id, count=count, extraParams=extraParams)

    def addMaterial(
        self,
        name=None,
        amount=None,
        units=None,
        resource_id=None,
        resource_item_id=None,
        extraParams={},
    ):
        """
        Add a new material to the ExperimentProtocol.

        Parameters
        ----------
        name (str)
            The name of the material to add.
        amount (str)
            The amount used.
        units (str)
            The units for the amount.
        resource_id (int)
            The id of the :class:`~labstep.entities.resource.model.Resource` used.
        resource_item_id (ResourceItem)
            The id of the specific
            :class:`~labstep.entities.resource.model.ResourceItem` used.

        Returns
        -------
        :class:`~labstep.entities.experimentMaterial.model.ExperimentMaterial`
            The newly added material entity.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            resource = user.getResources(search_query='Sample A')[0]
            experiment.addMaterial(name='Sample A', amount='2', units='ml',
                                 resource_id=resource.id)
        """
        return experimentMaterialRepository.newExperimentMaterial(self.__user__,
                                                                  experiment_id=self.id,
                                                                  name=name,
                                                                  amount=amount,
                                                                  units=units,
                                                                  resource_id=resource_id,
                                                                  resource_item_id=resource_item_id,
                                                                  extraParams=extraParams)

    def addSteps(self, N):
        """
        Add steps to a Protocol within an Experiment

        Parameters
        ----------
        N (int)
            The number of steps to add.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_protocol_steps = exp_protocol.addSteps(5)
        """
        from labstep.generic.entity.repository import entityRepository

        steps = [{"experiment_id": self.id}] * N
        return entityRepository.newEntities(self.__user__, ExperimentStep, steps)

    def addTable(self, name=None, data=None):
        """
        Add a new table to a Protocol within an Experiment.

        Parameters
        ----------
        name (str)
            The name of the table.
        data (json)
            The data of the table in json format.

        Returns
        -------
        :class:`~labstep.entities.experimentTable.model.ExperimentTable`
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

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_protocol.addTable(name='Calibration', data=data)
        """
        from labstep.generic.entity.repository import entityRepository

        params = {"experiment_id": self.id, "name": name, "data": data}
        return entityRepository.newEntity(self.__user__, ExperimentTable, params)

    def getSteps(self):
        """
        Returns a list of the steps in a Protocol within an Experiment.

        Returns
        -------
        List[:class:`~labstep.entities.experimentStep.model.ExperimentStep`]
            List of the steps in an Experiment's Protocol.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_protocol_steps = exp_protocol.getSteps()
            exp_protocol_steps[0].attributes()
        """
        self.update()
        steps = self.experiment_steps
        return listToClass(steps, ExperimentStep, self.__user__)

    def getTables(self):
        """
        Returns a list of the tables in a Protocol within an Experiment.

        Returns
        -------
        List[:class:`~labstep.entities.experimentTable.model.ExperimentTable`]
            List of the tables in an Experiment's Protocol.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_protocol_tables = exp_protocol.getTables()
            exp_protocol_tables[0].attributes()
        """
        self.update()
        tables = self.experiment_tables
        return listToClass(tables, ExperimentTable, self.__user__)

    def getTimers(self):
        """
        Returns a list of the timers in a Protocol within an Experiment.

        Returns
        -------
        List[:class:`~labstep.entities.experimentTimer.model.ExperimentTimer`]
            List of the timers in an Experiment's Protocol.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_protocol_timers = exp_protocol.getTimers()
            exp_protocol_timers[0].attributes()
        """
        self.update()
        timers = self.experiment_timers
        return listToClass(timers, ExperimentTimer, self.__user__)

    def getDataElements(self):
        """
        Retrieve the Data Elements of a Protocol within an Experiment.

        Returns
        -------
        :class:`~labstep.entities.metadata.model.Metadata`
            An array of objects representing the Labstep
            Data Elements on a Protocol within an Experiment.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            metadata = exp_protocol.getDataElements()
        """
        from labstep.entities.metadata.repository import metadataRepository

        return metadataRepository.getMetadata(self)

    def addDataElement(
        self,
        fieldName,
        fieldType="default",
        value=None,
        date=None,
        number=None,
        unit=None,
        filepath=None,
        extraParams={},
    ):
        """
        Add a Data Element to a Protocol within an Experiment.

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
        filepath (str)
            Local path to the file to upload for type 'file'

        Returns
        -------
        :class:`~labstep.entities.metadata.model.Metadata`
            An object representing the new Labstep Data Element.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            experiment_protocol = experiment.getProtocols()[0]
            dataElement = experiment_protocol.addDataElement(
                "Refractive Index", value="1.73"
            )
        """
        from labstep.entities.metadata.repository import metadataRepository

        return metadataRepository.addMetadataTo(
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

    def addFile(self, filepath=None, rawData=None):
        """
        Add a file to an Experiment Protocol.

        Parameters
        ----------
        filepath (str)
            The path to the file to upload.
        rawData (bytes)
            Raw data to upload as a file.

        Returns
        -------
        :class:`~labstep.file.File`
            The newly added file entity.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            experiment_protocol = experiment.getProtocols()[0]
            file = experiment_protocol.addFile(filepath='./my_file.csv')
        """
        params = {'experiment_id': self.id}
        return fileRepository.newFile(self.__user__, filepath=filepath, rawData=rawData, extraParams=params)

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

            experiment = user.getExperiment(17000)
            experiment_protocol = experiment.getProtocols()[0]
            filess = experiment_protocol.getFiles()
        """
        self.update()
        files = self.files
        return listToClass(files, File, self.__user__)

    def export(self, rootPath):
        from labstep.entities.experimentProtocol.repository import experimentProtocolRepository
        return experimentProtocolRepository.exportExperimentProtocol(self, rootPath)
