#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.experimentInventoryField.model import ExperimentInventoryField
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def getExperimentInventoryField(user, experiment_inventoryfield_id):
    return entityRepository.getEntity(
        user, ExperimentInventoryField, id=experiment_inventoryfield_id
    )


def getExperimentInventoryFields(user, experiment_id, count=UNSPECIFIED, extraParams={}):
    params = {
        'experiment_id': experiment_id,
        **extraParams
    }
    return entityRepository.getEntities(user, ExperimentInventoryField, count, params)


def newExperimentInventoryField(user, experiment_id, name, resource_id=UNSPECIFIED, resource_item_id=UNSPECIFIED, amount=UNSPECIFIED, units=UNSPECIFIED, extraParams={}):
    params = {
        "experiment_id": experiment_id,
        "name": name,
        "resource_id": resource_id,
        "resource_item_id": resource_item_id,
        "value": amount,
        "units": units,
        **extraParams,
    }

    if params["value"] is not UNSPECIFIED:
        params["value"] = str(params["value"])

    return entityRepository.newEntity(user, ExperimentInventoryField, params)


def editExperimentInventoryField(expermient_inventoryfield, name=UNSPECIFIED, amount=UNSPECIFIED, units=UNSPECIFIED, resource_id=UNSPECIFIED, resource_item_id=UNSPECIFIED, extraParams={}):
    params = {
        "name": name,
        "value": amount,
        "units": units,
        "resource_id": resource_id,
        "resource_item_id": resource_item_id,
        **extraParams
    }

    return entityRepository.editEntity(expermient_inventoryfield, params)
