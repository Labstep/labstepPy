#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity


class ProtocolTimer(Entity):
    __entityName__ = "protocol-timer"

    def edit(self, name=None, hours=None, minutes=None, seconds=None, extraParams={}):
        """
        Edit an existing Protocol Timer.

        Parameters
        ----------
        name (str)
            The name of the timer.
        hours (int)
            The hours of the timer.
        minutes (int)
            The minutes of the timer.
        seconds (int)
            The seconds of the timer.

        Returns
        -------
        :class:`~labstep.entities.protocolTimer.model.ProtocolTimer`
            An object representing the edited Protocol Timer.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            protocol_timers = protocol.getTimers()
            protocol_timers[0].edit(name='New Timer Name',
                                    minutes=1, seconds=17)
        """
        from labstep.generic.entity.repository import entityRepository

        params = {"name": name, **extraParams}

        if hours is not None:
            params["hours"] = hours
        if minutes is not None:
            params["minutes"] = minutes
        if seconds is not None:
            params["seconds"] = seconds

        return entityRepository.editEntity(self, params)
