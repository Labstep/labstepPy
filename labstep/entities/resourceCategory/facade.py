#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.resourceCategory.repository import resourceCategoryRepository


def getResourceCategory(user, resourceCategory_id):
    """
    Retrieve a specific Labstep ResourceCategory.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    resourceCategory_id (int)
        The id of the ResourceCategory to retrieve.

    Returns
    -------
    ResourceCategory
        An object representing a Labstep ResourceCategory.
    """
    return resourceCategoryRepository.getResourceCategory(user, resourceCategory_id)


def getResourceCategorys(
    user, count=100, search_query=None, tag_id=None, extraParams={}
):
    """
    Retrieve a list of a user's ResourceCategorys on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    count (int)
        The number of ResourceCategorys to retrieve.
    search_query (str)
        Search for ResourceCategorys with this 'name'.
    tag_id (int)
        The id of the Tag to retrieve.

    Returns
    -------
    ResourceCategorys
        A list of ResourceCategory objects.
    """
    return resourceCategoryRepository.getResourceCategorys(
        user, count, search_query, tag_id, extraParams
    )


def newResourceCategory(user, name, extraParams={}):
    """
    Create a new Labstep ResourceCategory.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the ResourceCategory.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your ResourceCategory a name.

    Returns
    -------
    ResourceCategory
        An object representing the new Labstep ResourceCategory.
    """
    return resourceCategoryRepository.newResourceCategory(user, name, extraParams)


def editResourceCategory(resourceCategory, name=None, deleted_at=None, extraParams={}):
    """
    Edit an existing ResourceCategory.

    Parameters
    ----------
    resourceCategory (obj)
        The ResourceCategory to edit.
    name (str)
        The new name of the ResourceCategory.
    deleted_at (str)
        The timestamp at which the ResourceCategory is deleted/archived.

    Returns
    -------
    ResourceCategory
        An object representing the edited ResourceCategory.
    """
    return resourceCategoryRepository.editResourceCategory(
        resourceCategory, name, deleted_at, extraParams
    )
