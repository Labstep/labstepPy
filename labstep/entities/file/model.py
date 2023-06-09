#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import os
from labstep.generic.entity.model import Entity
from labstep.constants import UNSPECIFIED


class File(Entity):
    __entityName__ = "file"
    __unSearchable__ = True

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
        import labstep.entities.file.repository as fileRepository

        return fileRepository.downloadFile(self.__user__, self.id)

    def save(self, folder=UNSPECIFIED, name=UNSPECIFIED):
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

        if name is UNSPECIFIED:
            name = self.name

        if folder is not UNSPECIFIED:
            filepath = os.path.join(folder, name)
        else:
            filepath = name

        data = self.getData()
        open(filepath, "wb").write(data)

    def export(self, path):
        """
        Export the file to the directory specified. 

        Parameters
        -------
        path (str)
            The path to the directory to save the file.

        Example
        -------
        ::

            file = user.getFile(17000)
            file.export('/my_folder')
        """
        import labstep.entities.file.repository as fileRepository

        return fileRepository.exportFile(self, path)
