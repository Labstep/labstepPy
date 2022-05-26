#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>
from deprecated import deprecated
from labstep.entities.experimentLink.repository import newExperimentLink
from labstep.generic.entityPrimary.model import EntityPrimary
from labstep.generic.entityList.model import EntityList
from labstep.entities.experimentProtocol.model import ExperimentProtocol
from labstep.entities.experimentSignature.model import ExperimentSignature
from labstep.service.helpers import getTime, handleDate
from labstep.constants import UNSPECIFIED


class Experiment(EntityPrimary):
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

    def edit(self, name=UNSPECIFIED, entry=UNSPECIFIED, started_at=UNSPECIFIED, extraParams={}):
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
        import labstep.entities.experiment.repository as experimentRepository

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
        import labstep.entities.experiment.repository as experimentRepository

        return experimentRepository.editExperiment(self, deleted_at=getTime())

    def lock(self):
        """
        Lock an Experiment. Once locked, only owners can unlock.

        Example
        -------
        ::

            my_experiment = user.getExperiment(17000)
            my_experiment.lock()
        """
        import labstep.entities.experiment.repository as experimentRepository
        return experimentRepository.editExperiment(self, extraParams={'locked_at': getTime()})

    def unlock(self):
        """
        Unlock a locked Experiment. Can only be done with owner permission.

        Example
        -------
        ::

            my_experiment = user.getExperiment(17000)
            my_experiment.lock()
            my_experiment.unlock()
        """
        import labstep.entities.experiment.repository as experimentRepository
        return experimentRepository.editExperiment(self, extraParams={'locked_at': None})

    def complete(self, date=UNSPECIFIED):
        """
        Marks an experiment as complete.

        Parameters
        ----------
        date (str)
            Optionally specify a particular datetime it was completed.
            Date format 'YYYY-MM-DD HH:MM:SS'

        Example
        -------
        ::

            my_experiment = user.getExperiment(17000)
            my_experiment.complete()
        """
        import labstep.entities.experiment.repository as experimentRepository
        return experimentRepository.editExperiment(self,
                                                   extraParams={'ended_at': handleDate(date) if date is not UNSPECIFIED else getTime()})

    def getEntry(self):
        """
        Returns a JSON document representing the entry for the experiment.

        Example
        -------
        ::

            my_experiment = user.getExperiment(17000)
            print(my_experiment.getEntry())
        """
        import labstep.generic.entity.repository as entityRepository

        if hasattr(self, 'root_experiment') is False:
            self.update()

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
        import labstep.entities.experiment.repository as experimentRepository

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
        import labstep.generic.entity.repository as entityRepository

        return entityRepository.getEntities(
            self.__user__,
            ExperimentProtocol,
            count,
            {"is_root": 0, "experiment_workflow_id": self.id},
        )

    def addChemicalReaction(
        self,
        data=UNSPECIFIED,
        extraParams={},
    ):
        """
        Add Chemical Reaction to a Labstep Experiment.

        Parameters
        ----------
        data (str)
            The data of the reaction in RXN format

        Returns
        -------
        :class:`~labstep.entities.chemicalReaction.model.ChemicalReaction`
            An object representing the new Chemical Reaction

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            chemicalReaction = experiment.addChemicalReaction(data='RXN 233')
        """
        return self.root_experiment.addChemicalReaction(
            extraParams={"data": data, **extraParams},
        )

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
        Add Data Fields to a Labstep Experiment.

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
        :class:`~labstep.entities.experimentDataField.model.ExperimentDataField`
            An object representing the new Labstep Data Field.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            dataField = experiment.addDataField("Refractive Index",
                                               value="1.73")
        """
        return self.root_experiment.addDataField(
            fieldName=fieldName,
            fieldType=fieldType,
            value=value,
            date=date,
            number=number,
            unit=unit,
            filepath=filepath,
            extraParams=extraParams,
        )

    def getDataFields(self):
        """
        Retrieve the Data Fields of a Protocol within an Experiment.

        Returns
        -------
        :class:`~labstep.entities.experimentDataField.model.ExperimentDataField`
            An array of objects representing Data Fields
            on a Protocol within an Experiment.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            dataFields = exp_protocol.getDataFields()
        """
        return self.root_experiment.getDataFields()

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
            exp_chemical_reactions = experiment.getChemicalReactions()
        """
        return self.root_experiment.getChemicalReactions()

    def getSignatures(self):
        """
        Retrieve a list of signatures added to the experiment

        Returns
        -------
        List[:class:`~labstep.entities.experimentSignature.model.ExperimentSignature`]
            List of the signatures added to the Experiment
        """
        exp = self.__user__.getExperiment(self.id)
        return EntityList(exp.signatures, ExperimentSignature, self.__user__)

    def addSignature(self, statement=UNSPECIFIED, lock=False):
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
        import labstep.generic.entity.repository as entityRepository

        params = {
            "statement": statement,
            "is_lock": int(lock),
            "experiment_workflow_id": self.id,
        }
        return entityRepository.newEntity(self.__user__, ExperimentSignature, params)

    def getSignatureRequests(self):
        """
        Returns a list of pending signature requests for the experiment.

        Returns
        -------
        List[:class:`~labstep.entities.experimentSignatureRequest.model.ExperimentSignatureRequest`]
        """
        import labstep.entities.experimentSignatureRequest.repository as experimentSignatureRequestRepository

        return experimentSignatureRequestRepository.getExperimentSignatureRequests(self.__user__, self.id)

    def requestSignature(self, user_id, message=UNSPECIFIED):
        """
        Request a signature from another user in the workspace

        Parameters
        ----------

        user_id (int)
            Id of the user you are requesting a signature from

        message (str)
            Optional message to include in signature request email

        """
        import labstep.entities.experimentSignatureRequest.repository as experimentSignatureRequestRepository

        return experimentSignatureRequestRepository.newExperimentSignatureRequest(self.__user__, self.id, user_id=user_id, message=message)

    def getInventoryFields(self):
        """
        Returns a list of the inventory fields in the Experiment.

        Returns
        -------
        List[:class:`~labstep.entities.experimentInventoryField.model.ExperimentInventoryField`]
            List of the inventory fields in an Experiment.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_inventory_fields = experiment.getInventoryFields()
            print(exp_inventory_fields[0])
        """
        return self.root_experiment.getInventoryFields()

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
        Add a new inventory field to the Experiment.

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
        return self.root_experiment.addInventoryField(name=name,
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
        Remove the experiment from a collection.

        Parameters
        ----------
        collection_id (int)
            The id of the collection to remove from

        """
        import labstep.entities.collection.repository as collectionRepository

        return collectionRepository.removeFromCollection(self, collection_id)

    def getTables(self):
        """
        Returns a list of the tables in the entry of an Experiment.

        Returns
        -------
        List[:class:`~labstep.entities.experimentTable.model.ExperimentTable`]
            List of the tables in an Experiment entry

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            tables = experiment.getTables()
        """
        return self.root_experiment.getTables()

    def addTable(self, name=UNSPECIFIED, data=UNSPECIFIED):
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
        return self.root_experiment.addTable(name=name, data=data)

    def addFile(self, filepath=UNSPECIFIED, rawData=UNSPECIFIED):
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

    def getComments(self, count=100):
        """
        Retrieve the Comments attached to this Labstep Entity.

        Returns
        -------
        List[:class:`~labstep.entities.comment.model.Comment`]
            List of the comments attached.

        Example
        -------
        ::

            entity = user.getExperiment(17000)
            comments = entity.getComments()
            comments[0].attributes()
        """
        import labstep.entities.comment.repository as commentRepository

        if hasattr(self, 'thread_ids') is False:
            self.update()

        return commentRepository.getComments(self, count, extraParams={'parent_thread_id[]': self.thread_ids})

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

    def addExperimentLink(self, experiment_id):
        """
        Link this experiment to a previous experiment.
        """
        return newExperimentLink(self.__user__, src_experiment_id=self.id, dest_experiment_id=experiment_id)

    def getExperimentLinks(self, direction='forward'):
        """
        Returns a list of experiments that the current experiment references (direction = "forward")
        or a list of experiments that reference the current experiment (direction = "backwards")

        Returns
        -------
        List[:class:`~labstep.experimentLink.ExperimentLink`]
            List of linked experiments.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            experimentLinks = experiment.getExperimentLinks(direction="backwards")
        """
        import labstep.entities.experimentLink.repository as experimentLinkRepository

        return experimentLinkRepository.getExperimentLinks(self.__user__, self.id, direction=direction)

    def export(self, path):
        """
        Export the experiment to the directory specified. 

        Parameters
        -------
        path (str)
            The path to the directory to save the experiment.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            experiment.export('/my_folder')
        """
        import labstep.entities.experiment.repository as experimentRepository

        return experimentRepository.exportExperiment(self, path)

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
