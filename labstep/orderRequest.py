#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylama:ignore=E501

from .entity import getEntity, getEntities, newEntity, editEntity
from .helpers import getTime, handleStatus, update, showAttributes
from .comment import addCommentWithFile, getComments
from .tag import tag, getAttachedTags
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


def getOrderRequests(user, count=100, search_query=None, tag_id=None):
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
    metadata = {'search_query': search_query,
                'tag_id': tag_id}
    return getEntities(user, OrderRequest, count, metadata)


def newOrderRequest(user, resource, quantity=1):
    """
    Create a new Labstep OrderRequest.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the OrderRequest.
        Must have property 'api_key'. See 'login'.
    resource (obj)
        The Labstep Resource.
    quantity (int)
        The quantity of the new OrderRequest.

    Returns
    -------
    OrderRequest
        An object representing the new Labstep OrderRequest.
    """
    fields = {'resource_id': resource.id,
              'quantity': quantity}
    return newEntity(user, OrderRequest, fields)


def editOrderRequest(orderRequest, status=None, resource=None, quantity=None,
                     price=None, currency=None, deleted_at=None):
    """
    Edit an existing OrderRequest.

    Parameters
    ----------
    orderRequest (obj)
        The OrderRequest to edit.
    status (str)
        The status of the OrderRequest. Options are: "new", "approved",
        "ordered", "back_ordered", "received", and "cancelled".
    resource (obj)
        The Resource of the OrderRequest.
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
    fields = {'status': handleStatus(status),
              'quantity': quantity,
              'price': price,
              'currency': currency,
              'deleted_at': deleted_at}
    if resource is not None:
        fields['resource_id'] = resource.id

    return editEntity(orderRequest, fields)


class OrderRequest:
    __entityName__ = 'order-request'

    def __init__(self, data, user):
        self.__user__ = user
        update(self, data)

    # functions()
    def attributes(self):
        """
        Show all attributes of an OrderRequest.

        Example
        -------
        .. code-block::

            my_order_request = user.getOrderRequest(17000)
            my_order_request.attributes()

        The output should look something like this:

        .. program-output:: python ../labstep/attributes/orderRequest_attributes.py

        To inspect specific attributes of an order request,
        for example, the order request 'name', 'id', 'status', etc.:

        .. code-block::

            print(my_order_request.name)
            print(my_order_request.id)
            print(my_order_request.status)
        """
        return showAttributes(self)

    def edit(self, status=None, resource=None, quantity=None,
             price=None, currency=None):
        """
        Edit an existing OrderRequest.

        Parameters
        ----------
        status (str)
            The status of the OrderRequest. Options are: "new", "approved",
            "ordered", "back_ordered", "received", and "cancelled".
        resource (obj)
            The Resource of the OrderRequest.
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
        .. code-block::

            my_orderRequest = user.getOrderRequest(17000)
            my_orderRequest.edit(status="back_ordered", quantity=3,
                                 price=50, currency="GBP")
        """
        return editOrderRequest(self, status, resource, quantity,
                                price, currency)

    def delete(self):
        """
        Delete an existing OrderRequest.

        Example
        -------
        .. code-block::

            my_orderRequest = user.getOrderRequest(17000)
            my_orderRequest.delete()
        """
        return editOrderRequest(self, deleted_at=getTime())

    def addComment(self, body, filepath=None):
        """
        Add a comment and/or file to a Labstep OrderRequest.

        Parameters
        ----------
        body (str)
            The body of the comment.
        filepath (str)
            A Labstep File entity to attach to the comment,
            including the filepath.

        Returns
        -------
        :class:`~labstep.comment.Comment`
            The comment added.

        Example
        -------
        .. code-block::

            my_orderRequest = user.getOrderRequest(17000)
            my_orderRequest.addComment(body='I am commenting!',
                                       filepath='pwd/file_to_upload.dat')
        """
        return addCommentWithFile(self, body, filepath)

    def getComments(self,count=100):
        """
        Gets the comments attached to this entity.

        Returns
        -------
        List[:class:`~labstep.comment.Comment`]
            List of the comments attached.

        Example
        -------
        .. code-block::

            entity = user.getOrderRequest(17000)
            comments = entity.getComments()
            print(comments[0].body)
        """
        return getComments(self,count)
        
    def addTag(self, name):
        """
        Add a tag to the OrderRequest (creates a
        new tag if none exists).

        Parameters
        ----------
        name (str)
            The name of the tag to create.

        Returns
        -------
        :class:`~labstep.orderRequest.OrderRequest`
            The OrderRequest that was tagged.

        Example
        -------
        .. code-block::

            my_orderRequest = user.getOrderRequest(17000)
            my_orderRequest.addTag(name='My Tag')
        """
        tag(self, name)
        return self

    def getTags(self):
        return getAttachedTags(self)

    def addMetadata(self, fieldType="default", fieldName=None,
                    value=None, date=None,
                    quantity_amount=None, quantity_unit=None):
        """
        Add Metadata to an Order Request.

        Parameters
        ----------
        fieldType (str)
            The Metadata field type. Options are: "default", "date",
            "quantity", or "number". The "default" type is "Text".
        fieldName (str)
            The name of the field.
        value (str)
            The value accompanying the fieldName entry.
        date (str)
            The date and time accompanying the fieldName entry. Must be
            in the format of "YYYY-MM-DD HH:MM".
        quantity_amount (float)
            The quantity.
        quantity_unit (str)
            The unit accompanying the quantity_amount entry.

        Returns
        -------
        :class:`~labstep.metadata.Metadata`
            An object representing the new Labstep Metadata.

        Example
        -------
        .. code-block::

            my_resource_category = user.getResourceCategory(17000)
            metadata = my_resource_category.addMetadata(fieldName="Refractive Index",
                                               value="1.73")
        """
        return addMetadataTo(self, fieldType, fieldName, value, date,
                             quantity_amount, quantity_unit)

    def getMetadata(self):
        return getMetadata(self)