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
        if self.link_source is not None:
            print('Warning: Files from External Cloud Providers cannot be downloaded')
            return

        if name is None:
            name = self.name

        if folder is not None:
            filepath = os.path.join(folder, name)
        else:
            filepath = name

        data = self.getData()
        open(filepath, "wb").write(data)

    def export(self, path):
        """
        Export the file to the directory specified. 

        Paramers
        -------
        path (str)
            The path to the directory to save the file.

        Example
        -------
        ::

            file = user.getFile(17000)
            file.export('/my_folder')
        """
        from labstep.entities.file.repository import fileRepository

        return fileRepository.exportFile(self, path)
