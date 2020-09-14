#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .primaryEntity import PrimaryEntity
from .entity import getEntity, getEntities, newEntity, editEntity
from .helpers import getTime
from .metadata import addMetadataTo, getMetadata
from .resourceItem import getResourceItems, newResourceItem, ResourceItem
from .orderRequest import newOrderRequest
from .resourceCategory import getResourceCategory


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
    params = {'search_query': search_query,
              'tag_id': tag_id,
              **extraParams}
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
    params = {'name': name, **extraParams}
    return newEntity(user, Resource, params)


def editResource(resource, name=None, deleted_at=None,
                 resource_category_id=None,
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
    resource_category_id (obj)
        The id of the ResourceCategory to add to a Resource.

    Returns
    -------
    resource
        An object representing the edited Resource.
    """
    params = {'name': name,
              'template_id': resource_category_id,
              'deleted_at': deleted_at,
              **extraParams}
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

    def edit(self, name=None, extraParams={}):
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

    def addMetadata(self, fieldName, fieldType="default",
                    value=None, date=None,
                    number=None, unit=None,
                    extraParams={}):
        """
        Add Metadata to a Resource.

        Parameters
        ----------
        fieldName (str)
            The name of the field.
        fieldType (str)
            The Metadata field type. Options are: "default", "date",
            "quantity", or "number". The "default" type is "Text".
        value (str)
            The value accompanying the fieldName entry.
        date (str)
            The date and time accompanying the fieldName entry. Must be
            in the format of "YYYY-MM-DD HH:MM".
        number (float)
            The quantity.
        unit (str)
            The unit accompanying the number entry.

        Returns
        -------
        :class:`~labstep.metadata.Metadata`
            An object representing the new Labstep Metadata.

        Example
        -------
        ::

            resource = user.getResource(17000)
            metadata = resource.addMetadata("Refractive Index",
                                               value="1.73")
        """
        return addMetadataTo(self,
                             fieldName=fieldName,
                             fieldType=fieldType,
                             value=value, date=date,
                             number=number, unit=unit,
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

    def getResourceCategory(self):
        """
        Get the ResourceCategory of the Resource.

        Parameters
        ----------
        resource_category_id (int)
            The id of :class:`~labstep.resourceCategory.ResourceCategory`
            to set for
            the Resource.

        Returns
        -------
        :class:`~labstep.resourceCategory.ResourceCategory`
            An object representing the Resource Category on Labstep.

        Example
        -------
        ::

            # Get a Resource
            resource = user.getResource(170)

            # Get the Resource Category of the resource
            resourceCategory = resource.getResourceCategory()
        """
        return getResourceCategory(self.template['id'])

    def setResourceCategory(self, resource_category_id, extraParams={}):
        """
        Add a Labstep ResourceCategory to a Resource.

        Parameters
        ----------
        resource_category_id (int)
            The id of :class:`~labstep.resourceCategory.ResourceCategory`
            to set for
            the Resource.

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
            my_resource = my_resource.setResourceCategory(resource_category.id)
        """
        return editResource(self, resource_category_id=resource_category_id,
                            extraParams=extraParams)

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
        return newOrderRequest(self.__user__,
                               resource_id=self.id,
                               quantity=quantity,
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
        return getResourceItems(self.__user__,
                                resource_id=self.id,
                                count=count,
                                search_query=search_query,
                                extraParams=extraParams)

    def newItem(self, name=None, availability='available',
                quantity_amount=None, quantity_unit=None,
                resource_location_id=None, extraParams={}):
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
        resource_location_id (int)
            The id of the ResourceLocation of the ResourceItem.

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
        return newResourceItem(self.__user__,
                               name=name,
                               resource_id=self.id,
                               availability=availability,
                               quantity_amount=quantity_amount,
                               quantity_unit=quantity_unit,
                               resource_location_id=resource_location_id,
                               extraParams=extraParams)

    def getItemTemplate(self):
        '''
        Get the template used for initialising new items of the resource.
        Returns
        -------
        :class:`~labstep.resourceItem.ResourceItem`
            An object representing a ResourceItem on Labstep.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            itemTemplate = my_resource.getItemTemplate()

            itemTemplate.addMetadata('Expiry Date')

        '''
        if self.resource_item_template is None:
            return None

        return ResourceItem(self.resource_item_template, self.__user__)

    def enableCustomItemTemplate(self):
        '''
        Enable a custom item template for this resource.
        If disabled the template for the Resource Category will be used.

        Returns
        -------
        :class:`~labstep.resourceItem.ResourceItem`
            An object representing a ResourceItem on Labstep.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            my_resource.enableCustomItemTemplate()

            itemTemplate = my_resource.getItemTemplate()

            itemTemplate.addMetadata('Expiry Date')

        '''
        if self.resource_item_template is None:
            self.newItem(extraParams={'is_template': True})
        else:
            self.getItemTemplate().edit(extraParams={'deleted_at': None})

    def disableCustomItemTemplate(self):
        '''
        Disable custom item template for this resource.
        If disabled the template for the Resource Category will be used.

        Returns
        -------
        :class:`~labstep.resourceItem.ResourceItem`
            An object representing a ResourceItem on Labstep.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            my_resource.disableCustomItemTemplate()
        '''
        self.getItemTemplate().delete()
