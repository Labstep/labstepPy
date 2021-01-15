#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.resourceLocation.repository import resourceLocationRepository


def getResourceLocation(user, resource_location_id):
    """
    Retrieve a specific Labstep ResourceLocation.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    resource_location_id (int)
        The id of the ResourceLocation to retrieve.

    Returns
    -------
    ResourceLocation
        An object representing a Labstep ResourceLocation.
    """
    return resourceLocationRepository.getResourceLocation(user, resource_location_id)


def getResourceLocations(
    user, count=100, search_query=None, tag_id=None, extraParams={}
):
    """
    Retrieve a list of a user's ResourceLocations on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    count (int)
        The number of ResourceLocations to retrieve.
    search_query (str)
        Search for ResourceLocations with this 'name'.
    tag_id (int)
        The id of the Tag to retrieve.

    Returns
    -------
    ResourceLocations
        A list of ResourceLocation objects.
    """
    return resourceLocationRepository.getResourceLocations(
        user, count, search_query, tag_id, extraParams
    )


def newResourceLocation(user, name, outer_location_id=None, extraParams={}):
    """
    Create a new Labstep ResourceLocation.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the ResourceLocation.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your ResourceLocation a name.

    outer_location_id (int)
        Id of existing location to create the location within

    Returns
    -------
    ResourceLocation
        An object representing the new Labstep ResourceLocation.
    """
    return resourceLocationRepository.newResourceLocation(
        user, name, outer_location_id, extraParams
    )


def editResourceLocation(resourceLocation, name, extraParams={}):
    """
    Edit an existing ResourceLocation.

    Parameters
    ----------
    resourceLocation (obj)
        The ResourceLocation to edit.
    name (str)
        The new name of the ResourceLocation.
    deleted_at (str)
        The timestamp at which the ResourceLocation is deleted/archived.

    Returns
    -------
    ResourceLocation
        An object representing the edited ResourceLocation.
    """
    return resourceLocationRepository.editResourceLocation(
        resourceLocation, name, extraParams
    )
