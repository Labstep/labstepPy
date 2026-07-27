#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.protocolTable.model import ProtocolTable
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def getProtocolTable(user, protocol_table_id):
    return entityRepository.getEntity(user, ProtocolTable, id=protocol_table_id)


def getProtocolTables(user, protocol_id, count=UNSPECIFIED, extraParams={}):
    params = {"protocol_id": protocol_id, **extraParams}
    return entityRepository.getEntities(user, ProtocolTable, count, params)
