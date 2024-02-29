#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.workspaceMember.model import WorkspaceMember
import labstep.generic.entity.repository as entityRepository
from labstep.service.helpers import url_join, getHeaders
from labstep.service.config import configService
from labstep.service.request import requestService
from labstep.constants import UNSPECIFIED


def getMemberParams(org, role_name):
    lower_case_role_name = role_name.lower()
    params = {}

    permission_role = org.getWorkspaceRoles().get(
        role_name) if org is not None else None

    if lower_case_role_name == 'viewer':
        params['type'] = 'view'
    elif lower_case_role_name == 'editor':
        params['type'] = 'edit'
    elif lower_case_role_name == 'owner':
        params['type'] = 'owner'
    elif permission_role != None:
        params['permission_role_guid'] = permission_role.guid
    elif permission_role == None:
        raise ValueError(f'Role name "{role_name}" does not exist.')

    return params


def getMembers(user, workspace_id, count=UNSPECIFIED, search_query=UNSPECIFIED, extraParams={}):

    params = {"group_id": workspace_id,
              "search_query": search_query, **extraParams}

    return entityRepository.getEntities(user, WorkspaceMember, count, params)


def addMember(user, workspace_id, user_id, workspace_role_name=UNSPECIFIED):
    params = {
        "group_id": workspace_id,
        "user_id": user_id,
    }

    member = entityRepository.newEntity(user, WorkspaceMember, params)

    if workspace_role_name is not UNSPECIFIED:
        setMemberWorkspaceRole(member, workspace_role_name)

    return member


def editMemberPermission(member, permission):
    params = {
        "type": permission,
    }
    return entityRepository.editEntity(member, params)


def setMemberWorkspaceRole(member, workspace_role_name: str):
    org = member.__user__.getOrganization()

    params = getMemberParams(org, workspace_role_name)

    return entityRepository.editEntity(member, params)


def removeMember(member):
    url = url_join(configService.getHost(), 'api/generic',
                   'user-group', str(member.id))
    headers = getHeaders(member.__user__)
    return requestService.delete(url, headers)
