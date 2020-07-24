#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylama:ignore=E501

from .entity import Entity, getEntity, getEntities, newEntity, editEntity
from .primaryEntity import PrimaryEntity
from .comment import getComments, addCommentWithFile
from .helpers import (getTime, createdAtFrom, createdAtTo,
                      handleDate, listToClass)
from .metadata import addMetadataTo, getMetadata


def getExperiment(user, experiment_id):
    """
    Retrieve a specific Labstep Experiment.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    experiment_id (int)
        The id of the Experiment to retrieve.

    Returns
    -------
    experiment
        An object representing a Labstep Experiment.
    """
    return getEntity(user, Experiment, id=experiment_id)


def getExperiments(user, count=100, search_query=None,
                   created_at_from=None, created_at_to=None, tag_id=None,
                   extraParams={}):
    """
    Retrieve a list of a user's Experiments on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    count (int)
        The number of Experiments to retrieve.
    search_query (str)
        Search for Experiments with this 'name'.
    created_at_from (str)
        The start date of the search range, must be
        in the format of 'YYYY-MM-DD'.
    created_at_to (str)
        The end date of the search range, must be
        in the format of 'YYYY-MM-DD'.
    tag_id (int)
        The id of the Tag to retrieve.
    extraParams (dict)
        Dictionary of extra filter parameters.

    Returns
    -------
    List[:class:`~labstep.experiment.Experiment`]
        A list of Experiment objects.
    """
    params = {'search_query': search_query,
              'created_at_from': createdAtFrom(created_at_from),
              'created_at_to': createdAtTo(created_at_to),
              'tag_id': tag_id,
              **extraParams}
    return getEntities(user, Experiment, count, params)


def newExperiment(user, name, description=None, extraParams={}):
    """
    Create a new Labstep Experiment.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the Experiment.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your Experiment a name.
    description (str)
        Give your Experiment a description.

    Returns
    -------
    experiment
        An object representing the new Labstep Experiment.
    """
    params = {'name': name,
              'description': description,
              **extraParams}
    return newEntity(user, Experiment, params)


def editExperiment(experiment, name=None, description=None, started_at=None,
                   deleted_at=None, extraParams={}):
    """
    Edit an existing Experiment.

    Parameters
    ----------
    experiment (obj)
        The Experiment to edit.
    name (str)
        The new name of the Experiment.
    description (str)
        The new description for the Experiment.
    started_at (str)
        The start date of the Experiment in the format of "YYYY-MM-DD HH:MM".
    deleted_at (str)
        The timestamp at which the Experiment is deleted/archived.

    Returns
    -------
    experiment
        An object representing the edited Experiment.
    """
    params = {'name': name,
              'state': description,
              'started_at': handleDate(started_at),
              'deleted_at': deleted_at,
              **extraParams}
    return editEntity(experiment, params)


def addProtocolToExperiment(experiment, protocol):
    """
    Add a Labstep Protocol to a Labstep Experiment.

    Parameters
    ----------
    experiment (obj)
        The Labstep Experiment to attach the Protocol to.
        Must have property 'id'.
    protocol (obj)
        The Labstep Protocol to attach. Must have property 'id'.

    Returns
    -------
    experiment_protocol
        An object representing the Protocol attached to the Experiment.
    """
    params = {'experiment_workflow_id': experiment.id,
              'protocol_id': protocol.last_version['id']}
    return newEntity(experiment.__user__, ExperimentProtocol, params)


