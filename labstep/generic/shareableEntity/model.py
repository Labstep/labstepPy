#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity


class ShareableEntity(Entity):
    __hasParentGroup__ = True

    def addComment(self, body, filepath=None, extraParams={}):
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
        from labstep.entities.comment.repository import commentRepository

        return commentRepository.addCommentWithFile(
            self, body=body, filepath=filepath, extraParams=extraParams
        )

    def getComments(self, count=100):
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
        from labstep.entities.comment.repository import commentRepository

        return commentRepository.getComments(self, count)

    def getPermissions(self):
        """
        Returns the sharing permissions for the Entity.

        Returns
        -------
        List[:class:`~labstep.entities.permission.model.Permission`]
        """
        from labstep.entities.permission.repository import permissionRepository

        return permissionRepository.getPermissions(self)

    def getSharelink(self):
        """
        Returns a sharelink for the Entity.

        Returns
        -------
        :class:`~labstep.entities.sharelink.model.Sharelink`
            The sharelink for the entity
        """
        from labstep.entities.sharelink.repository import shareLinkRepository

        return shareLinkRepository.getSharelink(self)

    def shareWith(self, workspace_id, permission="view"):
        """
        Shares the Entity with another Workspace.

        Parameters
        ----------
        workspace_id (int)
            The id of the workspace to share with

        permission (str)
            Permission to share with. Can be 'view' or 'edit'

        Returns
        -------
        None
        """
        from labstep.entities.permission.repository import permissionRepository

        return permissionRepository.newPermission(self, workspace_id, permission)

    def transferOwnership(self, workspace_id):
        """
        Transfer ownership of the Entity to a different Workspace

        Parameters
        ----------
        workspace_id (int)
            The id of the workspace to transfer ownership to
        """
        from labstep.entities.permission.repository import permissionRepository

        return permissionRepository.transferOwnership(self, workspace_id)
