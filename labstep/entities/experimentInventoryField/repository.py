#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.experimentInventoryField.model import ExperimentInventoryField
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED
import labstep.generic.entity.repository as entityRepository


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

def getValue(experiment_inventory_field, condition_id=UNSPECIFIED):
    """
    Get the value of an Experiment Inventory Field for a specific condition.

    Parameters
    ----------
    condition_id : int
        The ID of the condition to get the value for.

    Returns
    -------
    (amount, resource_item)
        The amount and ite, of the Experiment Inventory Field for the specified condition.
    """
    return experiment_inventory_field.getValue(condition_id)


def setValue(experiment_inventory_field, amount, resource_item_id=UNSPECIFIED, condition_id=UNSPECIFIED):
    """
    Set the value of an Experiment Inventory Field for a specific condition.

    Parameters
    ----------
    amount : float, optional
        The amount to set for the Experiment Inventory Field.
    resource_item_id : int, optional
        The ID of the resource item to associate with the Experiment Inventory Field.
    condition_id : int
        The ID of the condition to set the value for.

    Returns
    -------
    ExperimentInventoryField
        An object representing the edited Experiment Inventory Field.
    """
    if condition_id is not UNSPECIFIED:
        if experiment_inventory_field.is_variable is False:
            raise Exception(
                'Cannot set value for conditions on a constant field')

        conditionInventoryField = entityRepository.getEntities(
            experiment_inventory_field.__user__, ExperimentInventoryField, count=UNSPECIFIED, filterParams={
                'protocol_condition_id': condition_id
        }).get(experiment_inventory_field.guid, searchKey='variable_template_guid')

        if conditionInventoryField is None:
            params = {
                "is_input":experiment_inventory_field.is_input,
                "is_output":experiment_inventory_field.is_output,
                "experiment_id": experiment_inventory_field.experiment['id'],
                "variable_template_id": experiment_inventory_field.id,
                "protocol_condition_id": condition_id,
                "resource_item_id": resource_item_id,
                "value": amount,
            }
            conditionInventoryField = entityRepository.newEntity(experiment_inventory_field.__user__, ExperimentInventoryField, params)

        return conditionInventoryField.edit(amount=amount, resource_item_id=resource_item_id)

    return experiment_inventory_field.edit(amount=amount, resource_item_id=resource_item_id)