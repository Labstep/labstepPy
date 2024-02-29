#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.service.helpers import getTime
from labstep.constants import UNSPECIFIED


class JupyterSchedule(Entity):
    """
    Represents a JupyterNotebook Schedule on Labstep.
    """

    __entityName__='jupyter-cron'
    __hasGuid__ = True
    __unSearchable__=True

    def delete(self):
        """
        Delete an Jupyter Notebook Schedule entity.

        Example
        -------
        ::

            my_jupyter_notebook = user.getJupyterNotebook(17000)
            my_jupyter_shedule = my_jupyter_notebook.getJupyterSchedule(10000)
            my_jupyter_shedule.delete()
        """
        import labstep.entities.jupyterSchedule.repository as JupyterScheduleRepository

        return JupyterScheduleRepository.editJupyterSchedule(self, deleted_at=getTime())
    
    def edit(self, frequency=UNSPECIFIED, extraParams={}):
        """
        Edit an existing Jupyter Notebook Schedule entity.

        Parameters
        ----------
        frequency (str)
            Frequency values can be 'hourly' | 'daily' | 'weekly'.
            
            If frequency is set to hourly, the Jupyter Notebook script will run every hour starting at the time
            Jupyter Notebook Schedule was created.

            If frequency is set to daily, the Jupyter Notebook script will run everyday at midnight.

            If frequency is set to weekly, the Jupyter Notebook script will run every monday at midnight.

        Returns
        -------
        :class:`~labstep.entities.jupyterSchedule.model.JupyterSchedule`
            An object representing the edited Jupyter Notebook Schedule.

        Example
        -------
        ::

            my_jupyter_notebook = user.getJupyterNotebook(17000)
            my_jupyter_shedule = my_jupyter_notebook.getJupyterSchedule(10000)
            my_jupyter_shedule.edit(frequency='hourly')
        """
        import labstep.entities.jupyterSchedule.repository as JupyterScheduleRepository
        
        return JupyterScheduleRepository.editJupyterSchedule(
            self, frequency=frequency, extraParams=extraParams
        )