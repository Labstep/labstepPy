#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .primaryEntity import ShareableEntity
from .entity import Entity, getEntity, getEntities, newEntity, editEntity
from .helpers import getTime
from .metadata import addMetadataTo, getMetadata
from .file import newFile

TYPE_DEFAULT = 'default'
TYPE_NUMERIC = 'numeric'
TYPE_FILE = 'file'

FIELDS = [
    TYPE_DEFAULT,
    TYPE_NUMERIC,
    TYPE_FILE,
]

ALLOWED_FIELDS = {
    TYPE_DEFAULT: [
        'value',
    ],
    TYPE_NUMERIC: [
        'number',
        'unit',
    ],
    TYPE_FILE: [
        'file_id',
    ]
}


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
    return getEntity(user, Device, id=device_id)


def getDevices(user, count=100, search_query=None,
               extraParams={}):
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
    params = {'search_query': search_query,
              **extraParams}
    return getEntities(user, Device, count, params)


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
    params = {'name': name, **extraParams}
    return newEntity(user, Device, params)


def editDevice(device, name=None, deleted_at=None,
               extraParams={}):
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
    params = {'name': name,
              'deleted_at': deleted_at,
              **extraParams}
    return editEntity(device, params)


class Device(ShareableEntity):
    """
    Represents a Device on Labstep.

    To see all attributes of the device run
    ::
        print(my_device)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(my_device.name)
        print(my_device.id)
    """
    __entityName__ = 'device'

    def edit(self, name=None, extraParams={}):
        """
        Edit an existing Device.

        Parameters
        ----------
        name (str)
            The new name of the Device.

        Returns
        -------
        :class:`~labstep.device.Device`
            An object representing the edited Device.

        Example
        -------
        ::

            my_device = user.getDevice(17000)
            my_device.edit(name='A New Device Name')
        """
        return editDevice(self, name, extraParams=extraParams)

    def delete(self):
        """
        Delete an existing Device.

        Example
        -------
        ::

            my_device = user.getDevice(17000)
            my_device.delete()
        """
        return editDevice(self, deleted_at=getTime())

    def addMetadata(self, fieldName, fieldType="default",
                    value=None, date=None,
                    number=None, unit=None,
                    filepath=None,
                    extraParams={}):
        """
        Add Metadata to a Device.

        Parameters
        ----------
        fieldName (str)
            The name of the field.
        fieldType (str)
            The Metadata field type. Options are: "default", "date",
            "numeric", or "file". The "default" type is "Text".
        value (str)
            The value accompanying the fieldName entry.
        date (str)
            The date accompanying the fieldName entry. Must be
            in the format of "YYYY-MM-DD HH:MM".
        number (float)
            The numeric value.
        unit (str)
            The unit accompanying the number entry.
        filepath (str)
            Local path to the file to upload for type 'file'

        Returns
        -------
        :class:`~labstep.metadata.Metadata`
            An object representing the new Labstep Metadata.

        Example
        -------
        ::

            device = user.getDevice(17000)
            metadata = device.addMetadata("Refractive Index",
                                               value="1.73")
        """
        return addMetadataTo(self,
                             fieldName=fieldName,
                             fieldType=fieldType,
                             value=value, date=date,
                             number=number, unit=unit,
                             filepath=filepath,
                             extraParams=extraParams)

    def getMetadata(self):
        """
        Retrieve the Metadata of a Labstep Device.

        Returns
        -------
        :class:`~labstep.metadata.Metadata`
            An array of Metadata objects for the Device.

        Example
        -------
        ::

            my_device = user.getDevice(17000)
            metadatas = my_device.getMetadata()
            metadatas[0].attributes()
        """
        return getMetadata(self)

    def getData(self, count=100, search_query=None,
                extraParams={}):
        """
        Retrieve a list of the data sent by an device.

        Parameters
        ----------
        count (int)
            The total count of data points to return.
        search_query (str)
            Search for data points by name.
        extraParams (dict)
            Dictionary of extra filter parameters.

        Returns
        -------
        DeviceData
            A list of DeviceData objects.
        """
        params = {'search_query': search_query,
                  'device_id': self.id,
                  **extraParams}
        return getEntities(self.__user__, DeviceData, count, params)

    def addData(self, fieldName, fieldType="text",
                text=None,
                number=None, unit=None,
                filepath=None,
                extraParams={}):
        """
        Send new data from the Device.

        Parameters
        ----------
        fieldName (str)
            The name of the data field being sent.
        fieldType (str)
            The type of data being sent. Options are: "text", "numeric",
            or "file".
        text (str)
            The text for a field of type 'text'.
        number (float)
            The number for a field of type 'numeric'.
        unit (str)
            The unit for a field of type 'numeric'.
        filepath (str)
            Local path to the file to upload for type 'file'.

        Returns
        -------
        :class:`~labstep.device.DeviceData`
            An object representing the new Device Data.

        Example
        -------
        ::

            device = user.getDevice(17000)
            data = device.addData("Temperature","numeric",
                                               number=173, unit='K')
        """
        if fieldType not in FIELDS:
            msg = "Not a supported data type '{}'".format(fieldType)
            raise ValueError(msg)

        if filepath is not None:
            file_id = newFile(self.__user__, filepath).id
        else:
            file_id = None

        allowedFieldsForType = set(ALLOWED_FIELDS[fieldType])
        fields = {
            'value': text,
            'number': number,
            'unit': unit,
            'file_id': file_id
        }
        fields = {k: v for k, v in fields.items() if v}
        fields = set(fields.keys())
        violations = fields - allowedFieldsForType
        if violations:
            msg = 'Unallowed fields [{}] for type {}'.format(
                ",".join(violations), fieldType)
            raise ValueError(msg)

        params = {'device_id': self.id,
                  'type': fieldType,
                  'name': fieldName,
                  'value': text,
                  'number': number,
                  'unit': unit,
                  'file_id': file_id,
                  **extraParams}

        return newEntity(self.__user__, DeviceData, params)


class DeviceData(Entity):
    __entityName__ = 'device-data'

    def delete(self):
        """
        Delete a DeviceData.

        Example
        -------
        ::

            deviceData.delete()
        """
        return editEntity(self, fields={'deleted_at': getTime()})
