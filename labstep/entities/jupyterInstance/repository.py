#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Thomas Bullier <thomas@labstep.com>

from labstep.entities.jupyterInstance.model import JupyterInstance
from labstep.generic.entity.repository import entityRepository


class JupyterInstanceRepository:
    def getJupyterInstance(self, user, guid):
        return entityRepository.getEntity(user, JupyterInstance, id=guid)

    def editJupyterInstance(
        self,
        jupyterInstance,
        startedAt=None,
        endedAt=None
    ):
        params = {
            "started_at": startedAt,
            "ended_at": endedAt,
        }

        return entityRepository.editEntity(jupyterInstance, params)


jupyterInstanceRepository = JupyterInstanceRepository()