class ExperimentProtocol(Entity):
    __entityName__ = 'experiment'

    __isLegacy__ = True

    def edit(self, name=None, content_state=None, started_at=None, ended_at=None, extraParams={}):
        """
        Edit an existing ExperimentProtocol.

        Parameters
        ----------
        name (str)
            The new name of the ExperimentProtocol.
        content_state (str)
            The new content_state of the ExperimentProtocol.
        started_at (str)
            The date the ExperimentProtocol was started in the format of "YYYY-MM-DD HH:MM".
        ended_at (str)
            The date the ExperimentProtocol was finished in the format of "YYYY-MM-DD HH:MM".

        Returns
        -------
        :class:`~labstep.experiment.ExperimentProtocol`
            An object representing the edited ExperimentProtocol.

        Example
        -------
        ::

            my_experiment = user.getExperiment(17000)
            protocols = my_experiment.getProtocols()
            protocols[0].edit(name='A New Experiment Name',
                               started_at='2018-06-06 12:05')
        """
        fields = {
            'name': name,
            'content_state': content_state,
            'started_at': started_at,
            'ended_at': ended_at,
            **extraParams
        }
        return editEntity(self, fields)

    def getMaterials(self):
        """
        Returns a list of the materials in a Protocol within an Experiment.

        Returns
        -------
        List[:class:`~labstep.experiment.ExperimentMaterial`]
            List of the materials in an Experiment's Protocol.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_protocol_materials = exp_protocol.getMaterials()
            exp_protocol_materials[0].attributes()
        """
        self.update()
        materials = self.experiment_values
        return listToClass(materials, ExperimentMaterial, self.__user__)

    def addMaterial(self, name=None, amount=None, units=None, resource_id=None, resource_item_id=None,
                    extraParams={}):
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
            The id of the :class:`~labstep.resource.Resource` used.
        resource_item_id (ResourceItem)
            The id of the specific :class:`~labstep.resource.ResourceItem` used.

        Returns
        -------
        :class:`~labstep.experiment.ExperimentMaterial`
            The newly added material entity.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            resource = user.getResources(search_query='Sample A')[0]
            experiment.addMaterial(name='Sample A', amount='2', units='ml',
                                 resource_id=resource.id)
        """
        params = {'experiment_id': self.id,
                  'name': name,
                  'resource_id': resource_id,
                  'resource_item_id': resource_item_id,
                  'value': amount,
                  'units': units,
                  **extraParams}

        if params['value'] is not None:
            params['value'] = str(params['value'])

        return newEntity(self.__user__, ExperimentMaterial, params)

    def getSteps(self):
        """
        Returns a list of the steps in a Protocol within an Experiment.

        Returns
        -------
        List[:class:`~labstep.experiment.ExperimentStep`]
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
        List[:class:`~labstep.experiment.ProtocolTable`]
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
        List[:class:`~labstep.experiment.ExperimentTimer`]
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
        :class:`~labstep.metadata.Metadata`
            An array of objects representing the Labstep Data Elements on a Protocol within an Experiment.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            metadata = exp_protocol.getDataElements()
        """
        return getMetadata(self)

    def addDataElement(self, fieldName, fieldType="default",
                       value=None, date=None,
                       number=None, unit=None,
                       extraParams={}):
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

        Returns
        -------
        :class:`~labstep.metadata.Metadata`
            An object representing the new Labstep Data Element.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            experiment_protocol = experiment.getProtocols()[0]
            dataElement = experiment_protocol.addDataElement("Refractive Index",
                                               value="1.73")
        """
        return addMetadataTo(self, fieldName, fieldType, value, date,
                             number, unit,
                             extraParams=extraParams)


class ExperimentMaterial(Entity):
    __entityName__ = 'experiment-value'

    def __init__(self, data, user):
        super().__init__(data, user)
        self.amount = self.value

    def edit(self, amount=None, units=None, resource_id=None, resource_item_id=None):
        """
        Edit an existing Experiment Material.

        Parameters
        ----------
        amount (str)
            The amount of the Experiment Material.
        units (str)
            The units of the amount.
        resource_id (int)
            The :class:`~labstep.resource.Resource` of the Experiment Material.
        resource_item_id (int)
            The id of the :class:`~labstep.resource.ResourceItem` of the Experiment Material.

        Returns
        -------
        :class:`~labstep.experiment.ExperimentMaterial`
            An object representing the edited Experiment Material.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_protocol_materials = exp_protocol.getMaterials()
            exp_protocol_materials[0].edit(amount=1.7, units='ml')
        """
        params = {'value': amount,
                  'units': units,
                  'resource_id': resource_id,
                  'resource_item_id': resource_item_id
                  }

        return editEntity(self, params)


