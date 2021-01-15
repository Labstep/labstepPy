#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.resource.repository import resourceRepository


def getResource(user, resource_id):
    """
    Retrieve a specific Labstep Resource.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    resource_id (int)
        The id of the Resource to retrieve.

    Returns
    -------
    resource
        An object representing a Labstep Resource.
    """
    return resourceRepository.getResource(user, resource_id)


def getResources(user, count=100, search_query=None, tag_id=None, extraParams={}):
    """
    Retrieve a list of a user's Resources on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    count (int)
        The number of Resources to retrieve.
    search_query (str)
        Search for Resources with this 'name'.
    tag_id (int)
        The id of the Tag to retrieve.
    extraParams (dict)
        Dictionary of extra filter parameters.

    Returns
    -------
    resources
        A list of Resource objects.
    """
    return resourceRepository.getResources(
        user, count, search_query, tag_id, extraParams
    )


def newResource(user, name, extraParams={}):
    """
    Create a new Labstep Resource.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the Resource.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your Resource a name.

    Returns
    -------
    resource
        An object representing the new Labstep Resource.
    """
    return resourceRepository.newResource(user, name, extraParams)


def editResource(
    resource, name=None, deleted_at=None, resource_category_id=None, extraParams={}
):
    """
    Edit an existing Resource.

    Parameters
    ----------
    resource (obj)
        The Resource to edit.
    name (str)
        The new name of the Experiment.
    deleted_at (str)
        The timestamp at which the Resource is deleted/archived.
    resource_category_id (obj)
        The id of the ResourceCategory to add to a Resource.

    Returns
    -------
    resource
        An object representing the edited Resource.
    """
    return resourceRepository.editResource(
        resource, name, deleted_at, resource_category_id, extraParams
    )
