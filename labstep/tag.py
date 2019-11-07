#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from .config import API_ROOT
from .entity import getEntities, newEntity, editEntity
from .helpers import url_join, handleError, update


def getTags(user, count=1000, search_query=None):
    """
    Retrieve a list of the user's tags.

    Parameters
    ----------
    user (obj)
        The Labstep user.
        Must have property 'api_key'. See 'login'.
    count (int)
        The number of Tags to retrieve.
    search_query (str)
        Search for Tags with this 'name'.

    Returns
    -------
    tags
        A list of tag objects.
    """
    filterParams = {'search_query': search_query}
    return getEntities(user, Tag, count, filterParams)


def newTag(user, name):
    """
    Create a new Tag.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the Tag.
        Must have property 'api_key'. See 'login'.
    name (str)
        Name of the new Tag.

    Returns
    -------
    tag
        An object representing the new Labstep Tag.
    """
    fields = {'name': name}
    return newEntity(user, Tag, fields)


def addTagTo(entity, tag):
    """
    Attach an existing tag to a Labstep entity.
    (See 'tag' for simplified tagging).

    Parameters
    ----------
    entity (obj)
        The Labstep entity to tag. Can be Resource,
        Experiment, or Protocol. Must have 'id'.
    tag (str)
        The tag to attach. Must have an 'id' property.

    Returns
    -------
    entity
        An object representing the tagged entity.
    """
    entityName = entity.__entityName__

    headers = {'apikey': entity.__user__.api_key}
    url = url_join(API_ROOT, "api/generic/", entityName,
                   str(entity.id), tag.__entityName__, str(tag.id))
    r = requests.put(url, headers=headers)
    return json.loads(r.content)


def tag(entity, name):
    """
    Simple tagging of a Labstep entity (creates a
    new tag if none exists).

    Parameters
    ----------
    entity (obj)
        The Labstep entity to tag. Can be Resource,
        Experiment, or Protocol. Must have 'id'.
    name (str)
        The name of the tag to create.

    Returns
    -------
    entity
        An object representing the tagged entity.
    """
    user = entity.__user__
    tags = getTags(user, search_query=name)
    matchingTags = list(filter(lambda x: x.name == name, tags))

    if len(matchingTags) == 0:
        tag = newTag(user, name)
    else:
        tag = matchingTags[0]

    return addTagTo(entity, tag)


def editTag(tag, name):
    """
    Edit the name of an existing Tag.

    Parameters
    ----------
    tag (obj)
        The Tag to edit.
    name (str)
        The new name of the Tag.

    Returns
    -------
    tag
        An object representing the edited Tag.
    """
    fields = {'name': name}
    return editEntity(tag, fields)


def deleteTag(tag):
    """
    Delete an existing tag.

    Parameters
    ----------
    tag (obj)
        The tag to delete.

    Returns
    -------
    tag
        An object representing the tag to delete.
    """
    headers = {'apikey': tag.__user__.api_key}
    url = url_join(API_ROOT, "/api/generic/tag/", str(tag.id))
    r = requests.delete(url, headers=headers)
    handleError(r)
    return None


class Tag:
    __entityName__ = 'tag'

    def __init__(self, fields, user):
        self.__user__ = user
        update(self, fields)

    # functions()
    def edit(self, name):
        """
        Edit the name of an existing Tag.

        Parameters
        ----------
        name (str)
            The new name of the Tag.

        Returns
        -------
        :class:`~labstep.tag.Tag`
            An object representing the edited Tag.

        Example
        -------
        .. code-block::

            # Get all tags, since there is no function
            # to get one tag
            tags = user.getTags()

            # Select the tag by using
            # python indexing
            tags[1].edit(name='A New Tag Name')
        """
        return editTag(self, name)

    def delete(self):
        """
        Delete an existing Tag.

        Example
        -------
        .. code-block::

            # Get all tags, since there is
            # no function to get one tag
            tags = user.getTags()

            # Select the tag by using
            # python indexing
            tags[1].delete()
        """
        return deleteTag(self)
