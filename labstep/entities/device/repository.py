#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.device.model import Device
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def getDevice(user, device_id):
    return entityRepository.getEntity(user, Device, id=device_id)


def getDevices(user, count=100, search_query=UNSPECIFIED, extraParams={}):
    params = {"search_query": search_query, **extraParams}
    return entityRepository.getEntities(user, Device, count, params)


def newDevice(user, name, extraParams={}):
    params = {"name": name, **extraParams}
    return entityRepository.newEntity(user, Device, params)


def editDevice(device, name=UNSPECIFIED, deleted_at=UNSPECIFIED, extraParams={}):
    params = {"name": name, "deleted_at": deleted_at, **extraParams}
    return entityRepository.editEntity(device, params)
