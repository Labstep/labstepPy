#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
from deprecated import deprecated
from labstep.entities.file.model import File
from labstep.generic.entity.model import Entity
from labstep.generic.entityList.model import EntityList
from labstep.entities.experimentStep.model import ExperimentStep
from labstep.entities.jupyterNotebook.model import JupyterNotebook
from labstep.entities.chemicalReaction.model import ChemicalReaction
from labstep.entities.experimentTable.model import ExperimentTable
from labstep.entities.experimentTimer.model import ExperimentTimer
from labstep.entities.experimentInventoryField.model import ExperimentInventoryField
import labstep.entities.file.repository as fileRepository
import labstep.entities.experimentInventoryField.repository as experimentInventoryFieldRepository
import labstep.entities.chemicalReaction.repository as chemicalReactionRepository
from labstep.constants import UNSPECIFIED


class ExperimentProtocol(Entity):
    __entityName__ = "experiment"
    __unSearchable__ = True

    def edit(
        self, name=UNSPECIFIED, body=UNSPECIFIED, started_at=UNSPECIFIED, ended_at=UNSPECIFIED, extraParams={}
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
        import labstep.generic.entity.repository as entityRepository

        fields = {
            "name": name,
            "state": body,
            "started_at": started_at,
            "ended_at": ended_at,
            **extraParams,
        }
        return entityRepository.editEntity(self, fields)

    def getExperiment(self):

        from labstep.entities.experiment.repository import getExperiment

        return getExperiment(self.__user__, self.experiment_workflow['id'])

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
        return self.state

    def getInventoryFields(self, count=UNSPECIFIED, extraParams={}):
        """
        Returns a list of the inventory fields in a Protocol within an Experiment.

        Returns
        -------
        List[:class:`~labstep.entities.experimentInventoryField.model.ExperimentInventoryField`]
            List of the inventory fields in an Experiment's Protocol.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_protocol_inventory_fields = exp_protocol.getInventoryFields()
            exp_protocol_inventory_fields[0].attributes()
        """
        self.update()
        return EntityList(self.protocol_values, ExperimentInventoryField, self.__user__)

        # return experimentInventoryFieldRepository.getExperimentInventoryFields(self.__user__,experiment_id=self.id, count=count, extraParams=extraParams)

    def addInventoryField(
        self,
        name=UNSPECIFIED,
        amount=UNSPECIFIED,
        units=UNSPECIFIED,
        resource_id=UNSPECIFIED,
        resource_item_id=UNSPECIFIED,
        extraParams={},
    ):
        """
        Add a new inventory field to the ExperimentProtocol.

        Parameters
        ----------
        name (str)
            The name of the inventory field to add.
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
        :class:`~labstep.entities.experimentInventoryField.model.ExperimentInventoryField`
            The newly added inventory field entity.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            resource = user.getResources(search_query='Sample A')[0]
            experiment.addInventoryField(name='Sample A', amount='2', units='ml',
                                 resource_id=resource.id)
        """
        return experimentInventoryFieldRepository.newExperimentInventoryField(self.__user__,
                                                                              experiment_id=self.id,
                                                                              name=name,
                                                                              amount=amount,
                                                                              units=units,
                                                                              resource_id=resource_id,
                                                                              resource_item_id=resource_item_id,
                                                                              extraParams=extraParams)

    def addChemicalReaction(
        self,
        extraParams={},
    ):
        """
        Add a new chemical reaction to the ExperimentProtocol.

        Parameters
        ----------

        Returns
        -------
        :class:`~labstep.entities.chemicalReaction.model.ChemicalReaction`
            The newly added chemical reaction

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            experiment.addChemicalReaction()
        """
        return chemicalReactionRepository.newChemicalReaction(self.__user__, self.id, extraParams=extraParams)

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
        import labstep.generic.entity.repository as entityRepository

        steps = [{"experiment_id": self.id}] * N
        return entityRepository.newEntities(self.__user__, ExperimentStep, steps)

    def addTable(self, name=UNSPECIFIED, data=UNSPECIFIED):
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
        import labstep.generic.entity.repository as entityRepository

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
        if hasattr(self, 'experiment_steps'):
            steps = self.experiment_steps
        else:
            steps = self.protocol_steps
        return EntityList(steps, ExperimentStep, self.__user__)

    def getChemicalReactions(self):
        """
        Returns a list of the chemical reactions in a Protocol within an Experiment.

        Returns
        -------
        List[:class:`~labstep.entities.chemicalReaction.model.ChemicalReaction`]
            List of the chemical reactions in an Experiment's Protocol.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_chemical_reactions = exp_protocol.getChemicalReactions()
        """
        self.update()
        return EntityList(self.molecules, ChemicalReaction, self.__user__)

    def addTimer(self, name=UNSPECIFIED, hours=UNSPECIFIED, minutes=UNSPECIFIED, seconds=UNSPECIFIED):
        """
        Add a new timer to a Protocol within an Experiment.

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
        :class:`~labstep.entities.ExperimentTimer.model.ExperimentTimer`
            The newly added timer entity.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_protocol.addTimer(name='Refluxing', hours='4', minutes='30')
        """
        import labstep.generic.entity.repository as entityRepository

        params = {
            "experiment_id": self.id,
            "name": name,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
        }
        return entityRepository.newEntity(self.__user__, ExperimentTimer, params)

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
        if hasattr(self, 'experiment_tables'):
            tables = self.experiment_tables
        else:
            tables = self.protocol_tables
        return EntityList(tables, ExperimentTable, self.__user__)

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
        if hasattr(self, 'experiment_timers'):
            timers = self.experiment_timers
        else:
            timers = self.protocol_timers
        return EntityList(timers, ExperimentTimer, self.__user__)

    def getDataFields(self):
        """
        Retrieve the Data Fields of a Protocol within an Experiment.

        Returns
        -------
        :class:`~labstep.entities.experimentDataField.model.ExperimentDataField`
            An array of objects representing the Labstep
            Data Fields on a Protocol within an Experiment.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            metadata = exp_protocol.getDataFields()
        """
        import labstep.entities.experimentDataField.repository as experimentDataFieldRepository

        return experimentDataFieldRepository.getDataFields(self)

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
        Add a Data Field to a Protocol within an Experiment.

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
            An object representing the new Labstep Data Field.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            experiment_protocol = experiment.getProtocols()[0]
            dataField = experiment_protocol.addDataField(
                "Refractive Index", value="1.73"
            )
        """
        import labstep.entities.experimentDataField.repository as experimentDataFieldRepository

        return experimentDataFieldRepository.addDataFieldTo(
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

    def addFile(self, filepath=UNSPECIFIED, rawData=UNSPECIFIED):
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
            files = experiment_protocol.getFiles()
        """
        self.update()
        return EntityList(self.files, File, self.__user__)

    def export(self, rootPath, folderName=UNSPECIFIED):
        import labstep.entities.experimentProtocol.repository as experimentProtocolRepository
        return experimentProtocolRepository.exportExperimentProtocol(self, rootPath, folderName=folderName)

    def getJupyterNotebooks(self, count=UNSPECIFIED):
        """
        Retrieve the Jupyter Notebooks attached to this Labstep Entity.

        Returns
        -------
        List[:class:`~labstep.entities.jupyterNotebook.model.JupyterNotebook`]
            List of the Jupyter Notebooks attached.

        Example
        -------
        ::

            entity = user.getExperiment(17000)
            jupyter_notebooks = entity.getJupyterNotebooks()
            print(jupyter_notebooks[0])
        """
        self.update()
        return EntityList(self.jupyter_notebooks, JupyterNotebook, self.__user__)

    def addJupyterNotebook(self, name=UNSPECIFIED, data=UNSPECIFIED):
        """
        Add a Jupyter Notebook to an experiment entry.

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

            experiment = user.getExperiment(17000)
            experiment.addJupyterNotebook()
        """
        import labstep.entities.jupyterNotebook.repository as jupyterNotebookRepository

        return jupyterNotebookRepository.newJupyterNotebook(self.__user__, name, data, extraParams={'experiment_id': self.id})

    def addConditions(self, number_of_conditions):
        """
        Add conditions to the experiment protocol
        Parameters
        ----------
        number_of_conditions (int)
            The number of conditions to add
        Returns
        -------
        List[:class:`~labstep.entities.protocolCondition.model.ProtocolCondition`]
            A list of the protocol conditions added to the experiment.
        Example
        -------
        ::
        
            experiment = user.getExperiment(17000)
            protocol = experiment.getProtocols()[0]
            conditions = protocol.addConditions(5)
        """
        from labstep.entities.experimentCondition.repository import addExperimentConditions

        return addExperimentConditions(self, number_of_conditions)

    def getConditions(self):
        """
        Retrieve a list of the different conditions associated with this experiment protocol.
        Returns
        -------
        List[:class:`~labstep.entities.protocolCondition.model.ProtocolCondition`]
            A list of the protocol conditions associated with the experiment protocol.
        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            protocol = experiment.getProtocols()[0]
            conditions = protocol.getConditions()
        """
        from labstep.entities.experimentCondition.repository import getExperimentConditions

        return getExperimentConditions(self)

    @deprecated(version='3.3.2', reason="You should use experimentProtocol.addDataField instead")
    def addDataElement(self, *args, **kwargs):
        return self.addDataField(*args, **kwargs)

    @deprecated(version='3.3.2', reason="You should use experimentProtocol.getDataFields instead")
    def getDataElements(self):
        return self.getDataFields()

    @deprecated(version='3.12.0', reason="You should use getInventoryFields instead")
    def getMaterials(self, *args, **kwargs):
        return self.getInventoryFields(*args, **kwargs)

    @deprecated(version='3.12.0', reason="You should use addInventoryField instead")
    def addMaterial(self, *args, **kwargs):
        return self.addInventoryField(*args, **kwargs)
