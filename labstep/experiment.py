#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .entity import getEntity, getEntities, newEntity, editEntity
from .helpers import getTime, createdAtFrom, createdAtTo, update
from .comment import addCommentWithFile
from .tag import tag

experimentEntityName = 'experiment-workflow'


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
    return getEntity(user, experimentEntityName, id=experiment_id)


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
    experiment
        A list of Experiment objects.
    """
    metadata = {'search_query': search_query,
                'created_at_from': createdAtFrom(created_at_from),
                'created_at_to': createdAtTo(created_at_to),
                'tag_id': tag_id}
    return getEntities(user, experimentEntityName, count, metadata)


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
    metadata = {'name': name,
                'description': description}
    return newEntity(user, experimentEntityName, metadata)


def editExperiment(user, experiment, name=None, description=None,
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
    experiment
        An object representing the editted Experiment.
    """
    metadata = {'name': name,
                'description': description,
                'deleted_at': deleted_at}
    return editEntity(user, experimentEntityName, experiment.id, metadata)


def addProtocolToExperiment(user, experiment, protocol):
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
            'protocol_id': protocol['last_version']['id']}
    return newEntity(user, 'experiment', data)


class Experiment:
    def __init__(self, data, user):
        self.__user__ = user
        self.__entityName__ = experimentEntityName
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

        Example
        -------
        .. code-block::

            my_experiment = LS.Experiment(user.getExperiment(17000), user)
            my_experiment.edit(name='A New Experiment Name', description='This
                               is my new experiment description!')
        """
        newData = editExperiment(self.__user__, self, name, description)
        return update(self, newData)

    def delete(self):
        """
        Delete an existing Experiment.

        Example
        -------
        .. code-block::

            my_experiment = LS.Experiment(user.getExperiment(17000), user)
            my_experiment.delete()
        """
        return editExperiment(self.__user__, self, deleted_at=getTime())

    def addProtocol(self, protocol):
        """
        Add a Labstep Protocol to a Labstep Experiment.

        Parameters
        ----------
        protocol (obj)
            The Labstep Protocol to attach.

        Example
        -------
        .. code-block::

            # Get an experiment
            my_experiment = LS.Experiment(user.getExperiment(17000), user)

            # Get a protocol
            my_protocol = user.getProtocol(10000)

            # Attach the protocol to the experiment
            my_experiment.addProtocol(my_protocol)
        """
        return addProtocolToExperiment(self.__user__, self, protocol)

    def comment(self, body, filepath=None):
        """
        Add a comment to a Labstep Experiment.

        Parameters
        ----------
        body (str)
            The body of the comment.
        filepath (str)
            A Labstep File entity to attach to the comment,
            including the filepath.

        Example
        -------
        .. code-block::

            my_experiment = LS.Experiment(user.getExperiment(17000), user)
            my_experiment.comment(body='I am commenting!',
                                  filepath='pwd/file_to_upload.dat')
        """
        return addCommentWithFile(self.__user__, self, body, filepath)

    def addTag(self, name):
        """
        Add a tag to the Experiment (creates a
        new tag if none exists).

        Parameters
        ----------
        name (str)
            The name of the tag to create.

        Example
        -------
        .. code-block::

            my_experiment = LS.Experiment(user.getExperiment(17000), user)
            my_experiment.addTag(name='My Tag')
        """
        return tag(self.__user__, self, name)
