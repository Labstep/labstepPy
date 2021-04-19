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

    def newProtocolMaterial(self, user, protocol_id, name, resource_id=None, amount=None, units=None, extraParams={}):
        params = {
            "protocol_id": protocol_id,
            "name": name,
            "resource_id": resource_id,
            "value": amount,
            "units": units,
            **extraParams,
        }

        if params["value"] is not None:
            params["value"] = str(params["value"])

        return entityRepository.newEntity(user, ProtocolMaterial, params)

    def editProtocolMaterial(self, protocol_material, name=None, amount=None, units=None, resource_id=None, extraParams={}):
        params = {
            "name": name,
            "value": amount,
            "units": units,
            "resource_id": resource_id,
            **extraParams
        }

        return entityRepository.editEntity(protocol_material, params)


protocolMaterialRepository = ProtocolMaterialRepository()
