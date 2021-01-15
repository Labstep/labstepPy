#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.primaryEntity.model import PrimaryEntity
from labstep.service.helpers import getTime


class OrderRequest(PrimaryEntity):
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
        status=None,
        resource_id=None,
        quantity=None,
        price=None,
        currency=None,
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
        from labstep.entities.orderRequest.repository import orderRequestRepository

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
        from labstep.entities.orderRequest.repository import orderRequestRepository

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

    def addMetadata(
        self,
        fieldName,
        fieldType="default",
        value=None,
        date=None,
        number=None,
        unit=None,
        filepath=None,
        extraParams={},
    ):
        """
        Add Metadata to an Order Request.

        Parameters
        ----------
        fieldName (str)
            The name of the field.
        fieldType (str)
            The Metadata field type. Options are: "default", "date",
            "numeric", or "file". The "default" type is "Text".
        value (str)
            The value accompanying the fieldName entry.
        date (str)
            The date accompanying the fieldName entry. Must be
            in the format of "YYYY-MM-DD HH:MM".
        number (float)
            The numeric value.
        unit (str)
            The unit accompanying the number entry.
        filepath (str)
            Local path to the file to upload for type 'file'

        Returns
        -------
        :class:`~labstep.entities.metadata.model.Metadata`
            An object representing the new Labstep Metadata.

        Example
        -------
        ::

            my_resource_category = user.getResourceCategory(17000)
            metadata = my_resource_category.addMetadata("Refractive Index",
                                               value="1.73")
        """
        from labstep.entities.metadata.repository import metadataRepository

        return metadataRepository.addMetadataTo(
            self,
            fieldName,
            fieldType,
            value,
            date,
            number,
            unit,
            filepath=filepath,
            extraParams=extraParams,
        )

    def getMetadata(self):
        """
        Retrieve the Metadata of a Labstep OrderRequest.

        Returns
        -------
        :class:`~labstep.entities.metadata.model.Metadata`
            An array of Metadata objects for the OrderRequest.

        Example
        -------
        ::

            my_order_request = user.getOrderRequest(17000)
            metadatas = my_order_request.getMetadata()
            metadatas[0].attributes()
        """
        from labstep.entities.metadata.repository import metadataRepository

        return metadataRepository.getMetadata(self)
