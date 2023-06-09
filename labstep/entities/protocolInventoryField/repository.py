#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.protocolInventoryField.model import ProtocolInventoryField
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def getProtocolInventoryField(user, protocol_inventory_field_id):
    return entityRepository.getEntity(
        user, ProtocolInventoryField, id=protocol_inventory_field_id
    )


def getProtocolInventoryFields(user, protocol_id, count=UNSPECIFIED, extraParams={}):
    params = {
        'protocol_id': protocol_id,
        **extraParams
    }
    return entityRepository.getEntities(user, ProtocolInventoryField, count, params)


def newProtocolInventoryField(user, protocol_id, name, resource_id=UNSPECIFIED, amount=UNSPECIFIED, units=UNSPECIFIED, extraParams={}):
    params = {
        "protocol_id": protocol_id,
        "name": name,
        "resource_id": resource_id,
        "value": amount,
        "units": units,
        **extraParams,
    }

    if params["value"] is not UNSPECIFIED:
        params["value"] = str(params["value"])

    return entityRepository.newEntity(user, ProtocolInventoryField, params)


def editProtocolInventoryField(protocol_inventory_field, name=UNSPECIFIED, amount=UNSPECIFIED, units=UNSPECIFIED, resource_id=UNSPECIFIED, extraParams={}):
    params = {
        "name": name,
        "value": amount,
        "units": units,
        "resource_id": resource_id,
        **extraParams
    }

    return entityRepository.editEntity(protocol_inventory_field, params)
