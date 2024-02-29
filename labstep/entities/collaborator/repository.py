from labstep.entities.collaborator.model import Collaborator
from labstep.generic.entity.repository import getEntities, newEntity, editEntity
from labstep.service.request import requestService
from labstep.service.helpers import url_join, getHeaders
from labstep.service.config import configService
import json


def assign(parent_entity, user_id, extraParams):
    parenty_entity_name = str(
        f'{parent_entity.__entityName__}_id').replace('-', '_')

    params = {parenty_entity_name: parent_entity.id,
              'user_id': user_id,
              'is_assigned': True,
              **extraParams}

    return newEntity(parent_entity.__user__, Collaborator, params)


def unassign(collaborator, extraParams={}):
    entity_name = collaborator['permission_entity_info']['entityName']
    params = {f'{entity_name}_id': collaborator['permission_entity_info']['id'],
              'user_id': collaborator['user']['id'],
              'is_assigned': False,
              **extraParams}

    return newEntity(collaborator.__user__, Collaborator, params)


def getCollaborators(parent_entity, count, extraParams):
    entity_name = str(parent_entity.__entityName__).replace('-', '_')
    params = {f'{entity_name}_id': parent_entity.id,
              **extraParams}

    return getEntities(parent_entity.__user__, Collaborator, count, params)
