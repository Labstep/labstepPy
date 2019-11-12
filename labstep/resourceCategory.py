#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .entity import getEntity, getEntities, newEntity, editEntity
from .helpers import getTime, update
from .comment import addCommentWithFile
from .tag import tag


def getResourceCategory(user, resourceCategory_id):
    """
    Retrieve a specific Labstep ResourceCategory.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    resourceCategory_id (int)
        The id of the ResourceCategory to retrieve.

    Returns
    -------
    ResourceCategory
        An object representing a Labstep ResourceCategory.
    """
    return getEntity(user, ResourceCategory, id=resourceCategory_id)


def getResourceCategorys(user, count=100, search_query=None, tag_id=None):
    """
    Retrieve a list of a user's ResourceCategorys on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    count (int)
        The number of ResourceCategorys to retrieve.
    search_query (str)
        Search for ResourceCategorys with this 'name'.
    tag_id (int)
        The id of the Tag to retrieve.

    Returns
    -------
    ResourceCategorys
        A list of ResourceCategory objects.
    """
    metadata = {'search_query': search_query,
                'tag_id': tag_id}
    return getEntities(user, ResourceCategory, count, metadata)


def newResourceCategory(user, name):
    """
    Create a new Labstep ResourceCategory.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the ResourceCategory.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your ResourceCategory a name.

    Returns
    -------
    ResourceCategory
        An object representing the new Labstep ResourceCategory.
    """
    metadata = {'name': name}
    return newEntity(user, ResourceCategory, metadata)


def editResourceCategory(resourceCategory, name=None, deleted_at=None):
    """
    Edit an existing ResourceCategory.

    Parameters
    ----------
    resourceCategory (obj)
        The ResourceCategory to edit.
    name (str)
        The new name of the Experiment.
    deleted_at (str)
        The timestamp at which the ResourceCategory is deleted/archived.

    Returns
    -------
    ResourceCategory
        An object representing the edited ResourceCategory.
    """
    metadata = {'name': name,
                'deleted_at': deleted_at}
    return editEntity(resourceCategory, metadata)


class ResourceCategory:
    __entityName__ = 'resource-category'

    def __init__(self, data, user):
        self.__user__ = user
        update(self, data)

    # functions()
    def edit(self, name=None):
        """
        Edit an existing ResourceCategory.

        Parameters
        ----------
        name (str)
            The new name of the ResourceCategory.

        Returns
        -------
        :class:`~labstep.resourceCategory.ResourceCategory`
            An object representing the edited ResourceCategory.

        Example
        -------
        .. code-block::

            my_resourceCategory = user.getResourceCategory(17000)
            my_resourceCategory.edit(name='A New ResourceCategory Name')
        """
        return editResourceCategory(self, name)

    def delete(self):
        """
        Delete an existing ResourceCategory.

        Example
        -------
        .. code-block::

            my_resourceCategory = user.getResourceCategory(17000)
            my_resourceCategory.delete()
        """
        return editResourceCategory(self, deleted_at=getTime())

    def addComment(self, body, filepath=None):
        """
        Add a comment and/or file to a Labstep ResourceCategory.

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

            my_resourceCategory = user.getResourceCategory(17000)
            my_resourceCategory.addComment(body='I am commenting!',
                                filepath='pwd/file_to_upload.dat')
        """
        return addCommentWithFile(self, body, filepath)

    def addTag(self, name):
        """
        Add a tag to the ResourceCategory (creates a
        new tag if none exists).

        Parameters
        ----------
        name (str)
            The name of the tag to create.

        Returns
        -------
        :class:`~labstep.resourceCategory.ResourceCategory`
            The ResourceCategory that was tagged.

        Example
        -------
        .. code-block::

            my_resourceCategory = user.getResourceCategory(17000)
            my_resourceCategory.addTag(name='My Tag')
        """
        tag(self, name)
        return self
