#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylama:ignore=E501

from .entity import Entity, getEntity, getEntities, newEntity, editEntity
from .helpers import (getTime, createdAtFrom, createdAtTo,
                      handleDate, listToClass)
from .comment import addCommentWithFile, getComments
from .tag import tag, getAttachedTags


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
    filterParams = {'search_query': search_query,
                    'created_at_from': createdAtFrom(created_at_from),
                    'created_at_to': createdAtTo(created_at_to),
                    'tag_id': tag_id}
    params = {**filterParams, **extraParams}
    return getEntities(user, Experiment, count, params)


def newExperiment(user, name, description=None):
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
    fields = {'name': name,
              'description': description}
    return newEntity(user, Experiment, fields)


def editExperiment(experiment, name=None, description=None, started_at=None,
                   deleted_at=None):
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
    fields = {'name': name,
              'description': description,
              'started_at': handleDate(started_at),
              'deleted_at': deleted_at
              }
    return editEntity(experiment, fields)


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
    fields = {'experiment_workflow_id': experiment.id,
              'protocol_id': protocol.last_version['id']}
    return newEntity(experiment.__user__, ExperimentProtocol, fields)


class ExperimentProtocol(Entity):
    __entityName__ = 'experiment'

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
        materials = self.experiment_values
        return listToClass(materials, ExperimentMaterial, self.__user__)

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
        timers = self.experiment_timers
        return listToClass(timers, ExperimentTimer, self.__user__)


class ExperimentMaterial(Entity):
    __entityName__ = 'experiment-value'

    def edit(self, amount=None, units=None, resource=None, resourceItem=None):
        """
        Edit an existing Experiment Material.

        Parameters
        ----------
        amount (str)
            The amount of the Experiment Material.
        units (str)
            The units of the amount.
        resource (Resource)
            The :class:`~labstep.resource.Resource` of the Experiment Material.
        resourceItem (ResourceItem)
            The :class:`~labstep.resource.ResourceItem` of the Experiment Material.

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
        fields = {'value': amount,
                  'units': units}
        if resource is not None:
            fields['resource_id'] = resource.id
        if resourceItem is not None:
            fields['resource_item_id'] = resourceItem.id

        return editEntity(self, fields)


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
        fields = {'ended_at': completed_at}
        return editEntity(self, fields)

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
        fields = {'data': data}
        return editEntity(self, fields)


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


class Experiment(Entity):
    __entityName__ = 'experiment-workflow'

    def edit(self, name=None, description=None, started_at=None):
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
        return editExperiment(self, name, description, started_at)

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
        return list(map(lambda x: getEntity(self.__user__, ExperimentProtocol, x['id'], isDeleted=None), self.experiments))

    def addComment(self, body, filepath=None):
        """
        Add a comment and/or file to a Labstep Experiment.

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

            my_experiment = user.getExperiment(17000)
            my_experiment.addComment(body='I am commenting!',
                                     filepath='pwd/file_to_upload.dat')
        """
        return addCommentWithFile(self, body, filepath)

    def getComments(self, count=100):
        """
        Retrieve the Comments attached to this Labstep Entity.

        Returns
        -------
        List[:class:`~labstep.comment.Comment`]
            List of the comments attached.

        Example
        -------
        ::

            entity = user.getExperiment(17000)
            comments = entity.getComments()
            comments[0].attributes()
        """
        return getComments(self, count)

    def addTag(self, name):
        """
        Add a tag to the Experiment (creates a
        new tag if none exists).

        Parameters
        ----------
        name (str)
            The name of the tag to create.

        Returns
        -------
        :class:`~labstep.experiment.Experiment`
            The Experiment that was tagged.

        Example
        -------
        ::

            my_experiment = user.getExperiment(17000)
            my_experiment.addTag(name='My Tag')
        """
        tag(self, name)
        return self

    def getTags(self):
        """
        Retrieve the Tags attached to a this Labstep Entity.

        Returns
        -------
        List[:class:`~labstep.tag.Tag`]
            List of the tags attached.

        Example
        -------
        ::

            entity = user.getExperiment(17000)
            tags = entity.getTags()
            tags[0].attributes()
        """
        return getAttachedTags(self)
