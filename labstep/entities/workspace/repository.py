#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.workspace.model import Workspace
from labstep.generic.entity.repository import entityRepository


class WorkspaceRepository:
    def getWorkspace(self, user, workspace_id):
        return entityRepository.getEntity(user, Workspace, id=workspace_id)

    def getWorkspaces(self, user, count=100, search_query=None, extraParams={}):
        params = {"name": search_query, **extraParams}
        return entityRepository.getEntities(user, Workspace, count, params)

    def newWorkspace(self, user, name, extraParams={}):
        params = {"name": name, **extraParams}
        return entityRepository.newEntity(user, Workspace, params)

    def editWorkspace(self, workspace, name=None, deleted_at=None, extraParams={}):
        params = {"name": name, "deleted_at": deleted_at, **extraParams}
        return entityRepository.editEntity(workspace, params)


workspaceRepository = WorkspaceRepository()
