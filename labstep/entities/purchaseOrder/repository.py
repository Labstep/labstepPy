#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED
from labstep.entities.purchaseOrder.model import PurchaseOrder
from labstep.service.helpers import handleKeyword


def newPurchaseOrder(user,name=UNSPECIFIED, status=UNSPECIFIED, currency='USD', extraParams={}):
    params = {'name':name,
              "group_id": user.activeWorkspace,
              "status": handleKeyword(status),
              "currency": currency,
              **extraParams}
    return entityRepository.newEntity(user, PurchaseOrder, params)

def getPurchaseOrder(user, purchase_order_id, extraParams={}):
    return entityRepository.getEntity(user, PurchaseOrder, id=purchase_order_id, extraParams={**extraParams,'serializerGroups': 'default,order_request_show'})


def getPurchaseOrders(
    user,
    count=UNSPECIFIED,
    status=UNSPECIFIED,
    extraParams={},
):
    params = {
        "group_id": user.activeWorkspace,
        "status": handleKeyword(status),
        **extraParams,
    }
    return entityRepository.getEntities(user, PurchaseOrder, count, params)


def editPurchaseOrder(
    purchaseOrder,
    name=UNSPECIFIED,
    status=UNSPECIFIED,
    currency=UNSPECIFIED,
    handling_amount=UNSPECIFIED,
    discount_amount=UNSPECIFIED,
    tax_rate=UNSPECIFIED,
    deleted_at=UNSPECIFIED,
    extraParams={},
):
    params = {
        'name':name,
        "status": handleKeyword(status),
        "currency": currency,
        'handling_amount':handling_amount,
        'discount_amount':discount_amount,
        'tax_rate':tax_rate,
        "deleted_at": deleted_at,
        **extraParams,
    }

    return entityRepository.editEntity(purchaseOrder, params)
