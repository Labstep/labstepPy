#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Thomas Bullier <thomas@labstep.com>

from labstep.generic.primaryEntity.model import PrimaryEntity


class JupyterNotebook(PrimaryEntity):
    """
    Represents an JupyterNotebook on Labstep.
    """

    __entityName__ = "jupyter-notebook"
    __hasGuid__ = True

    def edit(self, name=None, status=None, data=None, extraParams={}):
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
        from labstep.entities.jupyterNotebook.repository import jupyterNotebookRepository

        return jupyterNotebookRepository.editJupyterNotebook(
            self, name=name, status=status, data=data, extraParams=extraParams
        )
