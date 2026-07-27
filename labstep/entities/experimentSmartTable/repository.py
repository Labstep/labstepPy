#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.experimentSmartTable.model import ExperimentSmartTable
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def newExperimentSmartTable(
    user,
    experiment_id=UNSPECIFIED,
    name=UNSPECIFIED,
    columns=UNSPECIFIED,
    extraParams={},
):
    params = {
        "group_id": user.activeWorkspace,
        "name": name,
        "column_definition_ids": columns,
        **extraParams,
    }
    return entityRepository.newEntity(user, ExperimentSmartTable, params)
