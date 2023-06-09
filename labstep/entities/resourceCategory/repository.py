#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.resourceCategory.model import ResourceCategory
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


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
    return entityRepository.getEntity(user, ResourceCategory, id=resourceCategory_id)


def getResourceCategorys(
        user, count=UNSPECIFIED, search_query=UNSPECIFIED, tag_id=UNSPECIFIED, extraParams={}
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
    filterParams = {"search_query": search_query, "tag_id": tag_id}
    params = {**filterParams, **extraParams, "is_template": 1}
    return entityRepository.getEntities(user, ResourceCategory, count, params)


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
    params = {"name": name, **extraParams, "is_template": 1}
    return entityRepository.newEntity(user, ResourceCategory, params)


def editResourceCategory(
        resourceCategory, name=UNSPECIFIED, deleted_at=UNSPECIFIED, extraParams={}
):
    params = {"name": name, "deleted_at": deleted_at, **extraParams}
    return entityRepository.editEntity(resourceCategory, params)
