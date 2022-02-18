#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entityPrimary.model import EntityPrimary
from labstep.generic.entityWithMetadata.model import EntityWithMetadata
from labstep.service.helpers import getTime
from labstep.constants import UNSPECIFIED


class OrderRequest(EntityPrimary, EntityWithMetadata):
    """
    Represents an Order Request on Labstep.

    To see all attributes of the order request run
    ::
        print(my_order_request)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(my_order_request.name)
        print(my_order_request.id)
    """

    __entityName__ = "order-request"

    def edit(
        self,
        status=UNSPECIFIED,
        resource_id=UNSPECIFIED,
        quantity=UNSPECIFIED,
        price=UNSPECIFIED,
        currency=UNSPECIFIED,
        extraParams={},
    ):
        """
        Edit an existing OrderRequest.

        Parameters
        ----------
        status (str)
            The status of the OrderRequest. Options are: "new", "approved",
            "ordered", "back_ordered", "received", and "cancelled".
        resource_id (int)
            The id of the :class:`~labstep.entities.resource.model.Resource` being requested.
        quantity (int)
            The quantity of the OrderRequest.
        price (int)
            The price of the OrderRequest.
        currency (str)
            The currency of the price in the format of the 3-letter
            currency code by country. For example, "EUR" for Euro, "GBP" for
            British Pound Sterling, "USD" for US Dollar, etc.

        Returns
        -------
        :class:`~labstep.entities.orderRequest.model.OrderRequest`
            An object representing the edited OrderRequest.

        Example
        -------
        ::

            my_orderRequest = user.getOrderRequest(17000)
            my_orderRequest.edit(status="back_ordered", quantity=3,
                                 price=50, currency="GBP")
        """
        import labstep.entities.orderRequest.repository as orderRequestRepository

        return orderRequestRepository.editOrderRequest(
            self,
            status=status,
            resource_id=resource_id,
            quantity=quantity,
            price=price,
            currency=currency,
            extraParams=extraParams,
        )

    def delete(self):
        """
        Delete an existing OrderRequest.

        Example
        -------
        ::

            my_orderRequest = user.getOrderRequest(17000)
            my_orderRequest.delete()
        """
        import labstep.entities.orderRequest.repository as orderRequestRepository

        return orderRequestRepository.editOrderRequest(self, deleted_at=getTime())

    def getResource(self):
        """
        Retrieve the Resource of the OrderRequest.

        Returns
        -------
        :class:`~labstep.entities.resource.model.Resource`
            An object representing the Resource of the OrderRequest.

        Example
        -------
        ::

            my_orderRequest = user.getOrderRequest(17000)
            my_orderRequest.getResource()
        """
        return self.__user__.getResource(self.resource["id"])
