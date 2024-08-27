#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
from deprecated import deprecated
from labstep.generic.entityWithSharing.model import EntityWithSharing
from labstep.service.helpers import getTime, handleDate
from labstep.constants import UNSPECIFIED


class CollaboratorRole(EntityWithSharing):
    """
    Represents a role a user can have with respect to a particular entity on Labstep i.e. Author, Reviewer, Approver, Assignee, etc.

    """

    __entityName__ = "entity-user-role"
    __unSearchable__ = True

    def edit(self, name=UNSPECIFIED, description=UNSPECIFIED, extraParams={}):
        """
        Edit an existing CollaboratorRole.

        Parameters
        ----------
        name (str)
            The new name of the CollaboratorRole.

        description(str)
            The new description of the CollaboratorRole.

        Returns
        -------
        :class:`~labstep.entities.collaboratorRole.model.CollaboratorRole`
            An object representing the edited CollaboratorRole.

        Example
        -------
        ::

            workspace = user.getWorkspace(17000)
            my_collaborator_role = workspace.getCollaboratorRole(17000)
            my_collaborator_role.edit(name='A New CollaboratorRole Name')
        """
        import labstep.entities.collaboratorRole.repository as collaboratorRoleRepository

        return collaboratorRoleRepository.editCollaboratorRole(self, name=name, description=description, extraParams=extraParams)


