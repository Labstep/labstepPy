#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.service.config import configService
from labstep.service.helpers import getHeaders, url_join
from labstep.entities.organization.model import Organization
import labstep.generic.entity.repository as entityRepository
from labstep.service.request import requestService


def getOrganization(user, id, extraParams={}):
    return entityRepository.getEntity(user, Organization, id, extraParams)


def editOrganization(organization, name, extraParams={}):
    params = {
        "name": name,
        **extraParams,
    }
    return entityRepository.editEntity(organization, params)


def newOrganization(user, name, extraParams={}):

    params = {
        "name": name,
        **extraParams,
    }

    return entityRepository.newEntity(user, Organization, params)
