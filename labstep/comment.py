#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .entity import editEntity, newEntity
from .helpers import update
from .file import newFile


def addComment(entity, body, file=None):
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
    return newEntity(entity.__user__, Comment, data)


def addCommentWithFile(entity, body, filepath):
    if filepath is not None:
        lsFile = newFile(entity.__user__, filepath)
    else:
        lsFile = None
    return addComment(entity, body, lsFile)


def editComment(comment, body):
    """
    Edit an existing comment/caption.

    Parameters
    ----------
    user (obj)
        The labstep user. Must have property 'api_key'. See 'login'.
    comment_id (obj)
        The id of the comment/caption to edit.
    body (str)
        The body of the new comment.

    Returns
    -------
    comment
        An object representing the editted comment.
    """
    metadata = {'body': body}
    return editEntity(comment, metadata)


class Comment:
    __entityName__ = 'comment'

    def __init__(self, data, user):
        self.__user__ = user
        update(self, data)

    def edit(self, body):
        editComment(self, body)
