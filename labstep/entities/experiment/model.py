#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.primaryEntity.model import PrimaryEntity
from labstep.entities.experimentProtocol.model import ExperimentProtocol
from labstep.entities.experimentMaterial.model import ExperimentMaterial
from labstep.entities.experimentTable.model import ExperimentTable
from labstep.entities.experimentSignature.model import ExperimentSignature
from labstep.service.helpers import getTime, listToClass


class Experiment(PrimaryEntity):
    """
    Represents an Experiment on Labstep.

    To see all attributes of an experiment run
    ::
        print(my_experiment)

    Specific attributes can be inspected via dot notation like so...
    ::
        print(my_experiment.name)
        print(my_experiment.id)
    """

    __entityName__ = "experiment-workflow"

    def __init__(self, data, user):
        super().__init__(data, user)
        if "root_experiment" in data:
            self.root_experiment = ExperimentProtocol(
                data['root_experiment'], user)

    def edit(self, name=None, entry=None, started_at=None, extraParams={}):
        """
        Edit an existing Experiment.

        Parameters
        ----------
        name (str)
            The new name of the Experiment.
        entry (obj)
            A JSON object representing the state of the Experiment Entry.
        started_at (str)
            The start date of the Experiment
            in the format of "YYYY-MM-DD HH:MM".

        Returns
        -------
        :class:`~labstep.entities.experiment.model.Experiment`
            An object representing the edited Experiment.

        Example
        -------
        ::

            my_experiment = user.getExperiment(17000)
            my_experiment.edit(name='A New Experiment Name',
                               started_at='2018-06-06 12:05')
        """
        from labstep.entities.experiment.repository import experimentRepository

        return experimentRepository.editExperiment(
            self, name=name, entry=entry, started_at=started_at, extraParams=extraParams
        )

    def delete(self):
        """
        Delete an existing Experiment.

        Example
        -------
        ::

            my_experiment = user.getExperiment(17000)
            my_experiment.delete()
        """
        from labstep.entities.experiment.repository import experimentRepository

        return experimentRepository.editExperiment(self, deleted_at=getTime())

    def getEntry(self):
        """
        Returns a JSON document representing the entry for the experiment.

        Example
        -------
        ::

            my_experiment = user.getExperiment(17000)
            print(my_experiment.getEntry())
        """
        from labstep.generic.entity.repository import entityRepository

        return entityRepository.getEntity(
            self.__user__, ExperimentProtocol, self.root_experiment.id
        ).state

    def addProtocol(self, protocol):
        """
        Add a Labstep Protocol to a Labstep Experiment.

        Parameters
        ----------
        protocol (Protocol)
            The :class:`~labstep.entities.protocol.model.Protocol` to attach.

        Returns
        -------
        :class:`~labstep.entities.protocol.model.Protocol`
            An object representing the Protocol attached to the Experiment.

        Example
        -------
        ::

            # Get an Experiment
            my_experiment = user.getExperiment(17000)

            # Get a Protocol
            my_protocol = user.getProtocol(10000)

            # Attach the Protocol to the Experiment
            my_experiment.addProtocol(my_protocol)
        """
        from labstep.entities.experiment.repository import experimentRepository

        return experimentRepository.addProtocolToExperiment(self, protocol)

    def getProtocols(self, count=100):
        """
        Retrieve the Protocols attached to this Labstep Experiment.

        Returns
        -------
        List[:class:`~labstep.entities.experimentProtocol.model.ExperimentProtocol`]
            List of the Protocols attached to the Experiment.

        Example
        -------
        ::

            entity = user.getExperiment(17000)
            protocols = entity.getProtocols()
            protocols[0].attributes()
        """
        from labstep.generic.entity.repository import entityRepository

        return entityRepository.getEntities(
            self.__user__,
            ExperimentProtocol,
            count,
            {"is_root": 0, "experiment_workflow_id": self.id},
        )

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
        Add Data Elements to a Labstep Experiment.

        Parameters
        ----------
        fieldName (str)
            The name of the field.
        fieldType (str)
            The Metadata field type. Options are: "default", "date",
            "numeric", or "file". The "default" type is "Text".
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
            dataElement = experiment.addDataElement("Refractive Index",
                                               value="1.73")
        """
        return self.root_experiment.addDataElement(
            fieldName=fieldName,
            fieldType=fieldType,
            value=value,
            date=date,
            number=number,
            unit=unit,
            filepath=filepath,
            extraParams=extraParams,
        )

    def getDataElements(self):
        """
        Retrieve the Data Elements of a Protocol within an Experiment.

        Returns
        -------
        :class:`~labstep.entities.metadata.model.Metadata`
            An array of objects representing Data Elements
            on a Protocol within an Experiment.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            dataElements = exp_protocol.getDataElements()
        """
        return self.root_experiment.getDataElements()

    def getSignatures(self):
        """
        Retrieve a list of signatures added to the experiment

        Returns
        -------
        List[:class:`~labstep.entities.experimentSignature.model.ExperimentSignature`]
            List of the signatures added to the Experiment
        """
        exp = self.__user__.getExperiment(self.id)
        return listToClass(exp.signatures, ExperimentSignature, self.__user__)

    def addSignature(self, statement=None, lock=False):
        """
        Add a signature to experiment

        Parameters
        ----------
        statement (str)
            Statement describing the signature.
        lock (boolean)
            Whether to lock the experiment against further edits.

        Returns
        -------
        :class:`~labstep.entities.experimentSignature.model.ExperimentSignature`
            The signature that has been added
        """
        from labstep.generic.entity.repository import entityRepository

        params = {
            "statement": statement,
            "is_lock": int(lock),
            "experiment_workflow_id": self.id,
        }
        return entityRepository.newEntity(self.__user__, ExperimentSignature, params)

    def getMaterials(self):
        """
        Returns a list of the materials in the Experiment.

        Returns
        -------
        List[:class:`~labstep.entities.experimentMaterial.model.ExperimentMaterial`]
            List of the materials in an Experiment.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_materials = experiment.getMaterials()
            print(exp_materials[0])
        """
        return self.root_experiment.getMaterials()

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
        Add a new material to the Experiment.

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
        return self.root_experiment.addMaterial(name=name,
                                                resource_id=resource_id,
                                                resource_item_id=resource_item_id,
                                                amount=amount,
                                                units=units,
                                                extraParams=extraParams)

    def addToCollection(self, collection_id):
        """
        Add the experiment to a collection.

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
        Remove the experiment from a collection.

        Parameters
        ----------
        collection_id (int)
            The id of the collection to remove from

        """
        from labstep.entities.collection.repository import collectionRepository

        return collectionRepository.removeFromCollection(self, collection_id)

    def addTable(self, name=None, data=None):
        """
        Add a new table to an Experiment.

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
            experiment.addTable(name='Calibration', data=data)
        """
        from labstep.generic.entity.repository import entityRepository

        params = {"experiment_id": self.root_experiment.id,
                  "name": name, "data": data}
        return entityRepository.newEntity(self.__user__, ExperimentTable, params)

    def addFile(self, filepath=None, rawData=None):
        """
        Add a file to an experiment entry.
        (Only use for files to be embedded in the body of the entry)

        Parameters
        ----------
        filepath (str)
            The path to the file to upload.
        rawData (bytes)
            Raw bytes data to upload as file

        Returns
        -------
        :class:`~labstep.file.File`
            The newly added file entity.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            experiment.addFile(filepath='./my_file.csv')
        """
        return self.root_experiment.addFile(filepath, rawData)

    def getFiles(self):
        """
        Returns a list of the files in a experiment entry.
        (Only includes the files embedded in the body of the entry)

        Returns
        -------
        List[:class:`~labstep.file.File`]
            List of the files in a experiment.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            experiment_files = experiment.getFiles()
        """
        return self.root_experiment.getFiles()

    def export(self, path):
        """
        Export the experiment to the directory specified. 

        Paramers
        -------
        path (str)
            The path to the directory to save the experiment.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            experiment.export('/my_folder')
        """
        from labstep.entities.experiment.repository import experimentRepository

        return experimentRepository.exportExperiment(self, path)
