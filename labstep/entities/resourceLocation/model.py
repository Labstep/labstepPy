#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

import requests
from labstep.service.config import API_ROOT
from labstep.generic.entity.model import Entity
from labstep.service.helpers import url_join, handleError, getHeaders, getTime


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

            # Get all ResourceLocations, since there is no function
            # to get one ResourceLocation.
            resource_locations = user.getResourceLocations()

            # Select the tag by using python index.
            resource_locations[1].edit(name='A New ResourceLocation Name')
        """
        from labstep.entities.resourceLocation.repository import resourceLocationRepository

        return resourceLocationRepository.editResourceLocation(
            self, name, extraParams=extraParams
        )

    def delete(self):
        """
        Delete an existing ResourceLocation.

        Parameters
        ----------
        resourceLocation (obj)
            The ResourceLocation to delete.

        Returns
        -------
        resourceLocation
            An object representing the ResourceLocation to delete.
        """
        return self.edit(extraParams={"deleted_at": getTime()})

    '''def addComment(self, body, filepath=None):
        """
        Add a comment and/or file to a Labstep ResourceLocation.

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

            # Get all ResourceLocations, since there is no function
            # to get one ResourceLocation.
            resource_locations = user.getResourceLocations()

            # Select the tag by using python index.
            resource_locations[1].addComment(body='I am commenting!',
                                             filepath='pwd/file_to_upload.dat')
        """
        return addCommentWithFile(self, body, filepath)'''

    '''def addTag(self, name):
        """
        Add a tag to the ResourceLocation (creates a
        new tag if none exists).

        Parameters
        ----------
        name (str)
            The name of the tag to create.

        Returns
        -------
        :class:`~labstep.entities.resourceLocation.model.ResourceLocation`
            The ResourceLocation that was tagged.

        Example
        -------
        ::

            # Get all ResourceLocations, since there is no function
            # to get one ResourceLocation.
            resource_locations = user.getResourceLocations()

            # Select the tag by using python index.
            resource_locations[1].addTag(name='My Tag')
        """
        tag(self, name)
        return self'''
