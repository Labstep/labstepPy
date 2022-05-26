#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.generic.entity.repository import editEntity
from labstep.service.helpers import getTime


class ExperimentLink(Entity):
    __entityName__ = "experiment-workflow-link"
    __hasGuid__ = True

    def getSourceExperiment(self):
        from labstep.entities.experiment.repository import getExperiment
        return getExperiment(self.__user__, self.src['id'])

    def getTargetExperiment(self):
        from labstep.entities.experiment.repository import getExperiment
        return getExperiment(self.__user__, self.dest['id'])

    def delete(self):
        return editEntity(self, {'deleted_at': getTime()})
