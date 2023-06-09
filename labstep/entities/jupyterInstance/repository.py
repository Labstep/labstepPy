#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.jupyterInstance.model import JupyterInstance
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def getJupyterInstance(user, guid):
    return entityRepository.getEntity(user, JupyterInstance, id=guid)


def editJupyterInstance(
    jupyterInstance,
    data=UNSPECIFIED,
    startedAt=UNSPECIFIED,
    endedAt=UNSPECIFIED
):
    params = {
        "data": data,
        "started_at": startedAt,
        "ended_at": endedAt,
    }

    return entityRepository.editEntity(jupyterInstance, params)
