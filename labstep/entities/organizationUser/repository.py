#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.service.helpers import getTime
from labstep.entities.organizationUser.model import OrganizationUser
import labstep.generic.entity.repository as entityRepository
from labstep.generic.entityList.model import EntityList
from labstep.entities.user.model import User
from labstep.constants import UNSPECIFIED
from labstep.service.helpers import (
    url_join,
    getHeaders,
)
from labstep.service.config import configService
import json
from labstep.service.request import requestService



def getOrganizationUsers(organization, count=UNSPECIFIED, extraParams={}):

    params = {
        'organization_id': organization.id,
        **extraParams,
    }

    return entityRepository.getEntities(
        organization.__user__,
        OrganizationUser, count,
        filterParams=params)


def promoteUser(organizationUser):
    params = {
        "type": "admin",
    }
    return entityRepository.editEntity(organizationUser, params)


def demoteUser(organizationUser):
    params = {
        "type": "member",
    }
    return entityRepository.editEntity(organizationUser, params)


def disableUser(organizationUser):
    params = {
        "deleted_at": getTime(),
    }
    user = User({"id": organizationUser.user['username']})
    user.__user__ = organizationUser.__user__
    return entityRepository.editEntity(user, params)


def addUsers(adminUser,users,workspace_id=UNSPECIFIED):
    headers = getHeaders(user=adminUser)
    url = url_join(configService.getHost(), "/api/generic/",
                   "user", "batch")
    response = requestService.post(
        url, headers=headers, json={"items": users, "group_id": adminUser.activeWorkspace})
    responseJson = json.loads(response.content)

    #sharelink_invitations = EntityList(responseJson["sharelink_invitations"], Sharelink, adminUser)
    if responseJson["share_link_invitation"]:
        print("WARNING: Some users were not added to the organization as they already have Labstep accounts. An invitation has been sent to them instead.")

    organization_users = [user["user_organizations"][0] for user in responseJson["user"] if user["user_organizations"]]

    return EntityList(organization_users, OrganizationUser, adminUser)






