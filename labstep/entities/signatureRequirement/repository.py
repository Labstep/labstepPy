#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.signatureRequirement.model import SignatureRequirement
import labstep.generic.entity.repository as entityRepository
from labstep.generic.entityList.model import EntityList
from labstep.service.helpers import getTime, handleDate, update
from labstep.constants import UNSPECIFIED

def getSignatureRequirement(user, collaboratorRoleRequirement):
    if collaboratorRoleRequirement.signature_requirement is None or collaboratorRoleRequirement.signature_requirement == []:
        return None
    else:
        return collaboratorRoleRequirement.signature_requirement

def setSignatureRequirement(user,
                            collaboratorRoleRequirement,
                            statement=UNSPECIFIED,
                            days_to_sign=UNSPECIFIED,
                            reject_entity_state_id=UNSPECIFIED,
                            extraParams={}):


    params = {
        "statement": statement,
        'days_to_sign': days_to_sign,
        'reject_entity_state_id': reject_entity_state_id,
        "entity_user_role_requirement_id": collaboratorRoleRequirement.id,
        **extraParams,
    }
    signature_requirement = entityRepository.newEntity(user, SignatureRequirement, params)
    update(collaboratorRoleRequirement, { "signature_requirement": signature_requirement })
    return signature_requirement


def editSignatureRequirement(signatureRequirement,
                             statement=UNSPECIFIED,
                             days_to_sign=UNSPECIFIED,
                             reject_entity_state_id=UNSPECIFIED,
                             extraParams={}):
    params = {
        "statement": statement,
        'days_to_sign': days_to_sign,
        'reject_entity_state_id': reject_entity_state_id,
        **extraParams,
    }
    return entityRepository.editEntity(signatureRequirement, params)