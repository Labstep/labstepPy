#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import labstep.entities.organizationUser.repository as organizationUserRepository
from labstep.generic.entity.model import Entity
import labstep.generic.entity.repository as entityRepository
import labstep.entities.workspace.repository as workspaceRepository
import labstep.entities.invitation.repository as invitationRepository
from labstep.constants import UNSPECIFIED


class Organization(Entity):
    __entityName__ = "organization"

    def edit(self, name, extraParams={}):
        """
        Edit Organization.

        Parameters
        ----------
        name (str)
            The name of the Organization.

        Returns
        -------
        :class:`~labstep.entities.organization.model.Organization`
            An object representing the organization.

        Example
        -------
        ::

            my_organization.edit(name='My new organization.')
        """
        import labstep.entities.organization.repository as organizationRepository

        return organizationRepository.editOrganization(self, name, extraParams=extraParams)

    def addUsers(self, users, workspace_id=UNSPECIFIED):
        """
        Add users to your organization.

        Parameters
        ----------
        users (list)
            A list of users to add in form [{'first_name': 'Bob',
            'last_name': 'Ross', 'email': 'test@labstep.com'}]

        workspace_id (string)
            Optionally specify the id of a workspace to add the new users to.

        Returns
        -------
        List[:class:`~labstep.entities.organizationUser.model.OrganizationUser`]
            A list of OrganizationUser objects representing the users added to the organization.

        Example
        -------
        ::

            users = my_organization.addUsers([
                {
                    'first_name': 'Bob',
                    'username': 'Ross',
                    'email': 'bob@labstep.com'
                },
                {
                    'first_name': 'Alice',
                    'username': 'Wonderland',
                    'email': 'alice@labstep.com'
                }
            ])
        """
        return organizationUserRepository.addUsers(self.__user__, users, workspace_id=workspace_id)

    def inviteUsers(self, emails, workspace_id=UNSPECIFIED):
        """
        Invite users to your organization.

        Parameters
        ----------
        emails (list)
            A list of email address to send invitations to.

        workspace_id (int)
            Optionally specifiy the id of a workspace to add the new users to.

        Example
        -------
        ::

            my_organization.inviteUsers(emails=['user1@labstep.com','user2@labstep.com'],
                workspace_id=123)
        """
        return invitationRepository.newInvitations(self.__user__,
                                                   invitationType='organization',
                                                   emails=emails,
                                                   organization_id=self.id,
                                                   workspace_id=workspace_id)

    def getWorkspaces(self, count=UNSPECIFIED, search_query=UNSPECIFIED):
        """
        Get the workspaces in your Organization

        Parameters
        ----------
        count (int)
            Number of workspaces to return.

        search_query (string)
            Search for specific workspaces by name.

        Returns
        -------
        List[:class:`~labstep.entities.workspace.model.Workspace`]
            A list of workspaces in the organization.

        Example
        -------
        ::

            workspaces = my_organization.getWorkspaces(search_query='R&D Workspace')
        """
        return workspaceRepository.getWorkspaces(self.__user__,
                                                 count=count,
                                                 search_query=search_query,
                                                 extraParams={'organization_id': self.id})

    def getUsers(self, count=UNSPECIFIED, extraParams={}):
        """
        Get the users in your Organization.

        Returns
        -------
        List[:class:`~labstep.entities.organizationUser.model.OrganizationUser`]
            A list of users in your organization

        Example
        -------
        ::

            users = my_organization.getUsers()
            user[0].disable()
        """
        return organizationUserRepository.getOrganizationUsers(self,
                                                               count=count,
                                                               extraParams=extraParams)

    def getPendingInvitations(self, extraParams={}):
        """
        Get pending invitations to your Organization.

        Returns
        -------
        List[:class:`~labstep.entities.invitation.model.Invitation`]
            A list of invitations sent

        Example
        -------
        ::

            invitations = my_organization.getPendingInvititations()
        """
        return invitationRepository.getInvitations(self.__user__,
                                                   self.id,
                                                   extraParams={'has_invited_user': False,
                                                                **extraParams})

    def newWorkspaceRole(self,
                         name,
                         extraParams={}):
        """
        Create a new Workspace Role in your Organization.

        Parameters
        ----------
        name (str)
            Name of the new Workspace Role.

        Returns
        -------
        :class:`~labstep.entities.workspaceRole.model.WorkspaceRole`
            An object representing a Workspace Role in Labstep.

        Example
        -------
        ::

            new_workspace_role = my_organization.newWorkspaceRole(name='Inventory Manager')
        """

        import labstep.entities.workspaceRole.repository as WorkspaceRoleRepository
        self.__user__ = self.__user__.update()
        return WorkspaceRoleRepository.newWorkspaceRole(
            self.__user__, organization_id=self.guid, name=name, extraParams=extraParams
        )

    def getWorkspaceRoles(self, count=UNSPECIFIED, search_query=UNSPECIFIED, extraParams={}):
        """
        Retrieve a list of organizations's Workspace Role in Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of Workspace Roles to retrieve.
        search_query (str)
            Search for Workspace Role with this 'name'.

        Returns
        -------
        List[:class:`~labstep.entities.workspaceRoles.model.WorkspaceRoles`]
            A list of Workspace Roles objects.

        Example
        -------
        ::

            workspace_roles = my_organization.getWorkspaceRoles(search_query='Inventory')
        """
        import labstep.entities.workspaceRole.repository as WorkspaceRoleRepository
        self.__user__.update()
        return WorkspaceRoleRepository.getWorkspaceRoles(
            self.__user__, count=count, search_query=search_query, extraParams=extraParams)

    def getWorkspaceRole(self, workspace_role_guid):
        """
        Retrieve a specific Labstep Workspace Role entity.

        Parameters
        ----------
        workspace_role_guid (str)
            The guid of the Workspace Role to retrieve.

        Returns
        -------
        :class:`~labstep.entities.workspaceRole.model.WorkspaceRole`
            An object representing a Workspace Role on Labstep.

        Example
        -------
        ::

            workspace_role = my_organization.getWorkspaceRole(17000)
        """
        import labstep.entities.workspaceRole.repository as WorkspaceRoleRepository
        self.__user__ = self.__user__.update()
        return WorkspaceRoleRepository.getWorkspaceRole(
            self.__user__, workspace_role_guid
        )
