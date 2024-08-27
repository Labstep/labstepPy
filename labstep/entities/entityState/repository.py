#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.entityState.model import EntityState
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def addEntityState(user, name,
                         color='#b5e550',
                         type='unstarted',
                         entity_state_workflow_id=UNSPECIFIED,
                         extraParams={}):
    params = {
        "name": name,
        'color': color,
        'type': type,
        'entity_state_workflow_id': entity_state_workflow_id,
        **extraParams,
    }
    return entityRepository.newEntity(user, EntityState, params)

def editEntityState(entityState, name=UNSPECIFIED,
                                 color=UNSPECIFIED,
                                 state_type=UNSPECIFIED,
                                 extraParams={}):
    params = {
        "name": name,
        'color': color,
        'type': state_type,
        **extraParams,
    }
    return entityRepository.editEntity(entityState, params)

def getEntityState(user, entity_state_id, entity_state_workflow_id=UNSPECIFIED, group_id=UNSPECIFIED):

    extraParams = {
        "get_single": 1,
        'entity_state_workflow_id': entity_state_workflow_id,
        'group_id': group_id
    }

    return entityRepository.getEntity(user,EntityState,entity_state_id,extraParams=extraParams)


def getEntityStates(user, entity_state_workflow_id=UNSPECIFIED,
                         count=UNSPECIFIED,
                         search_query=UNSPECIFIED,
                         extraParams={}):
    params = {
              'entity_state_workflow_id':entity_state_workflow_id,
              "search_query": search_query,
              **extraParams}
    return entityRepository.getEntities(user, EntityState, count, params)

