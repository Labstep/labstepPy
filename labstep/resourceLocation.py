#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylama:ignore=E501

import requests
from .config import API_ROOT
from .entity import getEntities, newEntity, editEntity
from .helpers import url_join, handleError, update, showAttributes


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
    filterParams = {'search_query': search_query,
                    'tag_id': tag_id}
    params = {**filterParams, **extraParams}
    return getEntities(user, ResourceLocation, count, params)


def newResourceLocation(user, name):
    """
    Create a new Labstep ResourceLocation.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the ResourceLocation.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your ResourceLocation a name.

    Returns
    -------
    ResourceLocation
        An object representing the new Labstep ResourceLocation.
    """
    metadata = {'name': name}
    return newEntity(user, ResourceLocation, metadata)


def editResourceLocation(resourceLocation, name):
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
    metadata = {'name': name}
    return editEntity(resourceLocation, metadata)


def deleteResourceLocation(resourceLocation):
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
    headers = {'apikey': resourceLocation.__user__.api_key}
    url = url_join(API_ROOT, "/api/generic/", ResourceLocation.__entityName__,
                   str(resourceLocation.id))
    r = requests.delete(url, headers=headers)
    handleError(r)
    return None


class ResourceLocation:
    __entityName__ = 'resource-location'

    def __init__(self, data, user):
        self.__user__ = user
        update(self, data)

    # functions()
    def attributes(self):
        """
        Show all attributes of a ResourceLocation.

        Example
        -------
        .. code-block::

            # Use python index to select a ResourceLocation from the
            # getResourceLocations() list.
            my_resource_location = user.getResourceLocations()[1]
            my_resource_location.attributes()

        The output should look something like this:

        .. program-output:: python ../labstep/attributes/resourceLocation_attributes.py

        To inspect specific attributes of a ResourceLocation,
        for example, the ResourceLocation 'name', 'id', etc.:

        .. code-block::

            print(my_resource_location.name)
            print(my_resource_location.id)
        """
        return showAttributes(self)

    def edit(self, name):
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
        .. code-block::

            # Get all ResourceLocations, since there is no function
            # to get one ResourceLocation.
            resource_locations = user.getResourceLocations()

            # Select the tag by using python index.
            resource_locations[1].edit(name='A New ResourceLocation Name')
        """
        return editResourceLocation(self, name)

    def delete(self):
        """
        Delete an existing ResourceLocation.

        Example
        -------
        .. code-block::

            # Get all ResourceLocations, since there is no function
            # to get one ResourceLocation.
            resource_locations = user.getResourceLocations()

            # Select the tag by using python index.
            resource_locations[1].delete()
        """
        return deleteResourceLocation(self)

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
        .. code-block::

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
        .. code-block::

            # Get all ResourceLocations, since there is no function
            # to get one ResourceLocation.
            resource_locations = user.getResourceLocations()

            # Select the tag by using python index.
            resource_locations[1].addTag(name='My Tag')
        """
        tag(self, name)
        return self'''
