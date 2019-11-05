#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .entity import getEntity, getEntities, newEntity, editEntity
from .helpers import update, getTime, createdAtFrom, createdAtTo
from .comment import addCommentWithFile
from .tag import tag


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
    :class:`~labstep.experiment.Experiment`
        An object representing a Labstep Experiment.
    """
    return getEntity(user, Experiment, id=experiment_id)


def getExperiments(user, count=100, search_query=None,
                   created_at_from=None, created_at_to=None, tag_id=None):
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

    Returns
    -------
    List[:class:`~labstep.experiment.Experiment`]
        A list of Experiment objects.
    """
    metadata = {'search_query': search_query,
                'created_at_from': createdAtFrom(created_at_from),
                'created_at_to': createdAtTo(created_at_to),
                'tag_id': tag_id}
    return getEntities(user, Experiment, count, metadata)


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
    :class:`~labstep.experiment.Experiment`
        An object representing the new Labstep Experiment.
    """
    metadata = {'name': name,
                'description': description}
    return newEntity(user, Experiment, metadata)


def editExperiment(experiment, name=None, description=None,
                   deleted_at=None):
    """
    Edit an existing Experiment.

    Parameters
    ----------
    user (obj)
        The labstep user. Must have property 'api_key'. See 'login'.
    experiment (obj)
        The Experiment to edit.
    name (str)
        The new name of the Experiment.
    description (str)
        The new description for the Experiment.
    deleted_at (str)
        The timestamp at which the Experiment is deleted/archived.

    Returns
    -------
    :class:`~labstep.experiment.Experiment`
        An object representing the editted Experiment.
    """
    metadata = {'name': name,
                'description': description,
                'deleted_at': deleted_at}
    return editEntity(experiment, metadata)


def addProtocolToExperiment(experiment, protocol):
    """
    Add a Labstep Protocol to a Labstep Experiment.

    Parameters
    ----------
    user (obj)
        The labstep user. Must have property 'api_key'. See 'login'.
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
    data = {'experiment_workflow_id': experiment.id,
            'protocol_id': protocol.last_version['id']}
    return newEntity(experiment.__user__, SubExperiment, data)


class SubExperiment:
    __entityName__ = 'experiment'

    def __init__(self, data, user):
        self.__user__ = user
        update(self, data)


class Experiment:
    __entityName__ = 'experiment-workflow'

    def __init__(self, data, user):
        self.__user__ = user
        update(self, data)

    # functions()
    def edit(self, name=None, description=None):
        """
        Edit an existing Experiment.

        Parameters
        ----------
        name (str)
            The new name of the Experiment.
        description (str)
            The new description of the Experiment.

        Returns
        -------
        :class:`~labstep.experiment.Experiment`
            An object representing the edited Experiment.

        Example
        -------
        .. code-block::

            my_experiment = user.getExperiment(17000)
            my_experiment.edit(name='A New Experiment Name', description='This
                               is my new experiment description!')
        """
        return editExperiment(self, name, description)

    def delete(self):
        """
        Delete an existing Experiment.

        Example
        -------
        .. code-block::

            my_experiment = user.getExperiment(17000)
            my_experiment.delete()
        """
        return editExperiment(self, deleted_at=getTime())

    def addProtocol(self, protocol):
        """
        Add a Labstep Protocol to a Labstep Experiment.

        Parameters
        ----------
        protocol (obj)
            The Labstep Protocol to attach.

        Returns
        -------
        experiment_protocol
            An object representing the Protocol attached to the Experiment.

        Example
        -------
        .. code-block::

            # Get an experiment
            my_experiment = user.getExperiment(17000)

            # Get a protocol
            my_protocol = user.getProtocol(10000)

            # Attach the protocol to the experiment
            my_experiment.addProtocol(my_protocol)
        """
        return addProtocolToExperiment(self, protocol)

    def addComment(self, body, filepath=None):
        """
        Add a comment to a Labstep Experiment.

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
        .. code-block::

            my_experiment = user.getExperiment(17000)
            my_experiment.addComment(body='I am commenting!',
                                  filepath='pwd/file_to_upload.dat')
        """
        return addCommentWithFile(self, body, filepath)

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
        .. code-block::

            my_experiment = user.getExperiment(17000)
            my_experiment.addTag(name='My Tag')
        """
        tag(self, name)
        return self
