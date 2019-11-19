#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .entity import getEntity, getEntities, newEntity, editEntity
from .helpers import getTime, update
from .comment import addCommentWithFile
from .tag import tag


def getResourceLocation(user, resourceLocation_id):
    """
    Retrieve a specific Labstep ResourceLocation.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    resourceLocation_id (int)
        The id of the ResourceLocation to retrieve.

    Returns
    -------
    ResourceLocation
        An object representing a Labstep ResourceLocation.
    """
    return getEntity(user, ResourceLocation, id=resourceLocation_id)


def getResourceLocations(user, count=100, search_query=None, tag_id=None):
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
    metadata = {'search_query': search_query,
                'tag_id': tag_id}
    return getEntities(user, ResourceLocation, count, metadata)


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


def editResourceLocation(resourceLocation, name=None, deleted_at=None):
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
    metadata = {'name': name,
                'deleted_at': deleted_at}
    return editEntity(resourceLocation, metadata)


class ResourceLocation:
    __entityName__ = 'order-request'

    def __init__(self, data, user):
        self.__user__ = user
        update(self, data)

    # functions()
    def edit(self, name=None):
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

            my_resourceLocation = user.getResourceLocation(17000)
            my_resourceLocation.edit(name='A New ResourceLocation Name')
        """
        return editResourceLocation(self, name)

    def delete(self):
        """
        Delete an existing ResourceLocation.

        Example
        -------
        .. code-block::

            my_resourceLocation = user.getResourceLocation(17000)
            my_resourceLocation.delete()
        """
        return editResourceLocation(self, deleted_at=getTime())

    def addComment(self, body, filepath=None):
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

            my_resourceLocation = user.getResourceLocation(17000)
            my_resourceLocation.addComment(body='I am commenting!',
                                filepath='pwd/file_to_upload.dat')
        """
        return addCommentWithFile(self, body, filepath)

    def addTag(self, name):
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

            my_resourceLocation = user.getResourceLocation(17000)
            my_resourceLocation.addTag(name='My Tag')
        """
        tag(self, name)
        return self
