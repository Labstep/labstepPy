#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Thomas Bullier <thomas@labstep.com>

import labstep
import os
import labstep.generic.entity.repository as entityRepository
from labstep.entities.experimentProtocol.model import ExperimentProtocol


def getParent():
    """
    Get Parent based on Jupyter environment variables.

    """
    if ('LABSTEP_API_KEY' not in os.environ.keys() or 'LABSTEP_JUPYTER_EXPERIMENT_GUID' not in os.environ.keys()):
        raise Exception("Not in jupyter")

    user = labstep.authenticate()
    experimentGuid = os.environ['LABSTEP_JUPYTER_EXPERIMENT_GUID']

    return entityRepository.getEntity(user, ExperimentProtocol, experimentGuid, useGuid=True)
