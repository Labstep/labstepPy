#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylama:ignore=E501

from .primaryEntity import PrimaryEntity
from .entity import getEntity, getEntities, newEntity, editEntity
from .helpers import getTime
from .metadata import addMetadataTo, getMetadata


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
    params = {**filterParams, **extraParams}
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
    params = {'name': name, **extraParams}
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
    __entityName__ = 'resource-category'

    def edit(self, name, extraParams={}):
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

    def addMetadata(self, fieldName, fieldType="default",
                    value=None, date=None,
                    number=None, unit=None,
                    extraParams={}):
        """
        Add Metadata to a Resource Category.

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

            resource_category = user.getResourceCategory(17000)
            metadata = my_resource_category.addMetadata("Refractive Index",
                                                        value="1.73")
        """
        return addMetadataTo(self, fieldName, fieldType, value, date,
                             number, unit, extraParams=extraParams)

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

            entity = user.getResourceCategory(17000)
            metadatas = entity.getMetadata()
            metadatas[0].attributes()
        """
        return getMetadata(self)
