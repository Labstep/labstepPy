#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.service.helpers import getTime


class ResourceLocation(Entity):
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

    def edit(self, name=None, extraParams={}):
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
        from labstep.entities.resourceLocation.repository import resourceLocationRepository

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

    def addComment(self, body, filepath=None, extraParams={}):
        """
        Add a comment and/or file to a Labstep ResourceLocation.

        Parameters
        ----------
        body (str)
            The body of the comment.
        filepath (str)
            Filepath of file to attach to the comment

        Returns
        -------
        :class:`~labstep.entities.comment.model.Comment`
            The comment added.

        Example
        -------
        ::

            resource_location = user.getResourceLocation(123)
            resource_location.edit(name='A New ResourceLocation Name')
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
        Add Metadata to a ResourceLocation.

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

            resource_location = user.getResourceLocation(123)
            resource_location.addMetadata("Refractive Index",
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
        Retrieve the Metadata of a Labstep ResourceLocation.

        Returns
        -------
        List[:class:`~labstep.entities.metadata.model.Metadata`]
            An array of Metadata objects for the ResourceLocation.

        Example
        -------
        ::

            resource_location = user.getResourceLocation(123)
            metadata = resource_location.getMetadata()
        """
        from labstep.entities.metadata.repository import metadataRepository

        return metadataRepository.getMetadata(self)

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
        from labstep.entities.resourceItem.repository import resourceItemRepository
        return resourceItemRepository.getResourceItems(self.__user__, count=count, extraParams={'resource_location_id': self.id, **extraParams})
