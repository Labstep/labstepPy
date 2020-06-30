#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylama:ignore=E501

import requests
from .config import API_ROOT
from .entity import Entity, getEntity, getEntities, newEntity, editEntity, getHeaders
from .helpers import url_join, handleError


def getResourceLocation(user, resource_location_id):
    """
    Retrieve a specific Labstep ResourceLocation.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    resource_location_id (int)
        The id of the ResourceLocation to retrieve.

    Returns
    -------
    ResourceLocation
        An object representing a Labstep ResourceLocation.
    """
    return getEntity(user, ResourceLocation, id=resource_location_id)


def getResourceLocations(user, count=100, search_query=None, tag_id=None,
                         extraParams={}):
    """
    Retrieve a list of a user's ResourceLocations on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    count (int)
        The number of ResourceLocations to retrieve.
    search_query (str)
        Search for ResourceLocations with this 'name'.
    tag_id (int)
        The id of the Tag to retrieve.

    Returns
    -------
    ResourceLocations
        A list of ResourceLocation objects.
    """
    params = {'search_query': search_query,
              'tag_id': tag_id,
              **extraParams}
    return getEntities(user, ResourceLocation, count, params)


def newResourceLocation(user, name, outer_location_id=None, extraParams={}):
    """
    Create a new Labstep ResourceLocation.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the ResourceLocation.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your ResourceLocation a name.

    outer_location_id (int)
        Id of existing location to create the location within

    Returns
    -------
    ResourceLocation
        An object representing the new Labstep ResourceLocation.
    """
    params = {'name': name, 'outer_location_id': outer_location_id, **extraParams}
    return newEntity(user, ResourceLocation, params)


def editResourceLocation(resourceLocation, name, extraParams={}):
    """
    Edit an existing ResourceLocation.

    Parameters
    ----------
    resourceLocation (obj)
        The ResourceLocation to edit.
    name (str)
        The new name of the ResourceLocation.
    deleted_at (str)
        The timestamp at which the ResourceLocation is deleted/archived.

    Returns
    -------
    ResourceLocation
        An object representing the edited ResourceLocation.
    """
    params = {'name': name, **extraParams}
    return editEntity(resourceLocation, params)


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
    __entityName__ = 'resource-location'

    def edit(self, name=None, extraParams={}):
        """
        Edit an existing ResourceLocation.

        Parameters
        ----------
        name (str)
            The new name of the ResourceLocation.

        Returns
        -------
        :class:`~labstep.resourceLocation.ResourceLocation`
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
        return editResourceLocation(self, name, extraParams=extraParams)

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
        headers = getHeaders(self.__user__)
        url = url_join(API_ROOT, "/api/generic/", ResourceLocation.__entityName__,
                       str(self.id))
        r = requests.delete(url, headers=headers)
        handleError(r)
        return None

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
        :class:`~labstep.comment.Comment`
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
        :class:`~labstep.resourceLocation.ResourceLocation`
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
