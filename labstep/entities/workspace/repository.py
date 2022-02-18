#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.workspace.model import Workspace
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def getWorkspace(user, workspace_id):
    return entityRepository.getEntity(user, Workspace, id=workspace_id)


def getWorkspaces(user, count=100, search_query=UNSPECIFIED, extraParams={}):
    params = {"name": search_query, **extraParams}
    return entityRepository.getEntities(user, Workspace, count, params)


def newWorkspace(user, name, extraParams={}):
    params = {"name": name, **extraParams}
    return entityRepository.newEntity(user, Workspace, params)


def editWorkspace(workspace, name=UNSPECIFIED, deleted_at=UNSPECIFIED, extraParams={}):
    params = {"name": name, "deleted_at": deleted_at, **extraParams}
    return entityRepository.editEntity(workspace, params)
