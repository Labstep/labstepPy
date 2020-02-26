#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .primaryEntity import PrimaryEntity
from .entity import getEntity, getEntities, newEntity, editEntity
from .helpers import getTime
from .metadata import addMetadataTo, getMetadata
from .resourceItem import getResourceItems, newResourceItem
from .orderRequest import newOrderRequest


def getResource(user, resource_id):
    """
    Retrieve a specific Labstep Resource.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    resource_id (int)
        The id of the Resource to retrieve.

    Returns
    -------
    resource
        An object representing a Labstep Resource.
    """
    return getEntity(user, Resource, id=resource_id)


def getResources(user, count=100, search_query=None, tag_id=None,
                 extraParams={}):
    """
    Retrieve a list of a user's Resources on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    count (int)
        The number of Resources to retrieve.
    search_query (str)
        Search for Resources with this 'name'.
    tag_id (int)
        The id of the Tag to retrieve.
    extraParams (dict)
        Dictionary of extra filter parameters.

    Returns
    -------
    resources
        A list of Resource objects.
    """
    filterParams = {'search_query': search_query,
                    'tag_id': tag_id}
    params = {**filterParams, **extraParams}
    return getEntities(user, Resource, count, params)


def newResource(user, name, extraParams={}):
    """
    Create a new Labstep Resource.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the Resource.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your Resource a name.

    Returns
    -------
    resource
        An object representing the new Labstep Resource.
    """
    filterParams = {'name': name}
    params = {**filterParams, **extraParams}
    return newEntity(user, Resource, params)


def editResource(resource, name=None, deleted_at=None, resource_category=None,
                 extraParams={}):
    """
    Edit an existing Resource.

    Parameters
    ----------
    resource (obj)
        The Resource to edit.
    name (str)
        The new name of the Experiment.
    deleted_at (str)
        The timestamp at which the Resource is deleted/archived.
    resource_category (obj)
        The ResourceCategory to add to a Resource.

    Returns
    -------
    resource
        An object representing the edited Resource.
    """
    filterParams = {'name': name,
                    'deleted_at': deleted_at}

    if resource_category is not None:
        filterParams['resource_category_id'] = resource_category.id

    params = {**filterParams, **extraParams}
    return editEntity(resource, params)


class Resource(PrimaryEntity):
    """
    Represents a Resource on Labstep.

    To see all attributes of the resource run
    ::
        print(my_resource)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(my_resource.name)
        print(my_resource.id)
    """
    __entityName__ = 'resource'

    def edit(self, name, extraParams={}):
        """
        Edit an existing Resource.

        Parameters
        ----------
        name (str)
            The new name of the Resource.

        Returns
        -------
        :class:`~labstep.resource.Resource`
            An object representing the edited Resource.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            my_resource.edit(name='A New Resource Name')
        """
        return editResource(self, name, extraParams=extraParams)

    def delete(self):
        """
        Delete an existing Resource.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            my_resource.delete()
        """
        return editResource(self, deleted_at=getTime())

    def addMetadata(self, fieldType="default", fieldName=None,
                    value=None, date=None,
                    quantity_amount=None, quantity_unit=None,
                    extraParams={}):
        """
        Add Metadata to a Resource.

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

            my_resource = user.getResource(17000)
            metadata = my_resource.addMetadata(fieldName="Refractive Index",
                                               value="1.73")
        """
        return addMetadataTo(self, fieldType, fieldName, value, date,
                             quantity_amount, quantity_unit,
                             extraParams=extraParams)

    def getMetadata(self):
        """
        Retrieve the Metadata of a Labstep Resource.

        Returns
        -------
        :class:`~labstep.metadata.Metadata`
            An array of Metadata objects for the Resource.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            metadatas = my_resource.getMetadata()
            metadatas[0].attributes()
        """
        return getMetadata(self)

    def setResourceCategory(self, resource_category, extraParams={}):
        """
        Add a Labstep ResourceCategory to a Resource.

        Parameters
        ----------
        resource_category (ResourceCategory)
            The :class:`~labstep.resourceCategory.ResourceCategory` to add
            to the Resource.

        Returns
        -------
        :class:`~labstep.resource.Resource`
            An object representing the Resource on Labstep.

        Example
        -------
        ::

            # Get a ResourceCategory
            resource_category = user.getResourceCategory(170)

            # Set the Resource Category
            my_resource = my_resource.setResourceCategory(resource_category)
        """
        return editResource(self, resource_category, extraParams=extraParams)

    def newOrderRequest(self, quantity=1, extraParams={}):
        """
        Create a new Labstep OrderRequest.

        Parameters
        ----------
        quantity (int)
            The quantity of the new OrderRequest.

        Returns
        -------
        :class:`~labstep.orderRequest.OrderRequest`
            An object representing the new OrderRequest on Labstep.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            order_request = my_resource.newOrderRequest(quantity=2)
        """
        return newOrderRequest(self.__user__, self, quantity,
                               extraParams=extraParams)

    def getItems(self, count=100, search_query=None, extraParams={}):
        """
        Returns the items of this Resource.

        Parameters
        ----------
        count (int)
            The number of ResourceItems to retrieve.
        search_query (str)
            Search for ResourceItems with this 'name'.
        extraParams (dict)
            Dictionary of extra filter parameters.

        Returns
        -------
        List[:class:`~labstep.resourceItem.ResourceItem`]
            A list of ResourceItem objects.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            items = my_resource.getItems()
        """
        return getResourceItems(self.__user__, self, count=count,
                                search_query=search_query,
                                extraParams=extraParams)

    def newItem(self, name=None, availability='available',
                quantity_amount=None, quantity_unit=None,
                location=None, extraParams={}):
        """
        Create a new Labstep ResourceItem.

        Parameters
        ----------
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
        :class:`~labstep.resourceItem.ResourceItem`
            An object representing a ResourceItem on Labstep.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            item = my_resource.newItem(name='Test Item')
        """
        return newResourceItem(self.__user__, self, name,
                               availability, quantity_amount,
                               quantity_unit, location,
                               extraParams=extraParams)
