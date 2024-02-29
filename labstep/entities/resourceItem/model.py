#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.resourceLocation.repository import getResourceLocation
from labstep.generic.entityWithAssign.model import EntityWithAssign
from labstep.generic.entityWithComments.model import EntityWithComments
from labstep.generic.entityWithMetadata.model import EntityWithMetadata
from labstep.generic.entity.model import Entity
from labstep.service.helpers import getTime
from labstep.constants import UNSPECIFIED


class ResourceItem(EntityWithMetadata, EntityWithComments, EntityWithAssign):
    """
    Represents a Resource Item on Labstep.

    To see all attributes of the resource item run
    ::
        print(my_resource_item)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(my_resource_item.name)
        print(my_resource_item.id)
    """

    __entityName__ = "resource-item"

    def edit(
        self,
        name=UNSPECIFIED,
        availability=UNSPECIFIED,
        amount=UNSPECIFIED,
        unit=UNSPECIFIED,
        resource_location_guid=UNSPECIFIED,
        extraParams={},
        **kwargs
    ):
        """
        Edit an existing ResourceItem.

        Parameters
        ----------
        name (str)
            The new name of the ResourceItem.
        availability (str)
            The availability of the ResourceItem. Options are:
            "available" and "unavailable".
        amount (float)
            The quantity of the ResourceItem.
        unit (str)
            The unit of the quantity.
        resource_location_guid (str)
            The guid of the :class:`~labstep.entities.resourceLocation.model.ResourceLocation` of the ResourceItem.

        Returns
        -------
        :class:`~labstep.entities.resourceItem.model.ResourceItem`
            An object representing the edited ResourceItem.

        Example
        -------
        ::

            my_resource_item = user.getResourceItem(17000)
            my_resource_item.edit(name='A New ResourceItem Name')
        """
        import labstep.entities.resourceItem.repository as resourceItemRepository

        if 'quantity_amount' in kwargs:
            amount = kwargs['quantity_amount']

        if 'quantity_unit' in kwargs:
            unit = kwargs['quantity_unit']

        return resourceItemRepository.editResourceItem(
            self,
            name=name,
            availability=availability,
            amount=amount,
            unit=unit,
            resource_location_guid=resource_location_guid,
            extraParams=extraParams,
        )

    def delete(self):
        """
        Delete an existing ResourceItem.

        Example
        -------
        ::

            my_resource_item = user.getResourceItem(17000)
            my_resource_item.delete()
        """
        import labstep.entities.resourceItem.repository as resourceItemRepository

        return resourceItemRepository.editResourceItem(self, deleted_at=getTime())

    def getData(self):
        """
        Returns data linked to this resource via experiments.

        Returns
        -------
        List[:class:`~labstep.entities.experimentDataField.model.ExperimentDataField`]


        Example
        -------
        ::

            my_resource = user.getResource(17000)
            my_resource.getData()
        """
        import labstep.entities.experimentDataField.repository as experimentDataFieldRepository

        return experimentDataFieldRepository.getDataFields(self)

    def setLocation(self, resource_location_guid, position=None, size=[1, 1]):
        """
        Set the location of the item and the position within the location.

        Parameters
        ----------
        resource_location_guid (str)
            The guid of location to put the item
        position ([x: int,y: int])
            Optional: The position within the location to set as [x,y] coordinates
        size ([w: int,h: int])
            Optional: Specify the width / height the item takes up in the location (defaults to [1,1])


        Example
        -------
        ::

            item = user.getResourceItem(17000)
            location = user.getResourceLocation(12434)
            item.setLocation(location,[1,3])
        """
        self.edit(resource_location_guid=resource_location_guid)

        if position is not None:

            from labstep.entities.resourceLocation.repository import setPosition
            from labstep.entities.resourceLocation.model import ResourceLocation

            setPosition(entity=self,
                        location=ResourceLocation(
                            {'guid': resource_location_guid}, self.__user__),
                        position=position,
                        size=size)

    def getLocation(self):
        """
        Returns details on the location of the item as a dictionary of the form:


        {
            'resource_location': :class:`~labstep.entities.resourceLocation.model.ResourceLocation`,
            'position': [x (int),y (int)],
            'size': [w (int),h (int)]
        }
        """
        from labstep.entities.resourceLocation.repository import getPosition

        self.update()

        if getattr(self, 'resource_location', None) is not None:

            location = getResourceLocation(
                self.__user__, self.resource_location['guid'])

            position = getPosition(self, location)

            if position is None:
                return {
                    'resource_location': location,
                    'position': None,
                    'size': None
                }

            return {
                'resource_location': location,
                'position': [position['x'], position['y']],
                'size': [position['w'], position['h']]
            }
