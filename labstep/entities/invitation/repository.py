#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.service.helpers import url_join, getHeaders
from labstep.service.config import configService
from labstep.service.request import requestService
from labstep.entities.invitation.model import Invitation
from labstep.generic.entity.repository import entityRepository


class InvitationRepository:
    def newInvitations(self, user, invitationType, emails, organization_id, workspace_id=None):
        url = url_join(configService.getHost(), 'api/generic',
                       'share-link-invitation', invitationType)
        headers = getHeaders(user=user)
        json = {
            'emails': emails,
            'organization_id': organization_id,
            'organization_group_id': workspace_id
        }
        requestService.post(url=url, headers=headers, json=json)

    def getInvitations(self, user, organization_id, extraParams):
        return entityRepository.getEntities(user, Invitation, count=None, filterParams={
            'organization_id': organization_id, **extraParams})


invitationRepository = InvitationRepository()
