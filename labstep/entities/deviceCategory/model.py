#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entityWithSharing.model import EntityWithSharing
from labstep.service.helpers import getTime
from labstep.entities.deviceTemplate.model import DeviceTemplate
from labstep.constants import UNSPECIFIED

class DeviceCategory(EntityWithSharing):
    """
    Represents a Device Category on Labstep.

    To see all attributes of the device category run
    ::
        print(my_device_category)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(my_device_category.name)
        print(my_device_category.id)
    """

    __entityName__ = "device"
    __isTemplate__ = True

    def edit(self, name=UNSPECIFIED, extraParams={}):
        """
        Edit an existing DeviceCategory.

        Parameters
        ----------
        name (str)
            The new name of the DeviceCategory.

        Returns
        -------
        :class:`~labstep.entities.deviceCategory.model.DeviceCategory`
            An object representing the edited DeviceCategory.

        Example
        -------
        ::

            my_device_category = user.getDeviceCategory(17000)
            my_device_category.edit(name='A New DeviceCategory Name')
        """
        import labstep.entities.deviceCategory.repository as deviceCategoryRepository

        return deviceCategoryRepository.editDeviceCategory(
            self, name, extraParams=extraParams
        )

    def delete(self):
        """
        Delete an existing DeviceCategory.

        Example
        -------
        ::

            my_device_category = user.getDeviceCategory(17000)
            my_device_category.delete()
        """
        import labstep.entities.deviceCategory.repository as deviceCategoryRepository

        return deviceCategoryRepository.editDeviceCategory(
            self, deleted_at=getTime()
        )

    def getDeviceTemplate(self):
        """
        Returns the metadata template for devices of this category.

        Example
        -------
        ::

            my_device_category = user.getDeviceCategory(17000)
            deviceTemplate = my_device_category.getDeviceTemplate()

            deviceTemplate.getMetadata()
            deviceTemplate.addMetadata('Vendor')
        """
        return DeviceTemplate(self.__data__, self.__user__)



    