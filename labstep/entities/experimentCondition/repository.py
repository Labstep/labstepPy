#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Reynol Diaz <reynol.diaz@labstep.com>


def addExperimentConditions(entity, number_of_conditions):
    from labstep.generic.entity.repository import newEntities
    from labstep.entities.experimentCondition.model import ExperimentCondition

    conditions = [{f'{entity.__entityName__}_guid': entity.guid}
                  ] * number_of_conditions

    return newEntities(entity.__user__, ExperimentCondition, conditions)


def getExperimentConditions(entity):
    from labstep.generic.entity.repository import getEntities
    from labstep.entities.experimentCondition.model import ExperimentCondition
    from labstep.constants import UNSPECIFIED


    params = {
        f'{entity.__entityName__}_guid': entity.guid if hasattr(entity,'guid') else UNSPECIFIED,
    }
    
    return getEntities(entity.__user__, ExperimentCondition, count=UNSPECIFIED,filterParams=params)