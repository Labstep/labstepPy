#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.jupyterNotebook.model import JupyterNotebook
from labstep.service.request import requestService
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def newJupyterNotebook(user, name=UNSPECIFIED, data=UNSPECIFIED, extraParams={}):
    params = {"name": name, 'data': data, **extraParams}
    return entityRepository.newEntity(user, JupyterNotebook, params)


def getJupyterNotebooks(user, count=UNSPECIFIED, extraParams={}):
    params = {**extraParams}
    return entityRepository.getEntities(user, JupyterNotebook, count, params)


def getJupyterNotebook(user, guid):
    return entityRepository.getEntity(user, JupyterNotebook, id=guid)


def editJupyterNotebook(
    jupyterNotebook,
    name=UNSPECIFIED,
    status=UNSPECIFIED,
    data=UNSPECIFIED,
    extraParams={},
):
    params = {
        "name": name,
        "status": status,
        "data": data,
        **extraParams,
    }

    return entityRepository.editEntity(jupyterNotebook, params)


def runJupyterNotebook(jupyterNotebook):
    return requestService.get(
        f'https://jupyter-api.labstep.com/run/{jupyterNotebook.guid}')
