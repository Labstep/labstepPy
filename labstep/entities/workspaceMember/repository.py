#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.workspaceMember.model import WorkspaceMember
from labstep.generic.entity.repository import entityRepository
from labstep.service.helpers import url_join, getHeaders
from labstep.service.config import configService
from labstep.service.request import requestService


class WorkspaceMemberRepository:
    def getMembers(self, user, workspace_id, count=100, search_query=None, extraParams={}):

        params = {"group_id": workspace_id,
                  "search_query_user": search_query, **extraParams}

        return entityRepository.getEntities(user, WorkspaceMember, count, params)

    def addMember(self, user, workspace_id, user_id):
        params = {
            "group_id": workspace_id,
            "user_id": user_id,
        }
        return entityRepository.newEntity(user, WorkspaceMember, params)

    def editMemberPermission(self, member, permission):
        params = {
            "type": permission,
        }
        return entityRepository.editEntity(member, params)

    def removeMember(self, member):
        url = url_join(configService.getHost(), 'api/generic',
                       'user-group', str(member.id))
        headers = getHeaders(member.__user__)
        return requestService.delete(url, headers)


workspaceMemberRepository = WorkspaceMemberRepository()
