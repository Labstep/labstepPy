#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .entity import getEntity, getEntities, newEntity, editEntity
from .helpers import getTime, update
from .comment import addCommentWithFile
from .tag import tag


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
    return getEntity(user, Resource, id=resource_id)


def getResources(user, count=100, search_query=None, tag_id=None,
                 extraParams={}):
    """
    Retrieve a list of a user's Resources on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    count (int)
        The number of Resources to retrieve.
    search_query (str)
        Search for Resources with this 'name'.
    tag_id (int)
        The id of the Tag to retrieve.
    extraParams (dict)
        Dictionary of extra filter parameters

    Returns
    -------
    resources
        A list of Resource objects.
    """
    filterParams = {'search_query': search_query,
                    'tag_id': tag_id}

    params = {**filterParams, **extraParams}

    return getEntities(user, Resource, count, params)


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
    fields = {'name': name}
    return newEntity(user, Resource, fields)


def editResource(resource, name=None, deleted_at=None):
    """
    Edit an existing Resource.

    Parameters
    ----------
    resource (obj)
        The Resource to edit.
    name (str)
        The new name of the Experiment.
    deleted_at (str)
        The timestamp at which the Resource is deleted/archived.

    Returns
    -------
    resource
        An object representing the edited Resource.
    """
    fields = {'name': name,
              'deleted_at': deleted_at}
    return editEntity(resource, fields)


class Resource:
    __entityName__ = 'resource'

    def __init__(self, fields, user):
        self.__user__ = user
        update(self, fields)

    # functions()
    def edit(self, name=None):
        """
        Edit an existing Resource.

        Parameters
        ----------
        name (str)
            The new name of the Resource.

        Returns
        -------
        :class:`~labstep.resource.Resource`
            An object representing the edited Resource.

        Example
        -------
        .. code-block::

            my_resource = user.getResource(17000)
            my_resource.edit(name='A New Resource Name')
        """
        return editResource(self, name)

    def delete(self):
        """
        Delete an existing Resource.

        Example
        -------
        .. code-block::

            my_resource = user.getResource(17000)
            my_resource.delete()
        """
        return editResource(self, deleted_at=getTime())

    def addComment(self, body, filepath=None):
        """
        Add a comment and/or file to a Labstep Resource.

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

            my_resource = user.getResource(17000)
            my_resource.addComment(body='I am commenting!',
                                filepath='pwd/file_to_upload.dat')
        """
        return addCommentWithFile(self, body, filepath)

    def addTag(self, name):
        """
        Add a tag to the Resource (creates a
        new tag if none exists).

        Parameters
        ----------
        name (str)
            The name of the tag to create.

        Returns
        -------
        :class:`~labstep.resource.Resource`
            The Resource that was tagged.

        Example
        -------
        .. code-block::

            my_resource = user.getResource(17000)
            my_resource.addTag(name='My Tag')
        """
        tag(self, name)
        return self
