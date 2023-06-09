#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.constants import UNSPECIFIED


class ExperimentTimer(Entity):
    __entityName__ = "protocol-timer"
    __hasGuid__ = True

    def edit(self, hours=UNSPECIFIED, minutes=UNSPECIFIED, seconds=UNSPECIFIED):
        """
        Edit an existing Experiment Timer.

        Parameters
        ----------
        hours (int)
            The hours of the timer.
        minutes (int)
            The minutes of the timer.
        seconds (int)
            The seconds of the timer.

        Returns
        -------
        :class:`~labstep.entities.experimentTimer.model.ExperimentTimer`
            An object representing the edited Experiment Timer.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_protocol_timers = exp_protocol.getTimers()
            exp_protocol_timers[0].edit(minutes=1, seconds=7)
        """
        import labstep.generic.entity.repository as entityRepository

        fields = {}

        if hours is not UNSPECIFIED:
            fields["hours"] = hours
        if minutes is not UNSPECIFIED:
            fields["minutes"] = minutes
        if seconds is not UNSPECIFIED:
            fields["seconds"] = seconds

        return entityRepository.editEntity(self, fields)

    """ def start(self):
        time = getTime() + self.hours + self.minutes + self.seconds
        fields = {'ended_at': time}
        return editEntity(self, fields)

    def pause(self):
        time = getTime()
        fields = {'paused_at': time}
        return editEntity(self, fields)

    def resume(self):
        time = getTime() + self.ended_at - self.paused_at
        fields = {'ended_at': time
                  'paused_at': 'null',
                  }
        return editEntity(self, fields) """
