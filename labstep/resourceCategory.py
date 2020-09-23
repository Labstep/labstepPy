#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylama:ignore=E501

from .primaryEntity import PrimaryEntity
from .entity import getEntity, getEntities, newEntity, editEntity, Entity
from .helpers import getTime
from .metadata import addMetadataTo, getMetadata
from .resourceItem import ResourceItem, newResourceItem


def getResourceCategory(user, resourceCategory_id):
    """
    Retrieve a specific Labstep ResourceCategory.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    resourceCategory_id (int)
        The id of the ResourceCategory to retrieve.

    Returns
    -------
    ResourceCategory
        An object representing a Labstep ResourceCategory.
    """
    return getEntity(user, ResourceCategory, id=resourceCategory_id)


def getResourceCategorys(user, count=100, search_query=None, tag_id=None,
                         extraParams={}):
    """
    Retrieve a list of a user's ResourceCategorys on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    count (int)
        The number of ResourceCategorys to retrieve.
    search_query (str)
        Search for ResourceCategorys with this 'name'.
    tag_id (int)
        The id of the Tag to retrieve.

    Returns
    -------
    ResourceCategorys
        A list of ResourceCategory objects.
    """
    filterParams = {'search_query': search_query,
                    'tag_id': tag_id}
    params = {**filterParams, **extraParams, 'is_template': 1}
    return getEntities(user, ResourceCategory, count, params)


def newResourceCategory(user, name, extraParams={}):
    """
    Create a new Labstep ResourceCategory.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the ResourceCategory.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your ResourceCategory a name.

    Returns
    -------
    ResourceCategory
        An object representing the new Labstep ResourceCategory.
    """
    params = {'name': name, **extraParams, 'is_template': 1}
    return newEntity(user, ResourceCategory, params)


def editResourceCategory(resourceCategory, name=None, deleted_at=None,
                         extraParams={}):
    """
    Edit an existing ResourceCategory.

    Parameters
    ----------
    resourceCategory (obj)
        The ResourceCategory to edit.
    name (str)
        The new name of the ResourceCategory.
    deleted_at (str)
        The timestamp at which the ResourceCategory is deleted/archived.

    Returns
    -------
    ResourceCategory
        An object representing the edited ResourceCategory.
    """
    params = {'name': name,
              'deleted_at': deleted_at,
              **extraParams}
    return editEntity(resourceCategory, params)


class ResourceCategory(PrimaryEntity):
    """
    Represents a Resource Category on Labstep.

    To see all attributes of the resource category run
    ::
        print(my_resource_category)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(my_resource_category.name)
        print(my_resource_category.id)
    """
    __entityName__ = 'resource'

    def edit(self, name=None, extraParams={}):
        """
        Edit an existing ResourceCategory.

        Parameters
        ----------
        name (str)
            The new name of the ResourceCategory.

        Returns
        -------
        :class:`~labstep.resourceCategory.ResourceCategory`
            An object representing the edited ResourceCategory.

        Example
        -------
        ::

            my_resource_category = user.getResourceCategory(17000)
            my_resource_category.edit(name='A New ResourceCategory Name')
        """
        return editResourceCategory(self, name, extraParams=extraParams)

    def delete(self):
        """
        Delete an existing ResourceCategory.

        Example
        -------
        ::

            my_resource_category = user.getResourceCategory(17000)
            my_resource_category.delete()
        """
        return editResourceCategory(self, deleted_at=getTime())

    def getResourceTemplate(self):
        '''
        Returns the metadata template for resources of this category.

        Example
        -------
        ::

            my_resource_category = user.getResourceCategory(17000)
            resourceTemplate = my_resource_category.getResourceTemplate()

            resourceTemplate.getMetadata()
            resourceTemplate.addMetadata('Vendor')
        '''
        return ResourceTemplate(self.__data__, self.__user__)

    def getItemTemplate(self):
        '''
        Returns the item template for resources of this category.

        Example
        -------
        ::

            my_resource_category = user.getResourceCategory(17000)
            itemTemplate = my_resource_category.getItemTemplate()

            itemTemplate.getMetadata()
            itemTemplate.addMetadata('Vendor')
        '''
        self.update()
        return ResourceItem(self.resource_item_template, self.__user__)

    def enableItemTemplate(self):
        '''
        Enable an item template for this resource category.
        This template will be used to initialise new items for resources in this category, unless the resource has it's own custom template.

        Returns
        -------
        None

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            my_resource.enableCustomItemTemplate()

            itemTemplate = my_resource.getItemTemplate()

            itemTemplate.addMetadata('Expiry Date')

        '''
        self.update()
        if self.resource_item_template is None:
            newResourceItem(self.__user__, self.id, extraParams={'is_template': 1})
        else:
            self.getItemTemplate().edit(extraParams={'deleted_at': None})

    def disableItemTemplate(self):
        '''
        Disable the item template for this resource category.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            my_resource.disableCustomItemTemplate()
        '''
        self.getItemTemplate().delete()


class ResourceTemplate(Entity):
    __entityName__ = 'resource'

    def addMetadata(self, fieldName, fieldType="default",
                    value=None, date=None,
                    number=None, unit=None,
                    filepath=None,
                    extraParams={}):
        """
        Add Metadata to the Resource Template.

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

            resource_category = user.getResourceCategory(17000)
            metadata = my_resource_category.addMetadata("Refractive Index",
                                                        value="1.73")
        """
        return addMetadataTo(self, fieldName, fieldType, value, date,
                             number, unit, filepath=filepath, extraParams=extraParams)

    def getMetadata(self):
        """
        Retrieve the Metadata of the Resource Template.

        Returns
        -------
        :class:`~labstep.metadata.Metadata`
            An array of Metadata objects for the Resource.

        Example
        -------
        ::

            entity = user.getResourceCategory(17000)
            metadatas = entity.getMetadata()
            metadatas[0].attributes()
        """
        return getMetadata(self)
