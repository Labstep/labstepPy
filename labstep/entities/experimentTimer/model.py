#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity


class ExperimentTimer(Entity):
    __entityName__ = "experiment-timer"

    def edit(self, hours=None, minutes=None, seconds=None):
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
        from labstep.generic.entity.repository import entityRepository

        fields = {}

        if hours is not None:
            fields["hours"] = hours
        if minutes is not None:
            fields["minutes"] = minutes
        if seconds is not None:
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
