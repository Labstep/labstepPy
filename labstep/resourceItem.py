#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .entity import getEntity, getEntities, newEntity, editEntity
from .helpers import getTime, update, showAttributes
from .comment import addCommentWithFile, getComments
from .metadata import addMetadataTo, getMetadata
from .resourceCategory import newResourceCategory
from .orderRequest import newOrderRequest
from .tag import tag


def getResourceItem(user, resource_id):
    """
    Retrieve a specific Labstep ResourceItem.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    resource_id (int)
        The id of the ResourceItem to retrieve.

    Returns
    -------
    resource
        An object representing a Labstep ResourceItem.
    """
    return getEntity(user, ResourceItem, id=resource_id)


def getResourceItems(user, resource, search_query=None, count=100,
                 extraParams={}):
    """
    Retrieve a list of a user's ResourceItems on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    count (int)
        The number of ResourceItems to retrieve.
    search_query (str)
        Search for ResourceItems with this 'name'.
    extraParams (dict)
        Dictionary of extra filter parameters.

    Returns
    -------
    resources
        A list of ResourceItem objects.
    """
    filterParams = {'search_query': search_query,
                    'resource_id': resource.id}
    params = {**filterParams, **extraParams}
    return getEntities(user, ResourceItem, count, params)


def newResourceItem(user, resource, name=None):
    """
    Create a new Labstep ResourceItem.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the ResourceItem.
        Must have property 'api_key'. See 'login'.
    resource ()
    name (str)
        Give your resource a name.

    Returns
    -------
    resource
        An object representing the new Labstep ResourceItem.
    """
    fields = {'name': name, 'resource_id': resource.id }
    return newEntity(user, ResourceItem, fields)


def editResourceItem(resourceItem, name=None, deleted_at=None):
    """
    Edit an existing ResourceItem.

    Parameters
    ----------
    resourceItem (obj)
        The ResourceItem to edit.
    name (str)
        The new name of the Experiment.
    deleted_at (str)
        The timestamp at which the ResourceItem is deleted/archived.

    Returns
    -------
    resource
        An object representing the edited ResourceItem.
    """
    fields = {'name': name,
              'deleted_at': deleted_at}
    return editEntity(resourceItem, fields)


class ResourceItem:
    __entityName__ = 'resource-item'

    def __init__(self, fields, user):
        self.__user__ = user
        update(self, fields)

    # functions()
    def attributes(self):
        """
        Show all attributes of a ResourceItem.

        Example
        -------
        .. code-block::

            my_resource = user.getResourceItem(17000)
            my_resource.attributes()

        The output should look something like this:

        .. program-output:: python ../labstep/attributes/resource_attributes.py

        To inspect specific attributes of a resource,
        for example, the resource 'name', 'id', etc.:

        .. code-block::

            print(my_resource.name)
            print(my_resource.id)
        """
        return showAttributes(self)

    def edit(self, name):
        """
        Edit an existing ResourceItem.

        Parameters
        ----------
        name (str)
            The new name of the ResourceItem.

        Returns
        -------
        :class:`~labstep.resource.ResourceItem`
            An object representing the edited ResourceItem.

        Example
        -------
        .. code-block::

            my_resource = user.getResourceItem(17000)
            my_resource.edit(name='A New ResourceItem Name')
        """
        return editResourceItem(self, name)

    def delete(self):
        """
        Delete an existing ResourceItem.

        Example
        -------
        .. code-block::

            my_resource = user.getResourceItem(17000)
            my_resource.delete()
        """
        return editResourceItem(self, deleted_at=getTime())

    def addComment(self, body, filepath=None):
        """
        Add a comment and/or file to a Labstep ResourceItem.

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

            my_resource = user.getResourceItem(17000)
            my_resource.addComment(body='I am commenting!',
                                filepath='pwd/file_to_upload.dat')
        """
        return addCommentWithFile(self, body, filepath)

    def getComments(self,count):
        """
        Gets the comments attached to this entity.

        Returns
        -------
        List[:class:`~labstep.comment.Comment`]
            List of the comments attached.

        Example
        -------
        .. code-block::

            entity = user.getResource(17000)
            comments = entity.getComments()
            print(comments[0].body)
        """
        return getComments(self,count)

    def addMetadata(self, fieldType="default", fieldName=None,
                    value=None, date=None,
                    quantity_amount=None, quantity_unit=None):
        """
        Add Metadata to a ResourceItem.

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

            my_resource = user.getResourceItem(17000)
            metadata = my_resource.addMetadata(fieldName="Refractive Index",
                                               value="1.73")
        """
        return addMetadataTo(self, fieldType, fieldName, value, date,
                             quantity_amount, quantity_unit)

    def getMetadata(self):
        """
        Get the metadata associated with the ResourceItem.
        Returns
        -------
        List[:class:`~labstep.resource.ResourceItem`]
            An array of Metadata objects for the ResourceItem.
        """
        return getMetadata(self)