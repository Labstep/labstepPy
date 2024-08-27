#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.collaboratorRole.model import CollaboratorRole
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED

def addCollaboratorRole(user, group_id, name=UNSPECIFIED, description=UNSPECIFIED, extraParams={}):
    params = {
        "group_id": group_id,
        "name": name,
        "description": description,
        **extraParams,
    }
    return entityRepository.newEntity(user, CollaboratorRole, params)

def editCollaboratorRole(collaboratorRole, name=UNSPECIFIED,
                                           description=UNSPECIFIED,
                                           deleted_at=UNSPECIFIED,
                                           extraParams={}):
    params = {
        "name": name,
        "description": description,
        "deleted_at": deleted_at,
        **extraParams,
    }
    return entityRepository.editEntity(collaboratorRole, params)

def getCollaboratorRole(user, collaboratorRole_id):
    return entityRepository.getEntity(user, CollaboratorRole, id=collaboratorRole_id)


def getCollaboratorRoles(user, entity_state_workflow_id=UNSPECIFIED,
                         group_id=UNSPECIFIED,
                         count=UNSPECIFIED,
                         search_query=UNSPECIFIED,
                         extraParams={}):
    params = {
              #'entity_state_workflow_id':entity_state_workflow_id,
              'group_id':group_id,
              #"search_query": search_query,
              **extraParams}
    return entityRepository.getEntities(user, CollaboratorRole, count, params)