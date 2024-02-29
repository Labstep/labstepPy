#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.service.helpers import getTime
from labstep.entities.deviceTemplate.model import DeviceTemplate
from labstep.constants import UNSPECIFIED
from labstep.service.helpers import handleDate


class DeviceBooking(Entity):
    """
    Represents a Device Booking on Labstep.

    """

    __entityName__ = "device-booking"

    def edit(self, started_at=UNSPECIFIED, ended_at=UNSPECIFIED, description=UNSPECIFIED, extraParams={}):
        """
        Edit an existing DeviceBooking.

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
            An object representing the edited DeviceBooking.

        Example
        -------
        ::

            my_device = user.getDevice(1000)
            my_device_booking = my_device.getDeviceBooking(17000)
            my_device_booking.edit(started_at='2025-08-20 00:00')
        """
        import labstep.entities.deviceBooking.repository as deviceBookingRepository

        return deviceBookingRepository.editDeviceBooking(
            self,
            started_at=handleDate(
                started_at) if started_at != UNSPECIFIED else UNSPECIFIED,
            ended_at=handleDate(
                ended_at) if ended_at != UNSPECIFIED else UNSPECIFIED,
            extraParams=extraParams
        )

    def delete(self):
        """
        Delete an existing DeviceBooking.

        Example
        -------
        ::

            my_device = user.getDevice(1000)
            my_device_booking = my_device.getDeviceBooking(17000)
            my_device_booking.delete()
        """
        import labstep.entities.deviceBooking.repository as deviceBookingRepository

        return deviceBookingRepository.editDeviceBooking(
            self, deleted_at=getTime()
        )
