#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.entityStateWorkflow.model import EntityStateWorkflow
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def newEntityStateWorkflow(user,
                           name,
                           target_entity='ExperimentWorkflow',
                           group_id=UNSPECIFIED,
                           extraParams={}):
    params = {
        'name': name,
        #'target_entity_class': target_entity.__entityName__,
        'target_entity_class': target_entity,
        'group_id': group_id,
        **extraParams,
    }
    return entityRepository.newEntity(user, EntityStateWorkflow, fields = params)

def editEntityStateWorkflow(entityStateWorkflow,
                            name=UNSPECIFIED,
                            extraParams={}):
    params = {
        'name': name,
        **extraParams,
    }
    return entityRepository.editEntity(entityStateWorkflow, params)

def getEntityStateWorkflow(user, entity_state_workflow_id):
    return entityRepository.getEntity(user, EntityStateWorkflow, id=entity_state_workflow_id)


def getEntityStateWorkflows(user,
                            search_query=UNSPECIFIED,
                            count=UNSPECIFIED,
                            extraParams={}):
    params = {'search_query': search_query,
              **extraParams}
    return entityRepository.getEntities(user, EntityStateWorkflow, count, params)

