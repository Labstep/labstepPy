#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.service.config import API_ROOT
from labstep.service.helpers import getHeaders, url_join
from labstep.entities.organization.model import Organization
from labstep.generic.entity.repository import entityRepository
from labstep.service.request import requestService


class OrganizationRepository:
    def getOrganization(self, user, id, extraParams={}):
        return entityRepository.getEntity(user, Organization, id, extraParams)

    def editOrganization(self, organization, name, extraParams={}):
        params = {
            "name": name,
            **extraParams,
        }
        return entityRepository.editEntity(organization, params)

    def newOrganization(self, user, name, extraParams={}):

        params = {
            "name": name,
            **extraParams,
        }

        return entityRepository.newEntity(user, Organization, params)


organizationRepository = OrganizationRepository()
