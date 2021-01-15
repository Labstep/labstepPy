#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.device.model import Device
from labstep.generic.entity.repository import entityRepository


class DeviceRepository:
    def getDevice(self, user, device_id):
        return entityRepository.getEntity(user, Device, id=device_id)

    def getDevices(self, user, count=100, search_query=None, extraParams={}):
        params = {"search_query": search_query, **extraParams}
        return entityRepository.getEntities(user, Device, count, params)

    def newDevice(self, user, name, extraParams={}):
        params = {"name": name, **extraParams}
        return entityRepository.newEntity(user, Device, params)

    def editDevice(self, device, name=None, deleted_at=None, extraParams={}):
        params = {"name": name, "deleted_at": deleted_at, **extraParams}
        return entityRepository.editEntity(device, params)


deviceRepository = DeviceRepository()
