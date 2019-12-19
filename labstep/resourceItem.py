#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylama:ignore=E501

from .entity import Entity, getEntity, getEntities, newEntity, editEntity
from .helpers import handleString, getTime
from .comment import addCommentWithFile, getComments
from .metadata import addMetadataTo, getMetadata


def getResourceItem(user, resourceItem_id):
    """
    Retrieve a specific Labstep ResourceItem.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    resourceItem_id (int)
        The id of the ResourceItem to retrieve.

    Returns
    -------
    ResourceItem
        An object representing a Labstep ResourceItem.
    """
    return getEntity(user, ResourceItem, id=resourceItem_id)


def getResourceItems(user, resource, count=100, search_query=None,
                     extraParams={}):
    """
    Retrieve a list of a user's ResourceItems on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    resource (obj)
        The Resource to retrieve the ResourceItems for.
    count (int)
        The number of ResourceItems to retrieve.
    search_query (str)
        Search for ResourceItems with this 'name'.
    extraParams (dict)
        Dictionary of extra filter parameters.

    Returns
    -------
    ResourceItems
        A list of ResourceItem objects.
    """
    filterParams = {'search_query': search_query,
                    'resource_id': resource.id}
    params = {**filterParams, **extraParams}
    return getEntities(user, ResourceItem, count, params)


def newResourceItem(user, resource, name=None, availability=None,
                    quantity_amount=None, quantity_unit=None,
                    location=None):
    """
    Create a new Labstep ResourceItem.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the ResourceItem.
        Must have property 'api_key'. See 'login'.
    resource (obj)
        The Resource to add a new ResourceItem to.
    name (str)
        The new name of the ResourceItem.
    availability (str)
        The status of the ResourceItem. Options are:
        "available" and "unavailable".
    quantity_amount (float)
        The quantity of the ResourceItem.
    quantity_unit (str)
        The unit of the quantity.
    location (obj)
        The ResourceLocation of the ResourceItem.

    Returns
    -------
    resource
        An object representing the new Labstep ResourceItem.
    """
    fields = {'resource_id': resource.id,
              'name': name,
              'status': handleString(availability),
              'quantity_amount': quantity_amount,
              'quantity_unit': quantity_unit}

    if location is not None:
        fields['resource_location_id'] = location.id

    return newEntity(user, ResourceItem, fields)


def editResourceItem(resourceItem, name=None, availability=None,
                     quantity_amount=None, quantity_unit=None,
                     location=None, deleted_at=None):
    """
    Edit an existing ResourceItem.

    Parameters
    ----------
    resourceItem (obj)
        The ResourceItem to edit.
    name (str)
        The new name of the ResourceItem.
    availability (str)
        The status of the ResourceItem. Options are:
        "available" and "unavailable".
    quantity_amount (float)
        The quantity of the ResourceItem.
    quantity_unit (str)
        The unit of the quantity.
    location (obj)
        The ResourceLocation of the ResourceItem.
    deleted_at (str)
        The timestamp at which the ResourceItem is deleted/archived.

    Returns
    -------
    ResourceItem
        An object representing the edited ResourceItem.
    """
    fields = {'name': name,
              'status': handleString(availability),
              'quantity_unit': quantity_unit,
              'deleted_at': deleted_at}

    if quantity_amount is not None:
        fields['quantity_amount'] = float(quantity_amount)

    if location is not None:
        fields['resource_location_id'] = location.id

    return editEntity(resourceItem, fields)


class ResourceItem(Entity):
    __entityName__ = 'resource-item'

    def edit(self, name=None, availability=None,
             quantity_amount=None, quantity_unit=None,
             location=None):
        """
        Edit an existing ResourceItem.

        Parameters
        ----------
        name (str)
            The new name of the ResourceItem.
        availability (str)
            The status of the OrderRequest. Options are:
            "available" and "unavailable".
        quantity_amount (float)
            The quantity of the ResourceItem.
        quantity_unit (str)
            The unit of the quantity.
        location (ResourceLocation)
            The :class:`~labstep.resourceLocation.ResourceLocation` of the ResourceItem.

        Returns
        -------
        :class:`~labstep.resourceItem.ResourceItem`
            An object representing the edited ResourceItem.

        Example
        -------
        ::

            my_resource_item = user.getResourceItem(17000)
            my_resource_item.edit(name='A New ResourceItem Name')
        """
        return editResourceItem(self, name, availability,
                                quantity_amount, quantity_unit,
                                location=location)

    def delete(self):
        """
        Delete an existing ResourceItem.

        Example
        -------
        ::

            my_resource_item = user.getResourceItem(17000)
            my_resource_item.delete()
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
        ::

            my_resource_item = user.getResourceItem(17000)
            my_resource_item.addComment(body='I am commenting!',
                                        filepath='pwd/file_to_upload.dat')
        """
        return addCommentWithFile(self, body, filepath)

    def getComments(self, count=100):
        """
        Retrieve the Comments attached to this Labstep Entity.

        Returns
        -------
        List[:class:`~labstep.comment.Comment`]
            List of the comments attached.

        Example
        -------
        ::

            entity = user.getResource(17000)
            item = entity.getItems()[1]
            comments = item.getComments()
            comments[0].attributes()
        """
        return getComments(self, count)

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
        ::

            my_resource_item = user.getResourceItem(17000)
            metadata = my_resource_item.addMetadata(fieldName="Refractive Index",
                                                    value="1.73")
        """
        return addMetadataTo(self, fieldType, fieldName, value, date,
                             quantity_amount, quantity_unit)

    def getMetadata(self):
        """
        Retrieve the Metadata of a Labstep ResourceItem.

        Returns
        -------
        List[:class:`~labstep.resource.ResourceItem`]
            An array of Metadata objects for the ResourceItem.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            my_resource_item = my_resource.getResourceItem(17000)
            metadata = my_resource_item.getMetadata()
            metadatas[0].attributes()
        """
        return getMetadata(self)
