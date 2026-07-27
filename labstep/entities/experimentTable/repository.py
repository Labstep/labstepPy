#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.experimentTable.model import ExperimentTable
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def getExperimentTable(user, experiment_table_id):
    return entityRepository.getEntity(user, ExperimentTable, id=experiment_table_id)


def getExperimentTables(user, experiment_id, count=UNSPECIFIED, extraParams={}):
    params = {"experiment_id": experiment_id, **extraParams}
    return entityRepository.getEntities(user, ExperimentTable, count, params)
