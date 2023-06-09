#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity


class EntityWithSharing(Entity):
    __hasParentGroup__ = True

    def getPermissions(self):
        """
        Returns the sharing permissions for the Entity.

        Returns
        -------
        List[:class:`~labstep.entities.permission.model.Permission`]
        """
        import labstep.entities.permission.repository as permissionRepository

        return permissionRepository.getPermissions(self)

    def getSharelink(self):
        """
        Returns a sharelink for the Entity.

        Returns
        -------
        :class:`~labstep.entities.sharelink.model.Sharelink`
            The sharelink for the entity
        """
        import labstep.entities.sharelink.repository as shareLinkRepository

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
        import labstep.entities.permission.repository as permissionRepository

        return permissionRepository.newPermission(self, workspace_id, permission)

    def transferOwnership(self, workspace_id):
        """
        Transfer ownership of the Entity to a different Workspace

        Parameters
        ----------
        workspace_id (int)
            The id of the workspace to transfer ownership to
        """
        import labstep.entities.permission.repository as permissionRepository

        return permissionRepository.transferOwnership(self, workspace_id)
