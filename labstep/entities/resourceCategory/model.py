#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entityWithSharing.model import EntityWithSharing
from labstep.service.helpers import getTime
from labstep.entities.resourceTemplate.model import ResourceTemplate
from labstep.entities.resourceItem.model import ResourceItem
from labstep.constants import UNSPECIFIED


class ResourceCategory(EntityWithSharing):
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

    __entityName__ = "resource"

    def edit(self, name=UNSPECIFIED, extraParams={}):
        """
        Edit an existing ResourceCategory.

        Parameters
        ----------
        name (str)
            The new name of the ResourceCategory.

        Returns
        -------
        :class:`~labstep.entities.resourceCategory.model.ResourceCategory`
            An object representing the edited ResourceCategory.

        Example
        -------
        ::

            my_resource_category = user.getResourceCategory(17000)
            my_resource_category.edit(name='A New ResourceCategory Name')
        """
        import labstep.entities.resourceCategory.repository as resourceCategoryRepository

        return resourceCategoryRepository.editResourceCategory(
            self, name, extraParams=extraParams
        )

    def delete(self):
        """
        Delete an existing ResourceCategory.

        Example
        -------
        ::

            my_resource_category = user.getResourceCategory(17000)
            my_resource_category.delete()
        """
        import labstep.entities.resourceCategory.repository as resourceCategoryRepository

        return resourceCategoryRepository.editResourceCategory(
            self, deleted_at=getTime()
        )

    def getResourceTemplate(self):
        """
        Returns the metadata template for resources of this category.

        Example
        -------
        ::

            my_resource_category = user.getResourceCategory(17000)
            resourceTemplate = my_resource_category.getResourceTemplate()

            resourceTemplate.getMetadata()
            resourceTemplate.addMetadata('Vendor')
        """
        return ResourceTemplate(self.__data__, self.__user__)

    def getItemTemplate(self):
        """
        Returns the item template for resources of this category.

        Example
        -------
        ::

            my_resource_category = user.getResourceCategory(17000)
            itemTemplate = my_resource_category.getItemTemplate()

            itemTemplate.getMetadata()
            itemTemplate.addMetadata('Vendor')
        """
        self.update()
        return ResourceItem(self.resource_item_template, self.__user__)

    def enableItemTemplate(self):
        """
        Enable an item template for this resource category.
        This template will be used to initialise new items for resources
        in this category, unless the resource has it's own custom template.

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

        """
        self.update()
        if self.resource_item_template is None:
            import labstep.entities.resourceItem.repository as resourceItemRepository

            resourceItemRepository.newResourceItem(
                self.__user__, self.id, extraParams={"is_template": 1}
            )
        else:
            self.getItemTemplate().edit(extraParams={"deleted_at": None})

    def disableItemTemplate(self):
        """
        Disable the item template for this resource category.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            my_resource.disableCustomItemTemplate()
        """
        self.getItemTemplate().delete()
