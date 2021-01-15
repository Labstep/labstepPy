#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.service.helpers import getTime


class ExperimentStep(Entity):
    __entityName__ = "experiment-step"

    def edit(self, completed_at=None):
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
        from labstep.generic.entity.repository import entityRepository

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

    def addComment(self, body, filepath=None):
        """
        Add a comment and/or file to this step.

        Parameters
        ----------
        body (str)
            The body of the comment.
        filepath (str)
            A Labstep File entity to attach to the comment,
            including the filepath.

        Returns
        -------
        :class:`~labstep.entities.comment.model.Comment`
            The comment added.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_protocol_steps = exp_protocol.getSteps()
            exp_protocol_steps[0].addComment('This step failed')
        """
        from labstep.entities.comment.repository import commentRepository

        return commentRepository.addCommentWithFile(self, body, filepath)

    def getComments(self, count=100):
        """
        Retrieve the Comments attached to this step.

        Parameters
        ----------

        count (int)
            The number of comments to return

        Returns
        -------
        List[:class:`~labstep.entities.comment.model.Comment`]
            List of the comments attached.

        Example
        -------
        ::

           experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_protocol_steps = exp_protocol.getSteps()
            exp_protocol_steps[0].getComments()
        """
        from labstep.entities.comment.repository import commentRepository

        return commentRepository.getComments(self, count)
