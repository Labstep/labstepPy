#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entityWithMetadata.model import EntityWithMetadata
from labstep.generic.entityWithComments.model import EntityWithComments
from labstep.generic.entityWithAssign.model import EntityWithAssign
from labstep.service.helpers import getTime
from labstep.constants import UNSPECIFIED


class ResourceLocation(EntityWithMetadata, EntityWithComments, EntityWithAssign):
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
    __hasGuid__ = True

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

    def getItems(self, count=UNSPECIFIED, extraParams={}):
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
        return resourceItemRepository.getResourceItems(self.__user__, count=count, extraParams={'resource_location_guid': self.guid, **extraParams})

    def getInnerLocations(self, extraParams={}):
        """
        Returns a list of the sub-locations within this location.

        Returns
        -------
        List[:class:`~labstep.entities.resourceLocation.model.ResourceLocation`]
            An array of locations in the ResourceLocation.

        Example
        -------
        ::

            resource_location = user.getResourceLocation(123)
            inner_locations = resource_location.getInnerLocations()
        """
        from labstep.entities.resourceLocation.repository import getResourceLocations

        return getResourceLocations(self.__user__, count=UNSPECIFIED, extraParams={
            'outer_location_guid': self.guid,
            **extraParams
        })

    def addInnerLocation(self, name, position=None, size=[1, 1], extraParams={}):
        """
        Adds a new inner location within this location.

        Parameters
        ----------
        name (str)
            The name of the new inner location.
        position ([x: int,y: int])
            Optional: The position within the outer location to set as [x,y] coordinates
        size ([w: int,h: int])
            Optional: Specify the width / height the item takes up in the outer location (defaults to [1,1])

        Returns
        -------
        :class:`~labstep.entities.resourceLocation.model.ResourceLocation`
            An object representing the new inner location.

        Example
        -------
        ::

            resource_location = user.getResourceLocation(123)
            resource_location.edit(name='A New ResourceLocation Name')

        """
        from labstep.entities.resourceLocation.repository import newResourceLocation, setPosition

        innerLocation = newResourceLocation(
            self.__user__, name=name, outer_location_guid=self.guid, extraParams=extraParams)

        if position is not None:
            setPosition(entity=innerLocation,
                        location=self,
                        position=position,
                        size=size)

        return innerLocation

    def setOuterLocation(self, outer_location_guid, position=None, size=[1, 1]):
        """
        Set the outer location for the location and the position within the outer location.

        Parameters
        ----------
        outer_location_guid (str)
            The guid of outer location for this location
        position ([x: int,y: int])
            Optional: The position within the outer location to set as [x,y] coordinates
        size ([w: int,h: int])
            Optional: Specify the width / height the item takes up in the outer location (defaults to [1,1])


        Example
        -------
        ::

            inner_location = user.getResourceLocation(1)
            outer_location = user.getResourceLocation(2)
            inner_location.setOuterLocation(outer_location_guid,position=[1,3],size=[1,1])
        """
        self.edit(extraParams={"outer_location_guid": outer_location_guid})

        if position is not None:

            from labstep.entities.resourceLocation.repository import setPosition
            from labstep.entities.resourceLocation.model import ResourceLocation

            setPosition(entity=self,
                        location=ResourceLocation(
                            {'guid': outer_location_guid}, self.__user__),
                        position=position,
                        size=size)

    def createPositionMap(self, rowCount, columnCount, data={}):
        """
        Creates a map of the location to specify the position of items / sub-locations within it.

        Parameters
        ----------
        rowCount (int)
            The number of rows in the map
        columnCount (int)
            The number of columns in the map
        data (dict)
            Optional: Dictionary specifying the position of the items / sub-locations within the location


        Example
        -------
        ::

            location = user.getResourceLocation(1)
            location.createPositionMap(n_rows=10,n_col=10)
        """

        return self.edit(extraParams={
            'map_data': {
                'rowCount': rowCount,
                'columnCount': columnCount,
                'data': data
            }
        })
