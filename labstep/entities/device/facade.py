#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.device.repository import deviceRepository


def getDevice(user, device_id):
    """
    Retrieve a specific Labstep Device.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    device_id (int)
        The id of the Device to retrieve.

    Returns
    -------
    device
        An object representing a Labstep Device.
    """
    return deviceRepository.getDevice(user, device_id)


def getDevices(user, count=100, search_query=None, extraParams={}):
    """
    Retrieve a list of a user's Devices on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    count (int)
        The number of Devices to retrieve.
    search_query (str)
        Search for Devices with this 'name'.
    extraParams (dict)
        Dictionary of extra filter parameters.

    Returns
    -------
    devices
        A list of Device objects.
    """
    return deviceRepository.getDevices(user, count, search_query, extraParams)


def newDevice(user, name, extraParams={}):
    """
    Create a new Labstep Device.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the Device.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your Device a name.

    Returns
    -------
    device
        An object representing the new Labstep Device.
    """
    return deviceRepository.newDevice(user, name, extraParams)


def editDevice(device, name=None, deleted_at=None, extraParams={}):
    """
    Edit an existing Device.

    Parameters
    ----------
    device (obj)
        The Device to edit.
    name (str)
        The new name of the Experiment.
    deleted_at (str)
        The timestamp at which the Device is deleted/archived.
    device_category_id (obj)
        The id of the DeviceCategory to add to a Device.

    Returns
    -------
    device
        An object representing the edited Device.
    """
    return deviceRepository.editDevice(device, name, deleted_at, extraParams)
