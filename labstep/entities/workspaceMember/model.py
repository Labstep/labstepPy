#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity


class WorkspaceMember(Entity):
    """
    Represents a member of a Labstep Workspace.

    To see all attributes of the workspace run
    ::
        print(member)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(member.name)
    """

    __entityName__ = "user-group"

    def remove(self):
        """
        Remove this member from the workspace (requires owner permission)
        """
        import labstep.entities.workspaceMember.repository as workspaceMemberRepository
        return workspaceMemberRepository.removeMember(self)

    def setWorkspaceRole(self, role_name):
        """
        Set an existing Workspace Role to a Workspace Member.

        Parameters
        ----------
        role_name(str)
            The name of the role to give the Workspace Member. It can be 'owner', 'viewer' or 'editor' or a custom role.

        Returns
        -------
        :class:`~labstep.entities.workspaceMember.model.WorkspaceMember`
            An object representing the edited Workspace Member.

        Example
        -------
        ::

            workspace_members = my_workspace.getMembers()
            workspace_members[0].setWorkspaceRole('edit')
        """
        import labstep.entities.workspaceMember.repository as workspaceMemberRepository

        return workspaceMemberRepository.setMemberWorkspaceRole(self, role_name)
