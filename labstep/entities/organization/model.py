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

        return organizationRepository.editOrganization(self.__user__, name, extraParams=extraParams)

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
