#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.deviceData.model import DeviceData
from labstep.generic.entityWithMetadata.model import EntityWithMetadata
from labstep.generic.entityWithSharing.model import EntityWithSharing
from labstep.generic.entityWithComments.model import EntityWithComments
from labstep.generic.entityWithAssign.model import EntityWithAssign
from labstep.service.helpers import getTime, handleDate
from labstep.constants import UNSPECIFIED


TYPE_DEFAULT = "default"
TYPE_NUMERIC = "numeric"
TYPE_FILE = "file"

FIELD_TYPES = {
    "text": TYPE_DEFAULT,
    "numeric": TYPE_NUMERIC,
    "file": TYPE_FILE,
}

ALLOWED_FIELDS = {
    TYPE_DEFAULT: [
        "value",
    ],
    TYPE_NUMERIC: [
        "number",
        "unit",
    ],
    TYPE_FILE: [
        "file_id",
    ],
}


class Device(EntityWithSharing, EntityWithMetadata, EntityWithComments, EntityWithAssign):
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

    __entityName__ = "device"

    def edit(self, name=UNSPECIFIED, extraParams={}):
        """
        Edit an existing Device.

        Parameters
        ----------
        name (str)
            The new name of the Device.

        Returns
        -------
        :class:`~labstep.entities.device.model.Device`
            An object representing the edited Device.

        Example
        -------
        ::

            my_device = user.getDevice(17000)
            my_device.edit(name='A New Device Name')
        """
        import labstep.entities.device.repository as deviceRepository

        return deviceRepository.editDevice(self, name, extraParams=extraParams)

    def delete(self):
        """
        Delete an existing Device.

        Example
        -------
        ::

            my_device = user.getDevice(17000)
            my_device.delete()
        """
        import labstep.entities.device.repository as deviceRepository

        return deviceRepository.editDevice(self, deleted_at=getTime())

    def addMetadata(
        self,
        fieldName,
        fieldType="default",
        value=UNSPECIFIED,
        date=UNSPECIFIED,
        number=UNSPECIFIED,
        unit=UNSPECIFIED,
        filepath=UNSPECIFIED,
        extraParams={},
    ):
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
        :class:`~labstep.entities.metadata.model.Metadata`
            An object representing the new Labstep Metadata.

        Example
        -------
        ::

            device = user.getDevice(17000)
            metadata = device.addMetadata("Refractive Index",
                                               value="1.73")
        """
        import labstep.entities.metadata.repository as metadataRepository

        return metadataRepository.addMetadataTo(
            self,
            fieldName=fieldName,
            fieldType=fieldType,
            value=value,
            date=date,
            number=number,
            unit=unit,
            filepath=filepath,
            extraParams=extraParams,
        )

    def getMetadata(self):
        """
        Retrieve the Metadata of a Labstep Device.

        Returns
        -------
        :class:`~labstep.entities.metadata.model.Metadata`
            An array of Metadata objects for the Device.

        Example
        -------
        ::

            my_device = user.getDevice(17000)
            metadatas = my_device.getMetadata()
            metadatas[0].attributes()
        """
        import labstep.entities.metadata.repository as metadataRepository

        return metadataRepository.getMetadata(self)

    def getData(self, count=100, search_query=UNSPECIFIED, extraParams={}):
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
        from labstep.generic.entity.repository import getEntities

        params = {"search_query": search_query,
                  "device_id": self.id, **extraParams}
        return getEntities(self.__user__, DeviceData, count, params)

    def addData(
        self,
        fieldName,
        fieldType="text",
        text=UNSPECIFIED,
        number=UNSPECIFIED,
        unit=UNSPECIFIED,
        filepath=UNSPECIFIED,
        extraParams={},
    ):
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
        :class:`~labstep.entities.device.model.DeviceData`
            An object representing the new Device Data.

        Example
        -------
        ::

            device = user.getDevice(17000)
            data = device.addData("Temperature","numeric",
                                               number=173, unit='K')
        """
        from labstep.generic.entity.repository import newEntity
        from labstep.entities.file.repository import newFile

        if fieldType not in FIELD_TYPES:
            msg = "Not a supported data type '{}'".format(fieldType)
            raise ValueError(msg)

        if filepath is not UNSPECIFIED:
            file_id = newFile(self.__user__, filepath).id
        else:
            file_id = UNSPECIFIED

        allowedFieldsForType = set(ALLOWED_FIELDS[FIELD_TYPES[fieldType]])
        fields = {"value": text, "number": number,
                  "unit": unit, "file_id": file_id}
        fields = {k: v for k, v in fields.items() if v is not UNSPECIFIED}
        fields = set(fields.keys())
        violations = fields - allowedFieldsForType
        if violations:
            msg = "Unallowed fields [{}] for type {}".format(
                ",".join(violations), fieldType
            )
            raise ValueError(msg)

        params = {
            "device_id": self.id,
            "type": FIELD_TYPES[fieldType],
            "name": fieldName,
            "value": text,
            "number": number,
            "unit": unit,
            "file_id": file_id,
            **extraParams,
        }

        return newEntity(self.__user__, DeviceData, params)

    def setDeviceCategory(self, device_category_id, extraParams={}):
        """
        Sets the Category for the Device

        Parameters
        ----------
        device_category_id (int)
            The id of :class:`~labstep.entities.deviceCategory.model.DeviceCategory`
            to set for
            the device.

        Returns
        -------
        :class:`~labstep.entities.device.model.Device`
            An object representing the Device on Labstep.

        Example
        -------
        ::

            # Get a DeviceCategory
            device_category = user.getDeviceCategory(170)

            # Set the Device Category
            my_device = my_resource.setDeviceCategory(device_category.id)
        """
        import labstep.entities.device.repository as deviceRepository

        return deviceRepository.editDevice(
            self, device_category_id=device_category_id, extraParams=extraParams
        )

    def getDeviceCategory(self):
        """
        Get the DeviceCategory of the Device.

        Returns
        -------
        :class:`~labstep.entities.deviceCategory.model.DeviceCategory`
            An object representing the Device Category on Labstep.

        Example
        -------
        ::

            # Get a Device
            device = user.getDevice(170)

            # Get the Device Category of the Device
            deviceCategory = device.getDeviceCategory()
        """

        if self.template is None:
            return None

        import labstep.entities.deviceCategory.repository as deviceCategoryRepository

        return deviceCategoryRepository.getDeviceCategory(
            self.__user__, self.template["id"]
        )

    def addDeviceBooking(
        self,
        started_at,
        ended_at,
        description=UNSPECIFIED,
        extraParams={},
    ):
        """
        Add a new DeviceBooking to a Device.

        Parameters
        ----------
        started_at (str)
            The new start date of the DeviceBooking
            in the format of "YYYY-MM-DD HH:MM".

        ended_at (str)
            The new finish date of the DeviceBooking
            in the format of "YYYY-MM-DD HH:MM".

        description (str)
            A description of what the booking is for.

        Returns
        -------
        :class:`~labstep.entities.deviceBooking.model.DeviceBooking`
            An object representing the new Labstep DeviceBooking.

        Example
        -------
        ::

            device = user.getDevice(17000)
            device_booking = device.addDeviceBooking(started_at='2025-08-20 00:00',ended_at='2025-08-22 00:00')
        """
        import labstep.entities.deviceBooking.repository as deviceBookingRepository

        return deviceBookingRepository.newDeviceBooking(self.__user__,
                                                        self,
                                                        ended_at=handleDate(
                                                            ended_at),
                                                        started_at=handleDate(
                                                            started_at),
                                                        description=description,
                                                        extraParams=extraParams)

    def getDeviceBooking(self, deviceBooking_id):
        """
        Get an specific DeviceBooking of the Device.

        Returns
        -------
        :class:`~labstep.entities.deviceBooking.model.DeviceBooking`
            An object representing the Device Booking on Labstep.

        Example
        -------
        ::

            # Get a Device
            device = user.getDevice(170)

            # Get the Device Booking of the Device
            deviceBooking = device.getDeviceBooking(1200)
        """
        import labstep.entities.deviceBooking.repository as deviceBookingRepository

        return deviceBookingRepository.getDeviceBooking(self.__user__, self.id, deviceBooking_id=deviceBooking_id)

    def getDeviceBookings(self, count=UNSPECIFIED, extraParams={}):
        """
        Get the DeviceBookings of the Device.

        Returns
        -------
        List[:class:`~labstep.entities.deviceBooking.model.DeviceBooking`]
            List of the DeviceBookings attached to the Device.

        Example
        -------
        ::

            # Get a Device
            device = user.getDevice(170)

            # Get the Device Booking of the Device
            deviceBookings = device.getDeviceBookings()
        """
        import labstep.entities.deviceBooking.repository as deviceBookingRepository

        return deviceBookingRepository.getDeviceBookings(self.__user__, self.id, count=count, extraParams=extraParams)
