#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .entity import Entity, editEntity, newEntity, getEntities
from .file import newFile


def getComments(entity, count=100):
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
    filterParams = {'thread_id': entity.thread['id']}
    return getEntities(entity.__user__, Comment, count, filterParams)


def addComment(entity, body, file=None):
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
    threadId = entity.thread['id']

    fields = {'body': body,
              'thread_id': threadId,
              }

    if file is not None:
        fields['file_id'] = [file.id]

    return newEntity(entity.__user__, Comment, fields)


def addCommentWithFile(entity, body, filepath):
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
    comment (obj)
        The comment/caption to edit.
    body (str)
        The body of the new comment.

    Returns
    -------
    comment
        An object representing the edited comment.
    """
    fields = {'body': body}
    return editEntity(comment, fields)


class Comment(Entity):
    __entityName__ = 'comment'

    def edit(self, body):
        """
        Edit an existing comment/caption.

        Parameters
        ----------
        body (str)
            The body of the new comment.

        Returns
        -------
        :class:`~labstep.comment.Comment`
            An object representing the edited comment.

        Example
        -------
        ::

            my_comment.edit(body='My new comment.')
        """
        return editComment(self, body)
