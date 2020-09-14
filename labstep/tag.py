#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from .config import API_ROOT
from .entity import Entity, getEntities, newEntity, editEntity, getHeaders
from .helpers import (url_join, handleError, handleString)


def getTags(user, count=1000, type=None, search_query=None, extraParams={}):
    """
    Retrieve a list of the user's tags.

    Parameters
    ----------
    user (obj)
        The Labstep user.
        Must have property 'api_key'. See 'login'.
    count (int)
        The number of Tags to retrieve.
    type (str)
        Return only tags of a certain type. Options are:
        'experiment_workflow', 'protocol_collection',
        'resource', 'order_request'.
    search_query (str)
        Search for Tags with this 'name'.
    extraParams (dict)
        Dictionary of extra filter parameters.

    Returns
    -------
    tags
        A list of tag objects.
    """
    params = {'search_query': search_query,
              'type': handleString(type),
              **extraParams}
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


def newTag(user, name, type, extraParams={}):
    """
    Create a new Tag.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the Tag.
        Must have property 'api_key'. See 'login'.
    name (str)
        Name of the new Tag.
    type (str)
            Return only tags of a certain type. Options are:
            'experiment_workflow', 'protocol_collection',
            'resource', 'order_request'.

    Returns
    -------
    tag
        An object representing the new Labstep Tag.
    """
    params = {'name': name,
              'type': handleString(type),
              **extraParams}
    return newEntity(user, Tag, params)


def addTagTo(entity, tag):
    """
    Attach an existing tag to a Labstep entity.
    (See 'tag' for simplified tagging).

    Parameters
    ----------
    entity (obj)
        The Labstep entity to tag. Can be Resource,
        Experiment, or Protocol. Must have 'id'.
    tag (obj)
        The tag to attach. Must have an 'id' property.

    Returns
    -------
    entity
        An object representing the tagged entity.
    """
    entityName = entity.__entityName__

    headers = getHeaders(entity.__user__)
    url = url_join(API_ROOT, "api/generic/", entityName,
                   str(entity.id), tag.__entityName__, str(tag.id))
    r = requests.put(url, headers=headers)
    handleError(r)
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
    type = (entity.__entityName__).replace('-', '_')

    tags = getTags(user, type=type, search_query=name,
                   extraParams={'group_id': user.activeWorkspace})
    matchingTags = list(filter(lambda x: x.name.lower() == name.lower(), tags))

    if len(matchingTags) == 0:
        tag = newTag(user, name, type=type)
    else:
        tag = matchingTags[0]

    return addTagTo(entity, tag)


def editTag(tag, name, extraParams={}):
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
    params = {'name': name, **extraParams}
    return editEntity(tag, params)


class Tag(Entity):
    """
    Represents a Tag on Labstep.

    To see all attributes of a tag run
    ::
        print(my_tag)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(my_tag.name)
        print(my_tag.id)
    """
    __entityName__ = 'tag'
    __hasParentGroup__ = True

    def edit(self, name=None, extraParams={}):
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
        ::

            # Get all tags, since there is no function
            # to get one tag.
            tags = user.getTags()

            # Select the tag by using python index.
            tags[1].edit(name='A New Tag Name')
        """
        return editTag(self, name, extraParams=extraParams)

    def delete(self):
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
        headers = getHeaders(self.__user__)
        url = url_join(API_ROOT, "/api/generic/",
                       Tag.__entityName__,
                       str(self.id))
        r = requests.delete(url, headers=headers)
        handleError(r)
        return None
