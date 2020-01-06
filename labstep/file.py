#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import os
from .config import API_ROOT
from .helpers import url_join, handleError
from .entity import Entity, getEntity, getEntities


def newFile(user, filepath):
    """
    Upload a file to the Labstep entity Data.

    Parameters
    ----------
    user (obj)
        The Labstep user uploading the file.
        Must have property 'api_key'. See 'login'.
    filepath (str)
        The filepath to the file to attach.

    Returns
    -------
    file
        An object representing the uploaded file to Labstep.
    """
    files = {'file': open(filepath, 'rb')}
    headers = {'apikey': user.api_key}
    url = url_join(API_ROOT, "/api/generic/file/upload")
    r = requests.post(url, headers=headers, files=files)
    handleError(r)
    data = json.loads(r.content)
    return File(list(data.values())[0], user)


def getFile(user, file_id):
    """
    Retrieve a specific Labstep File.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    file_id (int)
        The id of the File to retrieve.

    Returns
    -------
    file
        An object representing a Labstep File.
    """
    return getEntity(user, File, file_id, isDeleted=None)


def downloadFile(user, file_id):
    headers = {'apikey': user.api_key}
    url = url_join(API_ROOT, "/api/generic/file/download", str(file_id))
    r = requests.post(url, headers=headers)
    handleError(r)
    rawData = requests.get(json.loads(r.content)['signed_url']).content
    return rawData


def getFiles(user, count=100, search_query=None, file_type=None,
             extraParams={}):
    """
        Retrieve a list of a User's Files
        across all Workspaces on Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of files to retrieve.
        file_type (str)
            Return only files of a certain type. Options are:
            'csv', 'doc',
            'docx', 'jpg', 'pdf','png','ppt','pptx','svg','xls',
            'xlsx','xml' or 'generic' for all others.
        search_query (str)
            Search for files with this name.

        Returns
        -------
        List[:class:`~labstep.file.File`]
            A list of Labstep Files.

        Example
        -------
        ::

            entities = user.getFiles(search_query='bacteria')
        """
    filterParams = {'search_query': search_query,
                    'file_type': file_type}
    params = {**filterParams, **extraParams}
    return getEntities(user, File, count, params)


class File(Entity):
    __entityName__ = 'file'

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
        return downloadFile(self.__user__, self.id)

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
        open(filepath, 'wb').write(data)
