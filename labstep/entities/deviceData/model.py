#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.service.helpers import getTime


class DeviceData(Entity):
    __entityName__ = "device-data"

    def delete(self):
        """
        Delete a DeviceData.

        Example
        -------
        ::

            deviceData.delete()
        """
        from labstep.generic.entity.repository import entityRepository

        return entityRepository.editEntity(self, fields={"deleted_at": getTime()})
