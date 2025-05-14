#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED
from labstep.entities.resourceItem.model import ResourceItem
from labstep.service.helpers import handleKeyword


def getResourceItem(user, resourceItem_id):
    return entityRepository.getEntity(user, ResourceItem, id=resourceItem_id, extraParams={'serializerGroups': 'default,resource_item_metadatas'})


def getResourceItems(
    user, resource_id=UNSPECIFIED, count=UNSPECIFIED, search_query=UNSPECIFIED, extraParams={}
):
    params = {
        "search_query": search_query,
        "resource_id": resource_id,
        **extraParams,
    }
    return entityRepository.getEntities(user, ResourceItem, count, params)


def newResourceItem(
    user,
    resource_id,
    name=UNSPECIFIED,
    availability=UNSPECIFIED,
    amount=UNSPECIFIED,
    unit=UNSPECIFIED,
    resource_location_guid=UNSPECIFIED,
    extraParams={},
):
    params = {
        "resource_id": resource_id,
        "resource_location_guid": resource_location_guid,
        "name": name,
        "status": handleKeyword(availability),
        "amount": amount,
        "unit": unit,
        **extraParams,
    }

    return entityRepository.newEntity(user, ResourceItem, params)


def editResourceItem(
    resourceItem,
    name=UNSPECIFIED,
    availability=UNSPECIFIED,
    amount=UNSPECIFIED,
    unit=UNSPECIFIED,
    resource_location_guid=UNSPECIFIED,
    deleted_at=UNSPECIFIED,
    extraParams={},
):
    params = {
        "name": name,
        "status": handleKeyword(availability),
        "resource_location_guid": resource_location_guid,
        "unit": unit,
        "deleted_at": deleted_at,
        **extraParams,
    }

    if amount is not UNSPECIFIED:
        if amount != None:
            params["amount"] = str(float(amount))
        else:
            params["amount"] = amount

    return entityRepository.editEntity(resourceItem, params)
