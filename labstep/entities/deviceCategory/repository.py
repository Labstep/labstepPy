#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.deviceCategory.model import DeviceCategory
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def getDeviceCategory(user, deviceCategory_id):
    """
    Retrieve a specific Labstep DeviceCategory.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    deviceCategory_id (int)
        The id of the ResourceCategory to retrieve.

    Returns
    -------
    DeviceCategory
        An object representing a Labstep DeviceCategory.
    """
    return entityRepository.getEntity(user, DeviceCategory, id=deviceCategory_id)


def getDeviceCategorys(
        user, count=UNSPECIFIED, search_query=UNSPECIFIED, tag_id=UNSPECIFIED, extraParams={}
):
    """
    Retrieve a list of a user's DeviceCategorys on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    count (int)
        The number of DeviceCategorys to retrieve.
    search_query (str)
        Search for DeviceCategorys with this 'name'.
    tag_id (int)
        The id of the Tag to retrieve.

    Returns
    -------
    ResourceCategorys
        A list of DeviceCategory objects.
    """
    filterParams = {"search_query": search_query, "tag_id": tag_id}
    params = {**filterParams, **extraParams, "is_template": 1}
    return entityRepository.getEntities(user, DeviceCategory, count, params)


def newDeviceCategory(user, name, extraParams={}):
    """
    Create a new Labstep DeviceCategory.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the DeviceCategory.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your DeviceCategory a name.

    Returns
    -------
    ResourceCategory
        An object representing the new Labstep DeviceCategory.
    """
    params = {"name": name, **extraParams, "is_template": 1}
    return entityRepository.newEntity(user, DeviceCategory, params)


def editDeviceCategory(
        deviceCategory, name=UNSPECIFIED, deleted_at=UNSPECIFIED, extraParams={}
):
    params = {"name": name, "deleted_at": deleted_at, **extraParams}
    return entityRepository.editEntity(deviceCategory, params)