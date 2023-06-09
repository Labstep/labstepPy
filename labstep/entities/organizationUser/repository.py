#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.service.helpers import getTime
from labstep.entities.organizationUser.model import OrganizationUser
import labstep.generic.entity.repository as entityRepository
from labstep.entities.user.model import User
from labstep.constants import UNSPECIFIED


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
