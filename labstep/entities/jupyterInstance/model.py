#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Thomas Bullier <thomas@labstep.com>

from labstep.generic.primaryEntity.model import PrimaryEntity
from labstep.service.helpers import getTime


class JupyterInstance(PrimaryEntity):
    """
    Represents an JupyterInstance on Labstep.
    """

    __entityName__ = "jupyter-instance"
    __hasGuid__ = True

    def start(self):
        """
        Update JupyterInstance to indicate that server instance has started and is ready to use.

        Parameters
        ----------

        Returns
        -------
        :class:`~labstep.entities.jupyterInstance.model.JupyterInstance`
            An object representing the edited JupyterInstance.

        Example
        -------
        ::

            my_jupyterInstance = user.getJupyterInstance("872b3e7e-e21f-4403-9ef3-3650fe0d86ba")
            my_jupyterInstance.start()
        """
        from labstep.entities.jupyterInstance.repository import jupyterInstanceRepository

        return jupyterInstanceRepository.editJupyterInstance(
            self, startedAt=getTime()
        )

    def end(self):
        """
        Update JupyterInstance to indicate that server instance has shutdown.

        Parameters
        ----------

        Returns
        -------
        :class:`~labstep.entities.jupyterInstance.model.JupyterInstance`
            An object representing the edited JupyterInstance.

        Example
        -------
        ::

            my_jupyterInstance = user.getJupyterInstance("872b3e7e-e21f-4403-9ef3-3650fe0d86ba")
            my_jupyterInstance.end()
        """
        from labstep.entities.jupyterInstance.repository import jupyterInstanceRepository

        return jupyterInstanceRepository.editJupyterInstance(
            self, endedAt=getTime()
        )
