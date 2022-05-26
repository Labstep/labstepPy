#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entityWithMetadata.model import EntityWithMetadata
from labstep.generic.entityWithComments.model import EntityWithComments
from labstep.service.helpers import getTime
from labstep.constants import UNSPECIFIED


class ResourceLocation(EntityWithMetadata, EntityWithComments):
    """
    Represents a Resource Location on Labstep.

    To see all attributes of the resource location run
    ::
        print(my_resource_location)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(my_resource_location.name)
        print(my_resource_location.id)
    """

    __entityName__ = "resource-location"
    __hasParentGroup__ = True

    def edit(self, name=UNSPECIFIED, extraParams={}):
        """
        Edit an existing ResourceLocation.

        Parameters
        ----------
        name (str)
            The new name of the ResourceLocation.

        Returns
        -------
        :class:`~labstep.entities.resourceLocation.model.ResourceLocation`
            An object representing the edited ResourceLocation.

        Example
        -------
        ::

            resource_location = user.getResourceLocation(123)
            resource_location.edit(name='A New ResourceLocation Name')
        """
        import labstep.entities.resourceLocation.repository as resourceLocationRepository

        return resourceLocationRepository.editResourceLocation(
            self, name, extraParams=extraParams
        )

    def delete(self):
        """
        Delete an existing ResourceLocation.

        Returns
        -------
        :class:`~labstep.entities.resourceLocation.model.ResourceLocation`
            An object representing the deleted ResourceLocation.

        Example
        -------
        ::

            resource_location = user.getResourceLocation(123)
            resource_location.delete()
        """
        return self.edit(extraParams={"deleted_at": getTime()})

    def getItems(self, count=100, extraParams={}):
        """
        Get a list of items in this location.

        Returns
        -------
        List[:class:`~labstep.entities.resourceItem.model.ResourceItem`]
            An array of items in the ResourceLocation.

        Example
        -------
        ::

            resource_location = user.getResourceLocation(123)
            items = resource_location.getItems() 
        """
        import labstep.entities.resourceItem.repository as resourceItemRepository
        return resourceItemRepository.getResourceItems(self.__user__, count=count, extraParams={'resource_location_id': self.id, **extraParams})
