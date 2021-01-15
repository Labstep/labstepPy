#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.resourceItem.repository import resourceItemRepository


def getResourceItem(user, resourceItem_id):
    """
    Retrieve a specific Labstep ResourceItem.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    resourceItem_id (int)
        The id of the ResourceItem to retrieve.

    Returns
    -------
    ResourceItem
        An object representing a Labstep ResourceItem.
    """
    return resourceItemRepository.getResourceItem(user, resourceItem_id)


def getResourceItems(user, resource_id, count=100, search_query=None, extraParams={}):
    """
    Retrieve a list of a user's ResourceItems on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    resource_id (obj)
        The id of Resource to retrieve the ResourceItems for.
    count (int)
        The number of ResourceItems to retrieve.
    search_query (str)
        Search for ResourceItems with this 'name'.
    extraParams (dict)
        Dictionary of extra filter parameters.

    Returns
    -------
    ResourceItems
        A list of ResourceItem objects.
    """
    return resourceItemRepository.getResourceItems(
        user, resource_id, count, search_query, extraParams
    )


def newResourceItem(
    user,
    resource_id,
    name=None,
    availability=None,
    quantity_amount=None,
    quantity_unit=None,
    resource_location_id=None,
    extraParams={},
):
    """
    Create a new Labstep ResourceItem.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the ResourceItem.
        Must have property 'api_key'. See 'login'.
    resource_id (int)
        The id of the Resource to add a new ResourceItem to.
    name (str)
        The new name of the ResourceItem.
    availability (str)
        The status of the ResourceItem. Options are:
        "available" and "unavailable".
    quantity_amount (float)
        The quantity of the ResourceItem.
    quantity_unit (str)
        The unit of the quantity.
    resource_location_id (int)
        The id of the ResourceLocation of the ResourceItem.

    Returns
    -------
    resource
        An object representing the new Labstep ResourceItem.
    """
    return resourceItemRepository.newResourceItem(
        user,
        resource_id,
        name,
        availability,
        quantity_amount,
        quantity_unit,
        resource_location_id,
        extraParams,
    )


def editResourceItem(
    resourceItem,
    name=None,
    availability=None,
    quantity_amount=None,
    quantity_unit=None,
    resource_location_id=None,
    deleted_at=None,
    extraParams={},
):
    """
    Edit an existing ResourceItem.

    Parameters
    ----------
    resourceItem (obj)
        The ResourceItem to edit.
    name (str)
        The new name of the ResourceItem.
    availability (str)
        The status of the ResourceItem. Options are:
        "available" and "unavailable".
    quantity_amount (float)
        The quantity of the ResourceItem.
    quantity_unit (str)
        The unit of the quantity.
    location_id (int)
        The id of the ResourceLocation for the ResourceItem.
    deleted_at (str)
        The timestamp at which the ResourceItem is deleted/archived.

    Returns
    -------
    ResourceItem
        An object representing the edited ResourceItem.
    """
    return resourceItemRepository.editResourceItem(
        resourceItem,
        name,
        availability,
        quantity_amount,
        quantity_unit,
        resource_location_id,
        deleted_at,
        extraParams,
    )
