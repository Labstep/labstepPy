#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylama:ignore=E501

from .primaryEntity import PrimaryEntity
from .entity import getEntity, getEntities, newEntity, editEntity
from .helpers import getTime, handleString
from .metadata import addMetadataTo, getMetadata


def getOrderRequest(user, orderRequest_id):
    """
    Retrieve a specific Labstep OrderRequest.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    orderRequest_id (int)
        The id of the OrderRequest to retrieve.

    Returns
    -------
    OrderRequest
        An object representing a Labstep OrderRequest.
    """
    return getEntity(user, OrderRequest, id=orderRequest_id)


def getOrderRequests(user, count=100, search_query=None, tag_id=None, status=None,
                     extraParams={}):
    """
    Retrieve a list of a user's OrderRequests on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    count (int)
        The number of OrderRequests to retrieve.
    search_query (str)
        Search for OrderRequests with this 'name'.
    tag_id (int)
        The id of the Tag to retrieve.

    Returns
    -------
    OrderRequests
        A list of OrderRequest objects.
    """
    params = {'search_query': search_query,
              'tag_id': tag_id,
              'status': handleString(status),
              **extraParams}
    return getEntities(user, OrderRequest, count, params)


def newOrderRequest(user, resource_id=None, quantity=1, extraParams={}):
    """
    Create a new Labstep OrderRequest.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the OrderRequest.
        Must have property 'api_key'. See 'login'.
    resource_id (obj)
        The id of the Labstep Resource being requested.
    quantity (int)
        The quantity of the new OrderRequest.

    Returns
    -------
    OrderRequest
        An object representing the new Labstep OrderRequest.
    """
    params = {'resource_id': resource_id,
              'quantity': quantity,
              **extraParams}
    return newEntity(user, OrderRequest, params)


def editOrderRequest(orderRequest, status=None, resource_id=None, quantity=None,
                     price=None, currency=None, deleted_at=None, extraParams={}):
    """
    Edit an existing OrderRequest.

    Parameters
    ----------
    orderRequest (obj)
        The OrderRequest to edit.
    status (str)
        The status of the OrderRequest. Options are: "new", "approved",
        "ordered", "back_ordered", "received", and "cancelled".
    resource_id (obj)
        The id of the Resource being requested.
    quantity (int)
        The quantity of the OrderRequest.
    price (int)
        The price of the OrderRequest.
    currency (str)
        The currency of the price in the format of the 3-letter
        currency code by country. For example, "EUR" for Euro, "GBP" for
        British Pound Sterling, "USD" for US Dollar, etc.
    deleted_at (str)
        The timestamp at which the OrderRequest is deleted/archived.

    Returns
    -------
    OrderRequest
        An object representing the edited OrderRequest.
    """
    params = {'status': handleString(status),
              'resource_id': resource_id,
              'quantity': quantity,
              'price': price,
              'currency': currency,
              'deleted_at': deleted_at,
              **extraParams}

    return editEntity(orderRequest, params)


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
    __entityName__ = 'order-request'

    def edit(self, status=None, resource_id=None, quantity=None,
             price=None, currency=None, extraParams={}):
        """
        Edit an existing OrderRequest.

        Parameters
        ----------
        status (str)
            The status of the OrderRequest. Options are: "new", "approved",
            "ordered", "back_ordered", "received", and "cancelled".
        resource_id (int)
            The id of the :class:`~labstep.resource.Resource` being requested.
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
        :class:`~labstep.orderRequest.OrderRequest`
            An object representing the edited OrderRequest.

        Example
        -------
        ::

            my_orderRequest = user.getOrderRequest(17000)
            my_orderRequest.edit(status="back_ordered", quantity=3,
                                 price=50, currency="GBP")
        """
        return editOrderRequest(self, status=status, resource_id=resource_id, quantity=quantity,
                                price=price, currency=currency, extraParams=extraParams)

    def delete(self):
        """
        Delete an existing OrderRequest.

        Example
        -------
        ::

            my_orderRequest = user.getOrderRequest(17000)
            my_orderRequest.delete()
        """
        return editOrderRequest(self, deleted_at=getTime())

    def getResource(self):
        """
        Retrieve the Resource of the OrderRequest.

        Returns
        -------
        :class:`~labstep.resource.Resource`
            An object representing the Resource of the OrderRequest.

        Example
        -------
        ::

            my_orderRequest = user.getOrderRequest(17000)
            my_orderRequest.getResource()
        """
        return self.__user__.getResource(self.resource['id'])

    def addMetadata(self, fieldName, fieldType="default",
                    value=None, date=None,
                    number=None, unit=None,
                    filepath=None,
                    extraParams={}):
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
        :class:`~labstep.metadata.Metadata`
            An object representing the new Labstep Metadata.

        Example
        -------
        ::

            my_resource_category = user.getResourceCategory(17000)
            metadata = my_resource_category.addMetadata("Refractive Index",
                                               value="1.73")
        """
        return addMetadataTo(self, fieldName, fieldType, value, date,
                             number, unit, filepath=filepath, extraParams=extraParams)

    def getMetadata(self):
        """
        Retrieve the Metadata of a Labstep OrderRequest.

        Returns
        -------
        :class:`~labstep.metadata.Metadata`
            An array of Metadata objects for the OrderRequest.

        Example
        -------
        ::

            my_order_request = user.getOrderRequest(17000)
            metadatas = my_order_request.getMetadata()
            metadatas[0].attributes()
        """
        return getMetadata(self)
