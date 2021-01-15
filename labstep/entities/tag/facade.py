#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.tag.repository import tagRepository


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
    return tagRepository.getTags(user, count, type, search_query, extraParams)


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
    return tagRepository.getAttachedTags(entity, count)


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
    return tagRepository.newTag(user, name, type, extraParams)


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
    return tagRepository.addTagTo(entity, tag)


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
    return tagRepository.tag(entity, name)


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
    return tagRepository.editTag(tag, name, extraParams)
