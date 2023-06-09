#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.constants import UNSPECIFIED


class EntityWithComments(Entity):

    def addComment(self, body, filepath=UNSPECIFIED, extraParams={}):
        """
        Add a comment and/or file to a Labstep Entity.

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
            my_experiment.addComment(body='I am commenting!',
                                     filepath='pwd/file_to_upload.dat')
        """
        import labstep.entities.comment.repository as commentRepository

        return commentRepository.addCommentWithFile(
            self, body=body, filepath=filepath, extraParams=extraParams
        )

    def getComments(self, count=UNSPECIFIED):
        """
        Retrieve the Comments attached to this Labstep Entity.

        Returns
        -------
        List[:class:`~labstep.entities.comment.model.Comment`]
            List of the comments attached.

        Example
        -------
        ::

            entity = user.getExperiment(17000)
            comments = entity.getComments()
            comments[0].attributes()
        """
        import labstep.entities.comment.repository as commentRepository

        return commentRepository.getComments(self, count)
