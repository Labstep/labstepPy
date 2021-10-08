#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Thomas Bullier <thomas@labstep.com>

import labstep
import os
from labstep.entities.experimentProtocol.repository import experimentProtocolRepository

class Jupyter:
    def getExperiment(self):
        """
        Get Experiment based on Jupyter environment variables.

        """
        if ('LABSTEP_API_KEY' not in os.environ.keys() or 'LABSTEP_JUPYTER_EXPERIMENT_GUID' not in os.environ.keys()):
            raise Exception("Not in jupyter")

        user = labstep.authenticate()
        experimentGuid = os.environ['LABSTEP_JUPYTER_EXPERIMENT_GUID']

        return experimentProtocolRepository.getExperimentProtocolByGuid(user, experimentGuid)


jupyter = Jupyter()
