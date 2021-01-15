#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.experiment.repository import experimentRepository


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
    return experimentRepository.getExperiment(user, experiment_id)


def getExperiments(
    user,
    count=100,
    search_query=None,
    created_at_from=None,
    created_at_to=None,
    tag_id=None,
    collection_id=None,
    extraParams={},
):
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
        Search for Experiments containing this string in the name or entry.
    created_at_from (str)
        The start date of the search range, must be
        in the format of 'YYYY-MM-DD'.
    created_at_to (str)
        The end date of the search range, must be
        in the format of 'YYYY-MM-DD'.
    tag_id (int)
        Get experiments tagged with this tag.
    collection_id (int)
        Get experiments in this collection.
    extraParams (dict)
        Dictionary of extra filter parameters.

    Returns
    -------
    List[:class:`~labstep.experiment.Experiment`]
        A list of Experiment objects.
    """
    return experimentRepository.getExperiments(
        user,
        count,
        search_query,
        created_at_from,
        created_at_to,
        tag_id,
        collection_id,
        extraParams,
    )


def newExperiment(user, name, entry=None, extraParams={}):
    """
    Create a new Labstep Experiment.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the Experiment.
        Must have property 'api_key'. See 'login'.
    name (str)
        The name of the experiment.
    entry (obj)
        A JSON object representing the state of the Experiment Entry.

    Returns
    -------
    experiment
        An object representing the new Labstep Experiment.
    """
    return experimentRepository.newExperiment(user, name, entry, extraParams)


def editExperiment(
    experiment, name=None, entry=None, started_at=None, deleted_at=None, extraParams={}
):
    """
    Edit an existing Experiment.

    Parameters
    ----------
    experiment (obj)
        The Experiment to edit.
    name (str)
        The new name of the Experiment.
    entry (obj)
        A JSON object representing the state of the Experiment Entry.
    started_at (str)
        The start date of the Experiment in the format of "YYYY-MM-DD HH:MM".
    deleted_at (str)
        The timestamp at which the Experiment is deleted/archived.

    Returns
    -------
    experiment
        An object representing the edited Experiment.
    """
    return experimentRepository.editExperiment(
        experiment, name, entry, started_at, deleted_at, extraParams
    )


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
    return experimentRepository.addProtocolToExperiment(experiment, protocol)
