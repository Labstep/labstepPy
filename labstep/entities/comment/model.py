#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.service.helpers import getTime


class Comment(Entity):
    __entityName__ = "comment"

    def edit(self, body, extraParams={}):
        """
        Edit an existing comment/caption.

        Parameters
        ----------
        body (str)
            The body of the new comment.

        Returns
        -------
        :class:`~labstep.entities.comment.model.Comment`
            An object representing the edited comment.

        Example
        -------
        ::

            my_comment.edit(body='My new comment.')
        """
        from labstep.entities.comment.repository import commentRepository

        return commentRepository.editComment(self, body, extraParams=extraParams)

    def delete(self):
        """
        Delete the comment.

        Example
        -------
        ::

            comment.delete()
        """
        from labstep.entities.comment.repository import commentRepository

        return commentRepository.editComment(
            self, extraParams={"deleted_at": getTime()}
        )

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
        :class:`~labstep.entities.comment.model.Comment`
            The comment added.

        Example
        -------
        ::

            my_experiment = user.getExperiment(17000)
            my_experiment.getComments()[0].addComment(body='I am commenting!',
                                     filepath='pwd/file_to_upload.dat')
        """
        from labstep.entities.comment.repository import commentRepository

        return commentRepository.addCommentWithFile(self, body, filepath)

    def getComments(self, count=100):
        """
        Retrieve the Comments attached to this Comment.

        Returns
        -------
        List[:class:`~labstep.entities.comment.model.Comment`]
            List of the comments attached.

        Example
        -------
        ::

            entity = user.getExperiment(17000)
            comments = entity.getComments()[0].getComments()
            comments[0]
        """
        from labstep.entities.comment.repository import commentRepository

        return commentRepository.getComments(self, count)

    def export(self, rootPath):
        from labstep.entities.comment.repository import commentRepository
        return commentRepository.exportComment(self, rootPath)
