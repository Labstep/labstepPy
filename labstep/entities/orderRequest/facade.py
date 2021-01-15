#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.orderRequest.repository import orderRequestRepository


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
    return orderRequestRepository.getOrderRequest(user, orderRequest_id)


def getOrderRequests(
    user, count=100, search_query=None, tag_id=None, status=None, extraParams={}
):
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
    return orderRequestRepository.getOrderRequests(
        user, count, search_query, tag_id, status, extraParams
    )


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
    return orderRequestRepository.newOrderRequest(
        user, resource_id, quantity, extraParams
    )


def editOrderRequest(
    orderRequest,
    status=None,
    resource_id=None,
    quantity=None,
    price=None,
    currency=None,
    deleted_at=None,
    extraParams={},
):
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
    return orderRequestRepository.editOrderRequest(
        orderRequest,
        status,
        resource_id,
        quantity,
        price,
        currency,
        deleted_at,
        extraParams,
    )
