#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

import os
from labstep.generic.entity.model import Entity


class File(Entity):
    __entityName__ = "file"

    def getData(self):
        """
        Retrieve the contents of a File for manipulation within Python.

        Example
        -------
        ::

            entities = user.getFiles(search_query='bacteria')
            file = entities[0]
            data = file.getData()
        """
        from labstep.entities.file.repository import fileRepository

        return fileRepository.downloadFile(self.__user__, self.id)

    def save(self, folder=None, name=None):
        """
        Save a Labstep file to the local filesystem.

        Parameters
        ----------
        folder (str)
            The path to the folder where the file should be saved
            (defaults to the current working directory).
        name (str)
            Optionally give the file a new name.

        Returns
        -------
        None

        Example
        -------
        ::

            entities = user.getFiles(search_query='bacteria')
            file = entities[0]
            file.save()
        """
        if name is None:
            name = self.name

        if folder is not None:
            filepath = os.path.join(folder, name)
        else:
            filepath = name

        data = self.getData()
        open(filepath, "wb").write(data)
