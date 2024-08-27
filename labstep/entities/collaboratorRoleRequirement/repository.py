#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.collaboratorRoleRequirement.model import CollaboratorRoleRequirement
import labstep.generic.entity.repository as entityRepository
from labstep.generic.entityList.model import EntityList
from labstep.constants import UNSPECIFIED

def getCollaboratorRoleRequirements(user, entityState):
    if entityState['entity_user_role_requirements'] is None or entityState['entity_user_role_requirements'] == []:
        return None
    else:
        return CollaboratorRoleRequirement(entityState['entity_user_role_requirements'], user)

def addCollaboratorRoleRequirement(user,
                                   entity_state,
                                   entity_user_role_id,
                                   number_required=1,
                         extraParams={}):
    params = {
        "entity_state_id": entity_state.id,
        'entity_user_role_id': entity_user_role_id,
        'number_required': number_required,
        **extraParams,
    }

    collab_requirements = entityRepository.newEntity(user, CollaboratorRoleRequirement, params)

    setattr(entity_state,'entity_user_role_requirements', collab_requirements.__dict__)
    setattr(collab_requirements, 'entity_state_id', entity_state.id)

    return collab_requirements

def editCollaboratorRoleRequirement(collaboratorRoleRequirement,
                                    number_required=UNSPECIFIED,
                                    collaborator_role_id=UNSPECIFIED,
                                    auto_assign=UNSPECIFIED,
                                    extraParams={}):

    params = {
        "number_required": number_required,
        'collaborator_role_id': collaborator_role_id,
        **extraParams,
    }

    if auto_assign == 'creator:':
        params['automation'] = {
        'type': 'experiment_workflow_create',
        'trigger_log_type': 'experiment_workflow_created',
        'filter': [],
        'action': 'set_entity_user_role',
        'payload': { 'entity_user_role_id': collaborator_role_id if collaborator_role_id is not UNSPECIFIED else collaboratorRoleRequirement['entity_user_role']['id']} },
    if auto_assign == 'contributor':
        params['automation'] ={
            "type":"experiment_workflow_edit",
            "trigger_log_type":"experiment_workflow_updated",
            "filter":[
                {"type":"and",
                 "path":"entityStateWorkflow",
                 "predicates":[
                     {"attribute":"id",
                      "comparison":"eq",
                      "value":collaboratorRoleRequirement['permission_entity_info']['id']}]},
                {"type":"and","path":"entityState","predicates":[
                    {"attribute":"id",
                     "comparison":"eq",
                     "value":collaboratorRoleRequirement['entity_state_id']}]}],
            "action":"set_entity_user_role",
            "payload":{
                "entity_user_role_id":collaborator_role_id if collaborator_role_id is not UNSPECIFIED else collaboratorRoleRequirement['entity_user_role']['id']
                }}





    return entityRepository.editEntity(collaboratorRoleRequirement, params)

