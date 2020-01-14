#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylama:ignore=E501

from .entity import Entity, getEntity, getEntities, newEntity, editEntity
from .helpers import getTime, handleString
from .comment import addCommentWithFile, getComments
from .tag import tag, getAttachedTags
from .metadata import addMetadataTo, getMetadata
from .permissions import getPermissions, newPermission, transferOwnership


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


def getOrderRequests(user, count=100, search_query=None, tag_id=None,
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
    filterParams = {'search_query': search_query,
                    'tag_id': tag_id}
    params = {**filterParams, **extraParams}
    return getEntities(user, OrderRequest, count, params)


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
    fields = {'status': handleString(status),
              'quantity': quantity,
              'price': price,
              'currency': currency,
              'deleted_at': deleted_at}
    if resource is not None:
        fields['resource_id'] = resource.id

    return editEntity(orderRequest, fields)


class OrderRequest(Entity):
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

    def edit(self, status=None, resource=None, quantity=None,
             price=None, currency=None):
        """
        Edit an existing OrderRequest.

        Parameters
        ----------
        status (str)
            The status of the OrderRequest. Options are: "new", "approved",
            "ordered", "back_ordered", "received", and "cancelled".
        resource (Resource)
            The :class:`~labstep.resource.Resource` of the OrderRequest.
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
        return editOrderRequest(self, status, resource, quantity,
                                price, currency)

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
        ::

            my_orderRequest = user.getOrderRequest(17000)
            my_orderRequest.addComment(body='I am commenting!',
                                       filepath='pwd/file_to_upload.dat')
        """
        return addCommentWithFile(self, body, filepath)

    def getComments(self, count=100):
        """
        Gets the comments attached to this entity.

        Returns
        -------
        List[:class:`~labstep.comment.Comment`]
            List of the comments attached.

        Example
        -------
        ::

            entity = user.getOrderRequest(17000)
            comments = entity.getComments()
            comments[0].attributes()
        """
        return getComments(self, count)

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
        ::

            my_orderRequest = user.getOrderRequest(17000)
            my_orderRequest.addTag(name='My Tag')
        """
        tag(self, name)
        return self

    def getTags(self):
        """
        Retrieve the Tags attached to a this Labstep Entity.

        Returns
        -------
        List[:class:`~labstep.tag.Tag`]
            List of the tags attached.

        Example
        -------
        ::

            entity = user.getOrderRequest(17000)
            tags = entity.getTags()
            tags[0].attributes()
        """
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
        ::

            my_resource_category = user.getResourceCategory(17000)
            metadata = my_resource_category.addMetadata(fieldName="Refractive Index",
                                               value="1.73")
        """
        return addMetadataTo(self, fieldType, fieldName, value, date,
                             quantity_amount, quantity_unit)

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

    def getPermissions(self):
        """
        Returns the sharing permissions for the Order Request.

        Returns
        -------
        List[:class:`~labstep.permissions.Permission`]
        """
        return getPermissions(self)

    def shareWith(self, workspace_id, permission='view'):
        """
        Shares the OrderRequest with another Workspace.

        Parameters
        ----------
        workspace_id (int)
            The id of the workspace to share with

        permission (str)
            Permission to share with. Can be 'view' or 'edit'

        Returns
        -------
        None
        """
        return newPermission(self, workspace_id, permission)

    def transferOwnership(self, workspace_id):
        """
        Transfer ownership of the Entity to a different Workspace

        Parameters
        ----------
        workspace_id (int)
            The id of the workspace to transfer ownership to
        """
        return transferOwnership(self, workspace_id)
