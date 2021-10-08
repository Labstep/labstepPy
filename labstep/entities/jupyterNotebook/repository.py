#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Thomas Bullier <thomas@labstep.com>

from labstep.entities.jupyterNotebook.model import JupyterNotebook
from labstep.generic.entity.repository import entityRepository


class JupyterNotebookRepository:
    def getJupyterNotebook(self, user, guid):
        return entityRepository.getEntity(user, JupyterNotebook, id=guid)

    def editJupyterNotebook(
        self,
        jupyterNotebook,
        name=None,
        status=None,
        data=None,
        extraParams={},
    ):
        params = {
            "name": name,
            "status": status,
            "data": data,
            **extraParams,
        }

        return entityRepository.editEntity(jupyterNotebook, params)


jupyterNotebookRepository = JupyterNotebookRepository()
