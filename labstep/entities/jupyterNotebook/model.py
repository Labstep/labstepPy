#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.constants import UNSPECIFIED


class JupyterNotebook(Entity):
    """
    Represents an JupyterNotebook on Labstep.
    """

    __entityName__ = "jupyter-notebook"
    __hasGuid__ = True
    __unSearchable__=True

    def edit(self, name=UNSPECIFIED, status=UNSPECIFIED, data=UNSPECIFIED, extraParams={}):
        """
        Edit an existing JupyterNotebook.

        Parameters
        ----------
        name (str)
            A display name.
        status (str)
            Server status (stopped, pending, started).
        data (str)
            JupyterNotebook ipyb JSON data.

        Returns
        -------
        :class:`~labstep.entities.jupyterNotebook.model.JupyterNotebook`
            An object representing the edited JupyterNotebook.

        Example
        -------
        ::

            my_jupyterNotebook = user.getJupyterNotebook("872b3e7e-e21f-4403-9ef3-3650fe0d86ba")
            my_jupyterNotebook.edit(data='{test: 42}')
        """
        import labstep.entities.jupyterNotebook.repository as jupyterNotebookRepository

        return jupyterNotebookRepository.editJupyterNotebook(
            self, name=name, status=status, data=data, extraParams=extraParams
        )

    def run(self):
        """
        Executes the JupyterNotebook

        """
        from labstep.entities.jupyterNotebook.repository import runJupyterNotebook

        return runJupyterNotebook(self)

    def newJupyterSchedule(self, frequency, extraParams={}):
        """
        Schedule the Jupyter Notebook to run on a regular basis.

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
            An object representing the new Labstep JupyterSchedule.

        Example
        -------
        ::

            my_jupyter_notebook = user.getJupyterNotebook(17000)
            my_jupyter_shedule = my_jupyter_notebook.newJupyterSchedule(frequency='weekly')

        """
        import labstep.entities.jupyterSchedule.repository as JupyterScheduleRepository

        return JupyterScheduleRepository.newJupyterNotebookSchedule(self.__user__, self.guid, frequency=frequency, extraParams=extraParams)

    def getJupyterSchedules(
        self, count=UNSPECIFIED,  extraParams={}
    ):
        """
        Retrieve a list of a JupyterNotebook's JupyterSchedules

        Parameters
        ----------
        count (int)
            The number of entities to return.

        Returns
        -------
        List[:class:`~labstep.entities.jupyterSchedule.model.JupyterSchedule`]
            A list of JupyterSchedules.

        Example
        -------
        ::

            my_jupyter_notebook = user.getJupyterNotebook(17000)
            my_jupyter_shedules = my_jupyter_notebook.getJupyterSchedules()
        """
        import labstep.entities.jupyterSchedule.repository as JupyterScheduleRepository

        return JupyterScheduleRepository.getJupyterSchedules(
            self.__user__,
            jupyter_notebook_guid=self.guid,
            count=count,
            extraParams=extraParams,
        )

    def getJupyterSchedule(self, jupyter_schedule_guid):
        """
        Retrieve a specific JupyterSchedule entity.

        Parameters
        ----------
        jupyter_schedule_guid (str)
            The guid of the Jupyter Schedule entity to retrieve.

        Returns
        -------
        :class:`~labstep.entities.jupyterSchedule.model.JupyterSchedule`
            An object representing a Jupyter Schedule on Labstep.

        Example
        -------
        ::

            my_jupyter_notebook = user.getJupyterNotebook(17000)
            my_jupyter_shedules = my_jupyter_notebook.getJupyterSchedule(120000)
        """
        import labstep.entities.jupyterSchedule.repository as JupyterScheduleRepository

        return JupyterScheduleRepository.getJupyterSchedule(
            self.__user__, jupyter_schedule_guid
        )
