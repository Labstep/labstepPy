#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .entity import getEntity, getEntities, newEntity, editEntity
from .helpers import getTime, handleStatus, update
from .comment import addCommentWithFile
from .tag import tag


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


def newOrderRequest(user, name):
    """
    Create a new Labstep OrderRequest.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the OrderRequest.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your OrderRequest a name.

    Returns
    -------
    OrderRequest
        An object representing the new Labstep OrderRequest.
    """
    metadata = {'name': name}
    return newEntity(user, OrderRequest, metadata)


def editOrderRequest(orderRequest, status=None, resource=None, quantity=None,
                     price=None, currency=None, deleted_at=None):
    """
    Edit an existing OrderRequest.

    Parameters
    ----------
    orderRequest (obj)
        The OrderRequest to edit.
    name (str)
        The new name of the Experiment.
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
    def edit(self, status=None, resource=None, quantity=None,
             price=None, currency=None):
        """
        Edit an existing OrderRequest.

        Parameters
        ----------
        status (str)
            The status of the OrderRequest.
        resource (:class:`~labstep.resource.Resource`)
            The Resource being requested
        quantity (int)
            The number of items of the resource requested


        Returns
        -------
        :class:`~labstep.orderRequest.OrderRequest`
            An object representing the edited OrderRequest.

        Example
        -------
        .. code-block::

            my_orderRequest = user.getOrderRequest(17000)
            my_orderRequest.edit(name='A New OrderRequest Name')
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
