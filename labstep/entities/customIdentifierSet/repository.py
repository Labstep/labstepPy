#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.customIdentifierSet.model import CustomIdentifierSet
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def newCustomIdentifierSet(user,
                           settings,
                           target_entity,
                           group_id=UNSPECIFIED,
                           extraParams={}):

    entityClasses = {
        'experiment': 'experiment_workflow',
        'protocol': 'protocol_collection',
        'resource': 'resource',
        'device': 'device'
    }


    params = {
        'parent_class': entityClasses[target_entity],
        'group_id': group_id,
        'settings': settings,
        **extraParams,
    }
    return entityRepository.newEntity(user, CustomIdentifierSet, fields = params)


