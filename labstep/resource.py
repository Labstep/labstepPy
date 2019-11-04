#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .entity import getEntity, getEntities, newEntity, editEntity
from .helpers import getTime, update
from .comment import addCommentWithFile
from .tag import tag

resourceEntityName = 'resource'


def getResource(user, resource_id):
    """
    Retrieve a specific Labstep Resource.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    resource_id (int)
        The id of the Resource to retrieve.

    Returns
    -------
    resource
        An object representing a Labstep Resource.
    """
    return getEntity(user, resourceEntityName, id=resource_id)


def getResources(user, count=100, search_query=None, tag_id=None):
    """
    Retrieve a list of a user's Resources on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    count (int)
        The number of Resources to retrieve.
    search_query (str)
        Search for Resources with this 'name'.
    tag_id (int)
        The id of the Tag to retrieve.

    Returns
    -------
    resources
        A list of Resource objects.
    """
    metadata = {'search_query': search_query,
                'tag_id': tag_id}
    return getEntities(user, resourceEntityName, count, metadata)


def newResource(user, name):
    """
    Create a new Labstep Resource.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the Resource.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your resource a name.

    Returns
    -------
    resource
        An object representing the new Labstep Resource.
    """
    metadata = {'name': name}
    return newEntity(user, resourceEntityName, metadata)


def editResource(user, resource, name=None, deleted_at=None):
    """
    Edit an existing Resource.

    Parameters
    ----------
    user (obj)
        The labstep user. Must have property 'api_key'. See 'login'.
    resource (obj)
        The Resource to edit.
    name (str)
        The new name of the Experiment.
    deleted_at (obj)
        The timestamp at which the Resource is deleted/archived.

    Returns
    -------
    resource
        An object representing the Resource to edit.
    """
    metadata = {'name': name,
                'deleted_at': deleted_at}
    return editEntity(user, resourceEntityName, resource.id, metadata)


class Resource:
    def __init__(self, data, user):
        self.__user__ = user
        self.__entityName__ = resourceEntityName
        update(self, data)

    # functions()
    def edit(self, name=None):
        """
        Edit an existing Resource.

        Parameters
        ----------
        name (str)
            The new name of the Resource.

        Example
        -------
        .. code-block:: python

            my_resource = LS.Resource(user.getResource(17000), user)
            my_resource.edit(name='A New Resource Name')
        """
        return editResource(self.__user__, self, name)

    def delete(self):
        """
        Delete an existing Resource.

        Example
        -------
        .. code-block:: python

            my_resource = LS.Resource(user.getResource(17000), user)
            my_resource.delete()
        """
        return editResource(self.__user__, self, deleted_at=getTime())

    def comment(self, body, filepath=None):
        """
        Add a comment to a Labstep Resource.

        Parameters
        ----------
        body (str)
            The body of the comment.
        filepath (obj)
            A Labstep File entity to attach to the comment,
            including the filepath.

        Example
        -------
        .. code-block:: python

            my_resource = LS.Resource(user.getResource(17000), user)
            my_resource.comment(body='I am commenting!',
                                filepath='pwd/file_to_upload.dat')
        """
        return addCommentWithFile(self.__user__, self, body, filepath)

    def addTag(self, name):
        """
        Add a tag to the Resource (creates a
        new tag if none exists).

        Parameters
        ----------
        name (str)
            The name of the tag to create.

        Example
        -------
        .. code-block:: python

            my_resource = LS.Resource(user.getResource(17000), user)
            my_resource.addTag(name='My Tag')
        """
        return tag(self.__user__, self, name)
