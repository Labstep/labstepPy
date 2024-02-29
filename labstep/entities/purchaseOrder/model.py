#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entityWithMetadata.model import EntityWithMetadata
from labstep.generic.entityWithComments.model import EntityWithComments
from labstep.generic.entityWithAssign.model import EntityWithAssign
from labstep.service.helpers import getTime
from labstep.constants import UNSPECIFIED


class PurchaseOrder(EntityWithComments, EntityWithAssign, EntityWithMetadata):
    """
    Represents a Purchase Order on Labstep.

    To see all attributes of the order request run
    ::
        print(my_order_request)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(my_order_request.name)
        print(my_order_request.id)
    """

    __entityName__ = "purchase-order"

    def edit(
        self,
        name=UNSPECIFIED,
        status=UNSPECIFIED,
        currency=UNSPECIFIED,
        handling_amount=UNSPECIFIED,
        discount_amount=UNSPECIFIED,
        tax_rate=UNSPECIFIED,
        extraParams={},
    ):
        """
        Edit an existing Purchase Order.

        Parameters
        ----------
        name (str)
            The name of the Purchase Order.
        status (str)
            The status of the Purchase Order. Options are: "open", "pending",
            and "completed".
        currency (str)
            The currency of the price in the format of the 3-letter
            currency code by country. For example, "EUR" for Euro, "GBP" for
            British Pound Sterling, "USD" for US Dollar, etc.
        handling_amount (int)
            The amount designed to handling the Purchase Order.
        deducted_amount (int)
            The amount deducted in the Purchase Order.
        tax_rate (int)
            The tax rate used to calculate the total in the Purchase Order.
        

        Returns
        -------
        :class:`~labstep.entities.purchaseOrder.model.PurchaseOrder`
            An object representing the edited PurchaseOrder.

        Example
        -------
        ::

            my_purchaseOrder = user.getPurchaseOrder(17000)
            my_purchaseOrder.edit(status="completed", currency="GBP")
        """
        import labstep.entities.purchaseOrder.repository as purchaseOrderRepository

        return purchaseOrderRepository.editPurchaseOrder(
            self,
            name=name,
            status=status,
            currency=currency,
            handling_amount=handling_amount,
            discount_amount=discount_amount,
            tax_rate=tax_rate,
            extraParams=extraParams,
        )
    
    def delete(self):
        """
        Delete an existing Purchase Order.

        Example
        -------
        ::

            my_purchaseOrder = user.getPurchaseOrder(17000)
            my_purchaseOrder.delete()
        """
        import labstep.entities.purchaseOrder.repository as purchaseOrderRepository

        return purchaseOrderRepository.editPurchaseOrder(self, deleted_at=getTime())


    def addOrderRequest(self, order_request_id):
        """
        Add Order Request to an existing Purchase Order.

        Parameters
        ----------
        order_request_id (int)
            The ID of the Order request to be added to the Purchase Order.

        Example
        -------
        ::

            my_purchaseOrder = user.getPurchaseOrder(17000)
            my_purchaseOrder.addOrderRequest(120)
        """
        import labstep.entities.purchaseOrder.repository as purchaseOrderRepository

        user=self.__user__
        order_request=user.getOrderRequest(order_request_id)
        order_request.edit(extraParams={'purchase_order_id':self.id})

        return purchaseOrderRepository.getPurchaseOrder(self.__user__, self.id)
    
    def getOrderRequests(self):
        from labstep.generic.entityList.model import EntityList
        from labstep.entities.orderRequest.model import OrderRequest
        self.update()
        return EntityList(self.order_requests, OrderRequest, self.__user__)