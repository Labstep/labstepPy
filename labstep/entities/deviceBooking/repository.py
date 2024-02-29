#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.deviceBooking.model import DeviceBooking
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def getDeviceBooking(user, device_id, deviceBooking_id):
    params = {'device_id': device_id}
    return entityRepository.getEntity(user, DeviceBooking, id=deviceBooking_id, extraParams=params)


def getDeviceBookings(
        user, device_id, count=UNSPECIFIED, extraParams={}
):

    params = {'device_id': device_id, **extraParams}
    return entityRepository.getEntities(user, DeviceBooking, count, params)


def newDeviceBooking(user, device, ended_at, started_at, description=UNSPECIFIED, extraParams={}):
    params = {'ended_at': ended_at,
              'started_at': started_at,
              'device_id': device.id,
              'description': description,
              ** extraParams}
    return entityRepository.newEntity(user, DeviceBooking, params)


def editDeviceBooking(
        deviceBooking, ended_at=UNSPECIFIED, started_at=UNSPECIFIED, deleted_at=UNSPECIFIED, extraParams={}
):
    params = {'ended_at': ended_at,
              'started_at': started_at,
              "deleted_at": deleted_at, **extraParams}
    return entityRepository.editEntity(deviceBooking, params)
