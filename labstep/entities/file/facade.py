#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.file.repository import fileRepository


def newFile(user, filepath, extraParams={}):
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
    return fileRepository.newFile(user, filepath, extraParams)


def getFile(user, fileId):
    """
    Retrieve a specific Labstep File.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    fileId (int)
        The id of the File to retrieve.

    Returns
    -------
    file
        An object representing a Labstep File.
    """
    return fileRepository.getFile(user, fileId)


def downloadFile(user, fileId):
    return fileRepository.downloadFile(user, fileId)


def getFiles(user, count=100, search_query=None, file_type=None, extraParams={}):
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
    return fileRepository.getFiles(user, count, search_query, file_type, extraParams)
