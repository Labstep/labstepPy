import json
from labstep.service.helpers import url_join, getHeaders
from labstep.service.config import configService
from labstep.service.request import requestService
from labstep.entities.workspaceRole.model import WorkspaceRole
from labstep.generic.entity.repository import getEntities, newEntity, editEntity, getEntity
from labstep.constants import UNSPECIFIED


def newWorkspaceRole(user, organization_id, name, extraParams):
    params = {
        "name": name,
        'organization_id': organization_id,
        **extraParams}
    return newEntity(user, WorkspaceRole, params)


def getWorkspaceRole(user,
                     permissionRole_guid,):
    return getEntity(user, WorkspaceRole, guid=permissionRole_guid)


def editWorkspaceRole(permissionRole,
                      name=UNSPECIFIED,
                      extraParams={}):

    params = {"name": name,
              **extraParams}

    return editEntity(permissionRole, params)


def getWorkspaceRoles(user,
                      count=UNSPECIFIED,
                      search_query=UNSPECIFIED,
                      extraParams={},):

    params = {
        "search_query": search_query,
        **extraParams,
    }
    return getEntities(user, WorkspaceRole, count, params)


def deletePermissionRole(WorkspaceRole):
    from labstep.generic.entity.repository import deleteEntity

    deleteEntity(WorkspaceRole)

    return None