class ExperimentStep(Entity):
    __entityName__ = 'experiment-step'

    def edit(self, completed_at=None):
        """
        Edit an existing Experiment Step.

        Parameters
        ----------
        completed_at (str)
            The datetime at which the Experiment Step was completed.

        Returns
        -------
        :class:`~labstep.experiment.ExperimentStep`
            An object representing the edited Experiment Step.
        """
        params = {'ended_at': completed_at}
        return editEntity(self, params)

    def complete(self):
        """
        Mark an existing Experiment Step as 'Complete'.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_protocol_steps = exp_protocol.getSteps()
            exp_protocol_steps[0].complete()
            exp_protocol_steps[1].complete()
            exp_protocol_steps[2].complete()
        """
        return self.edit(completed_at=getTime())

    def addComment(self, body, filepath=None):
        """
        Add a comment and/or file to this step.

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
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_protocol_steps = exp_protocol.getSteps()
            exp_protocol_steps[0].addComment('This step failed')
        """
        return addCommentWithFile(self, body, filepath)

    def getComments(self, count=100):
        """
        Retrieve the Comments attached to this step.

        Parameters
        ----------

        count (int)
            The number of comments to return

        Returns
        -------
        List[:class:`~labstep.comment.Comment`]
            List of the comments attached.

        Example
        -------
        ::

           experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_protocol_steps = exp_protocol.getSteps()
            exp_protocol_steps[0].getComments()
        """
        return getComments(self, count)


class ExperimentTable(Entity):
    __entityName__ = 'experiment-table'

    def edit(self, data=None):
        """
        Edit an existing Experiment Table.

        Parameters
        ----------
        name (str)
            The name of the Experiment Table.
        data (str)
            The data of the table.

        Returns
        -------
        :class:`~labstep.experiment.ExperimentTable`
            An object representing the edited Experiment Table.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_protocol_tables = exp_protocol.getTables()
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
            exp_protocol_tables[0].edit(data=data)
        """
        params = {'data': data}
        return editEntity(self, params)


class ExperimentTimer(Entity):
    __entityName__ = 'experiment-timer'

    def edit(self, hours=None, minutes=None, seconds=None):
        """
        Edit an existing Experiment Timer.

        Parameters
        ----------
        hours (int)
            The hours of the timer.
        minutes (int)
            The minutes of the timer.
        seconds (int)
            The seconds of the timer.

        Returns
        -------
        :class:`~labstep.experiment.ExperimentTimer`
            An object representing the edited Experiment Timer.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_protocol_timers = exp_protocol.getTimers()
            exp_protocol_timers[0].edit(minutes=1, seconds=7)
        """
        fields = {}

        if hours is not None:
            fields['hours'] = hours
        if minutes is not None:
            fields['minutes'] = minutes
        if seconds is not None:
            fields['seconds'] = seconds

        return editEntity(self, fields)

    """ def start(self):
        time = getTime() + self.hours + self.minutes + self.seconds
        fields = {'ended_at': time}
        return editEntity(self, fields)

    def pause(self):
        time = getTime()
        fields = {'paused_at': time}
        return editEntity(self, fields)

    def resume(self):
        time = getTime() + self.ended_at - self.paused_at
        fields = {'ended_at': time
                  'paused_at': 'null',
                  }
        return editEntity(self, fields) """


