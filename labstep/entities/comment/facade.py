#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.comment.repository import commentRepository


def getComments(entity, count=100, extraParams={}):
    """
    Retrieve the Comments attached to a Labstep Entity.

    Parameters
    ----------
    entity (obj)
        The entity to retrieve Comments from.

    Returns
    -------
    comments
        List of the comments attached.
    """
    return commentRepository.getComments(entity, count, extraParams)


def addComment(entity, body, fileId=None, extraParams={}):
    """
    Add a comment to a Labstep entity such as an Experiment or Resource.

    Parameters
    ----------
    entity (obj)
        The Labstep entity to comment on. Must have
        'thread' property with property 'id'.
    body (str)
        The body of the comment.
    file (obj)
        A Labstep :class:`~labstep.file.File` entity to attach to the comment.
        Must have 'id'.

    Returns
    -------
    comment
        An object representing a comment on labstep.
    """
    return commentRepository.addComment(entity, body, fileId, extraParams)


def addCommentWithFile(entity, body, filepath, extraParams={}):
    """
    Add a comment with an attaching file.

    Parameters
    ----------
    entity (obj)
        The Labstep entity to comment on. Must have
        'thread' property with property 'id'.
    body (str)
        The body of the comment.
    filepath (str)
        A Labstep File entity to attach to the comment.
    """
    return commentRepository.addCommentWithFile(entity, body, filepath, extraParams)


def editComment(comment, body, extraParams={}):
    """
    Edit an existing comment/caption.

    Parameters
    ----------
    comment (obj)
        The comment/caption to edit.
    body (str)
        The body of the new comment.

    Returns
    -------
    comment
        An object representing the edited comment.
    """
    return commentRepository.editComment(comment, body, extraParams)
