#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.service.helpers import handleString
from labstep.entities.orderRequest.model import OrderRequest
from labstep.generic.entity.repository import entityRepository

class OrderRequestRepository:
    def getOrderRequest(self, user, orderRequest_id):
        return entityRepository.getEntity(user, OrderRequest, id=orderRequest_id)

    def getOrderRequests(
        self,
        user,
        count=100,
        search_query=None,
        tag_id=None,
        status=None,
        extraParams={},
    ):
        params = {
            "group_id": user.activeWorkspace,
            "search_query": search_query,
            "tag_id": tag_id,
            "status": handleString(status),
            **extraParams,
        }
        return entityRepository.getEntities(user, OrderRequest, count, params)

    def newOrderRequest(self, user, resource_id=None, quantity=1, extraParams={}):
        params = {"resource_id": resource_id, "quantity": quantity, **extraParams}
        return entityRepository.newEntity(user, OrderRequest, params)

    def editOrderRequest(
        self,
        orderRequest,
        status=None,
        resource_id=None,
        quantity=None,
        price=None,
        currency=None,
        deleted_at=None,
        extraParams={},
    ):
        params = {
            "status": handleString(status),
            "resource_id": resource_id,
            "quantity": quantity,
            "price": price,
            "currency": currency,
            "deleted_at": deleted_at,
            **extraParams,
        }

        return entityRepository.editEntity(orderRequest, params)


orderRequestRepository = OrderRequestRepository()
