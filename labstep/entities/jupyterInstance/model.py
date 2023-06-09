#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.service.helpers import getTime


class JupyterInstance(Entity):
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
        import labstep.entities.jupyterInstance.repository as jupyterInstanceRepository

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
        import labstep.entities.jupyterInstance.repository as jupyterInstanceRepository

        return jupyterInstanceRepository.editJupyterInstance(
            self, endedAt=getTime()
        )

    def edit(self, data=None, extraParams={}):
        """
        Edit an existing JupyterInstance.

        Parameters
        ----------
        data (str)
            JupyterNotebook ipyb JSON data.

        Returns
        -------
        :class:`~labstep.entities.jupyterInstance.model.JupyterInstance`
            An object representing the edited JupyterInstance.

        Example
        -------
        ::

            my_jupyterInstance = user.getJupyterInstance("872b3e7e-e21f-4403-9ef3-3650fe0d86ba")
            my_jupyterInstance.edit(data='{test: 42}')
        """
        import labstep.entities.jupyterInstance.repository as jupyterInstanceRepository

        return jupyterInstanceRepository.editJupyterInstance(
            self, data=data
        )
