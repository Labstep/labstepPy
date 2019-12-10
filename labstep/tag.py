#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from .config import API_ROOT
from .entity import getEntities, newEntity, editEntity
from .helpers import url_join, handleError, update, showAttributes


def getTags(user, count=1000, search_query=None, extraParams={}):
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
    extraParams (dict)
        Dictionary of extra filter parameters.

    Returns
    -------
    tags
        A list of tag objects.
    """
    filterParams = {'search_query': search_query}
    params = {**filterParams, **extraParams}
    return getEntities(user, Tag, count, params)


def getAttachedTags(entity, count=100):
    """
    Retrieve the Tags attached to a Labstep Entity.

    Parameters
    ----------
    entity (obj)
        The entity to retrieve Tags from.

    Returns
    -------
    tags
        List of the tags attached.
    """
    key = entity.__entityName__.replace('-', '_')+'_id'
    filterParams = {key: entity.id}
    return getEntities(entity.__user__, Tag, count=count,
                       filterParams=filterParams)


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
    tags = getTags(user, search_query=name, extraParams={
                   'group_id': user.activeWorkspace})
    matchingTags = list(filter(lambda x: x.name.lower() == name.lower(), tags))

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
    def attributes(self):
        """
        Show all attributes of a Tag.

        Example
        -------
        .. code-block::

            # Use python index to select a Tag from the
            # getTags() list.
            my_tag = user.getTags()[0]
            my_tag.attributes()

        The output should look something like this:

        .. program-output:: python ../labstep/attributes/tag_attributes.py

        To inspect specific attributes of a tag,
        for example, the tag 'name', 'id', etc.:

        .. code-block::

            print(my_tag.name)
            print(my_tag.id)
        """
        return showAttributes(self)

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
            # to get one tag.
            tags = user.getTags()

            # Select the tag by using python index.
            tags[1].edit(name='A New Tag Name')
        """
        return editTag(self, name)

    def delete(self):
        """
        Delete an existing Tag.

        Example
        -------
        .. code-block::

            # Get all tags, since there is no function
            # to get one tag.
            tags = user.getTags()

            # Select the tag by using python index.
            tags[1].delete()
        """
        return deleteTag(self)
