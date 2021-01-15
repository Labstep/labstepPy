#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>


class Permission:
    def __init__(self, data, entity):
        self.entity = entity
        self.workspace = data["entity"]
        self.permission = data["permission"]

    def set(self, permission):
        """
        Modify this sharing permission.

        Parameters
        ----------
        permission (str)
            The level of permission to grant. Can be 'view' or 'edit'

        Returns
        -------
        None
        """
        from labstep.entities.permission.repository import permissionRepository

        permissionRepository.editPermission(
            self.entity, self.workspace["id"], permission
        )

    def revoke(self):
        """
        Revoke this sharing permission.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        from labstep.entities.permission.repository import permissionRepository

        permissionRepository.revokePermission(self.entity, self.workspace["id"])
