#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.device.model import Device
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def getDevice(user, device_id):
    return entityRepository.getEntity(user, Device, id=device_id)


def getDevices(user, count=UNSPECIFIED, search_query=UNSPECIFIED, extraParams={}):
    params = {"search_query": search_query, **extraParams}
    return entityRepository.getEntities(user, Device, count, params)


def newDevice(user, name, extraParams={}, device_category_id=UNSPECIFIED):
    params = {"name": name,
              'template_id':device_category_id,
              **extraParams}
    return entityRepository.newEntity(user, Device, params)


def editDevice(device, name=UNSPECIFIED, deleted_at=UNSPECIFIED, extraParams={},device_category_id=UNSPECIFIED):
    params = {"name": name, 
              "deleted_at": deleted_at, 
              'template_id':device_category_id,
              **extraParams}
    return entityRepository.editEntity(device, params)
