#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.service.helpers import url_join, getHeaders
from labstep.service.config import configService
from labstep.service.request import requestService
from labstep.entities.invitation.model import Invitation
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def newInvitations(user, invitationType, emails, organization_id, workspace_id=UNSPECIFIED):
    url = url_join(configService.getHost(), 'api/generic',
                   'share-link-invitation', invitationType)
    headers = getHeaders(user=user)
    json = {
        'emails': emails,
        'organization_id': organization_id,
        'organization_group_id': workspace_id
    }
    requestService.post(url=url, headers=headers, json=json)


def getInvitations(user, organization_id, extraParams):
    return entityRepository.getEntities(user, Invitation, count=UNSPECIFIED, filterParams={
        'organization_id': organization_id, **extraParams})
