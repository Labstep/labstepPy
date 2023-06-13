#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entityWithComments.model import EntityWithComments
from labstep.service.helpers import getTime


class Comment(EntityWithComments):
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
        import labstep.entities.comment.repository as commentRepository

        return commentRepository.editComment(self, body, extraParams=extraParams)

    def delete(self):
        """
        Delete the comment.

        Example
        -------
        ::

            comment.delete()
        """
        import labstep.entities.comment.repository as commentRepository

        return commentRepository.editComment(
            self, extraParams={"deleted_at": getTime()}
        )

    def export(self, rootPath):
        import labstep.entities.comment.repository as commentRepository
        return commentRepository.exportComment(self, rootPath)