class ExperimentSignature(Entity):
    __entityName__ = 'signature'

    def revoke(self):
        """
        Revokes the signature.

        Returns
        -------
        :class:`~labstep.experiment.ExperimentSignature`
            An object representing the revoked signature.
        """
        fields = {
            "revoked_at": getTime()
        }
        return editEntity(self, fields)


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
    __entityName__ = 'experiment-workflow'

    def __init__(self, data, user):
        super().__init__(data, user)
        self.entry = ExperimentProtocol(self.root_experiment, user)

    def edit(self, name=None, description=None, started_at=None, extraParams={}):
        """
        Edit an existing Experiment.

        Parameters
        ----------
        name (str)
            The new name of the Experiment.
        description (str)
            The new description of the Experiment.
        started_at (str)
            The start date of the Experiment in the format of "YYYY-MM-DD HH:MM".

        Returns
        -------
        :class:`~labstep.experiment.Experiment`
            An object representing the edited Experiment.

        Example
        -------
        ::

            my_experiment = user.getExperiment(17000)
            my_experiment.edit(name='A New Experiment Name',
                               description='A new description!',
                               started_at='2018-06-06 12:05')
        """
        return editExperiment(self, name, description, started_at, extraParams=extraParams)

    def delete(self):
        """
        Delete an existing Experiment.

        Example
        -------
        ::

            my_experiment = user.getExperiment(17000)
            my_experiment.delete()
        """
        return editExperiment(self, deleted_at=getTime())

    def addProtocol(self, protocol):
        """
        Add a Labstep Protocol to a Labstep Experiment.

        Parameters
        ----------
        protocol (Protocol)
            The :class:`~labstep.protocol.Protocol` to attach.

        Returns
        -------
        :class:`~labstep.protocol.Protocol`
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
        return addProtocolToExperiment(self, protocol)

    def getProtocols(self):
        """
        Retrieve the Protocols attached to this Labstep Experiment.

        Returns
        -------
        List[:class:`~labstep.experiment.ExperimentProtocol`]
            List of the Protocols attached to the Experiment.

        Example
        -------
        ::

            entity = user.getExperiment(17000)
            protocols = entity.getProtocols()
            protocols[0].attributes()
        """
        self.update()
        return listToClass(self.experiments, ExperimentProtocol, self.__user__)

    def addDataElement(self, fieldName, fieldType="default",
                       value=None, date=None,
                       number=None, unit=None,
                       extraParams={}):
        """
        Add Data Elements to a Labstep Experiment.

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
        :class:`~labstep.metadata.Metadata`
            An object representing the new Labstep Data Element.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            dataElement = experiment.addDataElement("Refractive Index",
                                               value="1.73")
        """
        return self.entry.addDataElement(fieldName=fieldName,
                                         fieldType=fieldType,
                                         value=value,
                                         date=date,
                                         number=number,
                                         unit=unit,
                                         extraParams=extraParams)

    def getDataElements(self):
        """
        Retrieve the Data Elements of a Protocol within an Experiment.

        Returns
        -------
        :class:`~labstep.metadata.Metadata`
            An array of objects representing Data Elements on a Protocol within an Experiment.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            dataElements = exp_protocol.getDataElements()
        """
        return self.entry.getDataElements()

    def getSignatures(self):
        """
        Retrieve a list of signatures added to the experiment

        Returns
        -------
        List[:class:`~labstep.experiment.ExperimentSignature`]
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
        :class:`~labstep.experiment.ExperimentSignature`
            The signature that has been added
        """
        params = {
            "statement": statement,
            "is_lock": int(lock),
            "experiment_workflow_id": self.id
        }
        return newEntity(self.__user__, ExperimentSignature, params)

    def getMaterials(self):
        """
        Returns a list of the materials in the Experiment.

        Returns
        -------
        List[:class:`~labstep.experiment.ExperimentMaterial`]
            List of the materials in an Experiment.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_materials = experiment.getMaterials()
            print(exp_materials[0])
        """
        return self.entry.getMaterials()

    def addMaterial(self, name=None, amount=None, units=None, resource_id=None, resource_item_id=None,
                    extraParams={}):
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
            The id of the :class:`~labstep.resource.Resource` used.
        resource_item_id (ResourceItem)
            The id of the specific :class:`~labstep.resource.ResourceItem` used.

        Returns
        -------
        :class:`~labstep.experiment.ExperimentMaterial`
            The newly added material entity.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            resource = user.getResources(search_query='Sample A')[0]
            experiment.addMaterial(name='Sample A', amount='2', units='ml',
                                 resource_id=resource.id)
        """

        params = {'experiment_id': self.root_experiment['id'],
                  'name': name,
                  'resource_id': resource_id,
                  'resource_item_id': resource_item_id,
                  'value': amount,
                  'units': units,
                  **extraParams}

        if params['value'] is not None:
            params['value'] = str(params['value'])

        return newEntity(self.__user__, ExperimentMaterial, params)
