#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .constants import commentEntityName
from .core import editEntity, newEntity
from .helpers import update
from .file import newFile


def addComment(user, entity, body, file=None):
    """
    Add a comment to a Labstep entity such as an Experiment or Resource.

    Parameters
    ----------
    user (obj)
        The Labstep user adding a comment.
        Must have property 'api_key'. See 'login'.
    entity (obj)
        The Labstep entity to comment on. Must have
        'thread' property with property 'id'.
    body (str)
        The body of the comment.
    file (obj)
        A Labstep File entity to attach to the comment. Must have 'id'.
    Returns
    -------
    comment
        An object representing a comment on labstep.
    """
    threadId = entity.thread['id']
    if file is None:
        lsFile = None
    else:
        lsFile = [list(file.keys())[0]]
    data = {'body': body,
            'thread_id': threadId,
            'file_id': lsFile}
    return newEntity(user, commentEntityName, data)


def addCommentWithFile(user, entity, body, filepath):
    if filepath is not None:
        lsFile = newFile(user, filepath)
    else:
        lsFile = None
    return addComment(user, entity, body, lsFile)


def editComment(user, comment_id, comment):
    """
    Edit an existing comment/caption.

    Parameters
    ----------
    user (obj)
        The labstep user. Must have property 'api_key'. See 'login'.
    comment_id (obj)
        The id of the comment/caption to edit.
    comment (str)
        The body of the new comment.

    Returns
    -------
    comment
        An object representing the editted comment.
    """
    metadata = {'body': comment}
    return editEntity(user, commentEntityName, comment_id, metadata)


class Comment:
    def __init__(self, data, user):
        self.__user__ = user
        self.__entityName__ = commentEntityName
        update(self, data)
