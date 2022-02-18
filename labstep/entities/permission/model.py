#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity


class Permission(Entity):
    __entityName__ = 'permission'
    __hasGuid__ = True
    __unSearchable__ = True

    def __init__(self, data, user):
        super().__init__(data, user)
        self.workspace = data["group"]
        delattr(self, 'group')

    def set(self, type):
        """
        Modify this sharing permission.

        Parameters
        ----------
        type (str)
            The level of permission to grant. Can be 'view' or 'edit'

        Returns
        -------
        None
        """
        import labstep.entities.permission.repository as permissionRepository

        permissionRepository.editPermission(
            self, type
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
        import labstep.entities.permission.repository as permissionRepository

        permissionRepository.revokePermission(self)
