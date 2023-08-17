#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Reynol Diaz <reynol.diaz@labstep.com>


def addProtocolConditions(parent, number_of_conditions):
    from labstep.generic.entity.repository import newEntities
    from labstep.entities.protocolCondition.model import ProtocolCondition
    parent.update()

    conditions = [{f'{parent.__entityName__}_guid': parent.guid}
                  ] * number_of_conditions

    return newEntities(parent.__user__, ProtocolCondition, conditions)


def getProtocolConditions(parent):
    from labstep.generic.entity.repository import getEntities
    from labstep.entities.protocolCondition.model import ProtocolCondition
    from labstep.constants import UNSPECIFIED

    parent.update()

    params = {
        f'{parent.__entityName__}_guid': parent.guid if hasattr(parent,'guid') else UNSPECIFIED,
    }
    
    return getEntities(parent.__user__, ProtocolCondition, count=UNSPECIFIED,filterParams=params)