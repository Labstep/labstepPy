#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .entity import Entity, editEntity, newEntity, getEntities
from .file import newFile


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
    params = {'parent_thread_id': entity.thread['id'],
              'search': None,
              **extraParams}
    return getEntities(entity.__user__, Comment, count, params)


def addComment(entity, body, file_id=None, extraParams={}):
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

    params = {'body': body,
              'parent_thread_id': threadId,
              'file_id': [[file_id]] if file_id is not None else None,
              **extraParams}

    return newEntity(entity.__user__, Comment, params)


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
    if filepath is not None:
        file_id = newFile(entity.__user__, filepath).id
    else:
        file_id = None
    return addComment(entity, body, file_id=file_id, extraParams=extraParams)


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
    params = {'body': body, **extraParams}
    return editEntity(comment, params)


class Comment(Entity):
    __entityName__ = 'comment'

    def edit(self, body, extraParams={}):
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
        return editComment(self, body, extraParams=extraParams)

    def addComment(self, body, filepath=None):
        """
        Add a comment and/or file about this comment.

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
        ::

            my_experiment = user.getExperiment(17000)
            my_experiment.getComments()[0].addComment(body='I am commenting!',
                                     filepath='pwd/file_to_upload.dat')
        """
        return addCommentWithFile(self, body, filepath)

    def getComments(self, count=100):
        """
        Retrieve the Comments attached to this Comment.

        Returns
        -------
        List[:class:`~labstep.comment.Comment`]
            List of the comments attached.

        Example
        -------
        ::

            entity = user.getExperiment(17000)
            comments = entity.getComments()[0].getComments()
            comments[0]
        """
        return getComments(self, count)
