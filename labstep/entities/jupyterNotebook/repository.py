#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Thomas Bullier <thomas@labstep.com>

from labstep.entities.jupyterNotebook.model import JupyterNotebook
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def newJupyterNotebook(user, name=UNSPECIFIED, data=UNSPECIFIED):
    return entityRepository.newEntity(user, JupyterNotebook, {"name": name, "data": data})


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
