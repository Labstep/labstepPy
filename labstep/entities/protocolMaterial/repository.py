#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.protocolMaterial.model import ProtocolMaterial
from labstep.generic.entity.repository import entityRepository


class ProtocolMaterialRepository:
    def getProtocolMaterial(self, user, protocol_material_id):
        return entityRepository.getEntity(
            user, ProtocolMaterial, id=protocol_material_id
        )

    def getProtocolMaterials(self, user, protocol_id, count=100, extraParams={}):
        params = {
            'protocol_id': protocol_id,
            **extraParams
        }
        return entityRepository.getEntities(user, ProtocolMaterial, count, params)

    def newProtocolMaterial(self, user, name, resource_id=None, amount=None, units=None, extraParams={}):
        params = {
            "protocol_id": self.id,
            "name": name,
            "resource_id": resource_id,
            "value": amount,
            "units": units,
            **extraParams,
        }

        if params["value"] is not None:
            params["value"] = str(params["value"])

        return entityRepository.newEntity(self.__user__, ProtocolMaterial, params)

    def editProtocolMaterial(self, amount=None, units=None, resource_id=None):
        params = {
            "value": amount,
            "units": units,
            "resource_id": resource_id,
        }

        return entityRepository.editEntity(self, params)


protocolMaterialRepository = ProtocolMaterialRepository()
