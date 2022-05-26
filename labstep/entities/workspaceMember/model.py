#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

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
