#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.service.helpers import getTime


class ResourceItem(Entity):
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
        name=None,
        availability=None,
        quantity_amount=None,
        quantity_unit=None,
        resource_location_id=None,
        extraParams={},
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
        quantity_amount (float)
            The quantity of the ResourceItem.
        quantity_unit (str)
            The unit of the quantity.
        resource_location_id (int)
            The id of the :class:`~labstep.entities.resourceLocation.model.ResourceLocation` of the ResourceItem.

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
        from labstep.entities.resourceItem.repository import resourceItemRepository

        return resourceItemRepository.editResourceItem(
            self,
            name=name,
            availability=availability,
            quantity_amount=quantity_amount,
            quantity_unit=quantity_unit,
            resource_location_id=resource_location_id,
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
        from labstep.entities.resourceItem.repository import resourceItemRepository

        return resourceItemRepository.editResourceItem(self, deleted_at=getTime())

    def addComment(self, body, filepath=None, extraParams={}):
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
        :class:`~labstep.entities.comment.model.Comment`
            The comment added.

        Example
        -------
        ::

            my_resource_item = user.getResourceItem(17000)
            my_resource_item.addComment(body='I am commenting!',
                                        filepath='pwd/file_to_upload.dat')
        """
        from labstep.entities.comment.repository import commentRepository

        return commentRepository.addCommentWithFile(
            self, body, filepath, extraParams=extraParams
        )

    def getComments(self, count=100, extraParams={}):
        """
        Retrieve the Comments attached to this Labstep Entity.

        Returns
        -------
        List[:class:`~labstep.entities.comment.model.Comment`]
            List of the comments attached.

        Example
        -------
        ::

            entity = user.getResource(17000)
            item = entity.getItems()[1]
            comments = item.getComments()
            comments[0].attributes()
        """
        from labstep.entities.comment.repository import commentRepository

        return commentRepository.getComments(self, count, extraParams=extraParams)

    def addMetadata(
        self,
        fieldName,
        fieldType="default",
        value=None,
        date=None,
        number=None,
        unit=None,
        filepath=None,
        extraParams={},
    ):
        """
        Add Metadata to a ResourceItem.

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
        :class:`~labstep.entities.metadata.model.Metadata`
            An object representing the new Labstep Metadata.

        Example
        -------
        ::

            my_resource_item = user.getResourceItem(17000)
            metadata = my_resource_item.addMetadata("Refractive Index",
                                                    value="1.73")
        """
        from labstep.entities.metadata.repository import metadataRepository

        return metadataRepository.addMetadataTo(
            self,
            fieldName,
            fieldType=fieldType,
            value=value,
            date=date,
            number=number,
            unit=unit,
            filepath=filepath,
            extraParams=extraParams,
        )

    def getMetadata(self):
        """
        Retrieve the Metadata of a Labstep ResourceItem.

        Returns
        -------
        List[:class:`~labstep.entities.resource.model.ResourceItem`]
            An array of Metadata objects for the ResourceItem.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            my_resource_item = my_resource.getResourceItem(17000)
            metadata = my_resource_item.getMetadata()
            metadatas[0].attributes()
        """
        from labstep.entities.metadata.repository import metadataRepository

        return metadataRepository.getMetadata(self)
