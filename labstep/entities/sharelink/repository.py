#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.sharelink.model import Sharelink
import labstep.generic.entity.repository as entityRepository


def getSharelink(entity):
    key = entity.__entityName__.replace("-", "_") + "_id"
    return entityRepository.newEntity(entity.__user__, Sharelink, fields={key: entity.id})
