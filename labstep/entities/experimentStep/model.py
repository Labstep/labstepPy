#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entityWithComments.model import EntityWithComments
from labstep.service.helpers import getTime
from labstep.constants import UNSPECIFIED


class ExperimentStep(EntityWithComments):
    __entityName__ = "experiment-step"

    def edit(self, completed_at=UNSPECIFIED):
        """
        Edit an existing Experiment Step.

        Parameters
        ----------
        completed_at (str)
            The datetime at which the Experiment Step was completed.

        Returns
        -------
        :class:`~labstep.entities.experimentStep.model.ExperimentStep`
            An object representing the edited Experiment Step.
        """
        import labstep.generic.entity.repository as entityRepository

        params = {"ended_at": completed_at}
        return entityRepository.editEntity(self, params)

    def complete(self):
        """
        Mark an existing Experiment Step as 'Complete'.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_protocol_steps = exp_protocol.getSteps()
            exp_protocol_steps[0].complete()
            exp_protocol_steps[1].complete()
            exp_protocol_steps[2].complete()
        """
        return self.edit(completed_at=getTime())

    def export(self, rootPath):
        import labstep.entities.experimentStep.repository as experimentStepRepository
        return experimentStepRepository.exportExperimentStep(self, rootPath)
