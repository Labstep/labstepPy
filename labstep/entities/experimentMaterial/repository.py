#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.experimentMaterial.model import ExperimentMaterial
from labstep.generic.entity.repository import entityRepository


class ExperimentMaterialRepository:
    def getExperimentMaterial(self, user, experiment_material_id):
        return entityRepository.getEntity(
            user, ExperimentMaterial, id=experiment_material_id
        )

    def getExperimentMaterials(self, user, experiment_id, count=100, extraParams={}):
        params = {
            'experiment_id': experiment_id,
            **extraParams
        }
        return entityRepository.getEntities(user, ExperimentMaterial, count, params)

    def newExperimentMaterial(self, user, experiment_id, name, resource_id=None, resource_item_id=None, amount=None, units=None, extraParams={}):
        params = {
            "experiment_id": experiment_id,
            "name": name,
            "resource_id": resource_id,
            "resource_item_id": resource_item_id,
            "value": amount,
            "units": units,
            **extraParams,
        }

        if params["value"] is not None:
            params["value"] = str(params["value"])

        return entityRepository.newEntity(user, ExperimentMaterial, params)

    def editExperimentMaterial(self, expermient_material, name=None, amount=None, units=None, resource_id=None, resource_item_id=None, extraParams={}):
        params = {
            "name": name,
            "value": amount,
            "units": units,
            "resource_id": resource_id,
            "resource_item_id": resource_item_id,
            **extraParams
        }

        return entityRepository.editEntity(expermient_material, params)


experimentMaterialRepository = ExperimentMaterialRepository()
