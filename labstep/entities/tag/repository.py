#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

import json
from labstep.service.config import configService
from labstep.service.helpers import url_join, handleKeyword, getHeaders
from labstep.entities.tag.model import Tag
from labstep.service.request import requestService
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def getTags(user, count=1000, type=UNSPECIFIED, search_query=UNSPECIFIED, extraParams={}):
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
    params = {
        "search_query": search_query,
        "type": handleKeyword(type),
        **extraParams,
    }
    return entityRepository.getEntities(user, Tag, count, params)


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
    key = entity.__entityName__.replace("-", "_") + "_id"
    filterParams = {key: entity.id}
    return entityRepository.getEntities(
        entity.__user__, Tag, count=count, filterParams=filterParams
    )


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
    params = {"name": name, "type": handleKeyword(type), **extraParams}
    return entityRepository.newEntity(user, Tag, params)


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
    url = url_join(
        configService.getHost(),
        "api/generic/",
        entityName,
        str(entity.id),
        tag.__entityName__,
        str(tag.id),
    )
    response = requestService.put(url, headers=headers)
    return json.loads(response.content)


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
    type = (entity.__entityName__).replace("-", "_")

    tags = getTags(
        user,
        type=type,
        search_query=name,
        extraParams={"group_id": user.activeWorkspace},
    )
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
    params = {"name": name, **extraParams}
    return entityRepository.editEntity(tag, params)


def deleteTag(tag):
    headers = getHeaders(tag.__user__)
    url = url_join(configService.getHost(), "/api/generic/",
                   Tag.__entityName__, str(tag.id))
    requestService.delete(url, headers=headers)
    return None
