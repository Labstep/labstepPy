#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import labstep
import os
import labstep.generic.entity.repository as entityRepository
from labstep.entities.experimentProtocol.model import ExperimentProtocol
from labstep.entities.protocolVersion.model import ProtocolVersion


def getParent():
    """
    Get Parent based on Jupyter environment variables.

    """
    if ('LABSTEP_API_KEY' not in os.environ.keys()):
        raise Exception("Not in jupyter")

    user = labstep.authenticate()

    if ('LABSTEP_JUPYTER_EXPERIMENT_GUID' in os.environ.keys()):
        experimentGuid = os.environ['LABSTEP_JUPYTER_EXPERIMENT_GUID']
        if experimentGuid:
            return entityRepository.getEntity(user, ExperimentProtocol, experimentGuid, useGuid=True)

    if ('LABSTEP_JUPYTER_PROTOCOL_GUID' in os.environ.keys()):
        protocolGuid = os.environ['LABSTEP_JUPYTER_PROTOCOL_GUID']

        if protocolGuid:
            return entityRepository.getEntity(user, ProtocolVersion, protocolGuid, useGuid=True)

    raise Exception("No Jupyter Parent Found")
