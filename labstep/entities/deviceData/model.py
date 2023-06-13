#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

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
        import labstep.generic.entity.repository as entityRepository

        return entityRepository.editEntity(self, fields={"deleted_at": getTime()})
