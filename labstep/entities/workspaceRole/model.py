#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.generic.entityList.model import EntityList
from labstep.constants import UNSPECIFIED


class WorkspaceRole(Entity):
    __entityName__ = "permission-role"
    __hasGuid__ = True
    __unSearchable__ = True

    def edit(self, name=UNSPECIFIED,
             extraParams={}):
        """
        Edit an existing Workspace Role.

        Parameters
        ----------
        name (str)
            The name of the Workspace Role.

        Returns
        -------
        :class:`~labstep.entities.workspaceRole.model.WorkspaceRole`
            An object representing the edited Workspace Role.

        Example
        -------
        ::

            my_org = user.getOrganization()
            workspace_role = my_org.getWorkspaceRole(10000)
            workspace_role.edit(name='A New Workspace Role Name')
        """
        import labstep.entities.workspaceRole.repository as WorkspaceRoleRepository

        return WorkspaceRoleRepository.editWorkspaceRole(
            self, name=name, extraParams=extraParams
        )

    def delete(self):
        """
            Delete an existing workspace Role.

            Parameters
            ----------
            Permission role (obj)
                The workspace role to delete.

            Returns
            -------
            None

            Example
            -------
            ::

                my_org = user.getOrganization()
                workspace_role = my_org.getWorkspaceRole(10000)
                workspace_role.delete()
        """
        import labstep.entities.workspaceRole.repository as WorkspaceRoleRepository

        return WorkspaceRoleRepository.deletePermissionRole(self)

    def setPermission(self, entityClass, action, permission_setting='all'):
        """
            Grant users with this workspace role permission to perform certain actions for certain entity classes. 

            Parameters
            ----------
            entityClass (obj)
                The class of the entity to grant permission over.

            action (str)
                The action to grant permission for

            permission_setting (boolean)
                'all' - Grants permission to perform the action all entities of the given class.
                'if_assigned' - Grants permission to perform the action only for entities of the given class which the user has created or been assigned to.
                'none' - Revokes any permission to perform the action for entities of the given class.

            Returns
            -------
            :class:`~labstep.entities.workspaceRolePermission.model.WorkspaceRolePermission`
            An object representing the permission granted to the Workspace Role.

            Example
            -------
            ::

                from labstep.entities.experiment.model import Experiment

                my_org = user.getOrganization()
                workspace_role = my_org.newWorkspaceRole('Lab Manager')
                workspace_role.setPermission(Experiment,'edit','if_assigned')

            """
        from labstep.entities.workspaceRolePermission.repository import setWorkspaceRolePermission
        return setWorkspaceRolePermission(self, entityClass, action, permission_setting)

    def getPermissions(self):
        """
            Return a list of the permissions that have been granted to this Workspace Role.

            Parameters
            -------
            None

            Returns
            -------
            List[:class:`~labstep.entities.workspaceRolePermission.model.WorkspaceRolePermission`]
            An object representing the permission granted to the Workspace Role.

            Example
            -------
            ::

                my_org = user.getOrganization()
                workspace_role = my_org.getWorkspaceRole('Lab Manager')
                permissions = workspace_role.getPermissions()

        """
        from labstep.entities.workspaceRolePermission.model import WorkspaceRolePermission
        return EntityList(self.permission_role_settings, WorkspaceRolePermission, self.__user__)
