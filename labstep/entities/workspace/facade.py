#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.workspace.repository import workspaceRepository


def getWorkspace(user, workspace_id):
    """
    Retrieve a specific Labstep Workspace.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    workspace_id (int)
        The id of the Workspace to retrieve.

    Returns
    -------
    workspace
        An object representing a Labstep Workspace.
    """
    return workspaceRepository.getWorkspace(user, workspace_id)


def getWorkspaces(user, count=100, search_query=None, extraParams={}):
    """
    Retrieve a list of a user's Workspaces on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user whose Workspaces you want to retrieve.
        Must have property 'api_key'. See 'login'.
    count (int)
        The number of Workspaces to retrieve.
    search_query (str)
        Search for Workspaces with this 'name'.
    extraParams (dict)
        Dictionary of extra filter parameters.

    Returns
    -------
    workspaces
        A list of Workspace objects.
    """
    return workspaceRepository.getWorkspaces(user, count, search_query, extraParams)


def newWorkspace(user, name, extraParams={}):
    """
    Create a new Labstep Workspace.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the Workspace.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your Workspace a name.

    Returns
    -------
    workspace
        An object representing the new Labstep Workspace.
    """
    return workspaceRepository.newWorkspace(user, name, extraParams)


def editWorkspace(workspace, name=None, deleted_at=None, extraParams={}):
    """
    Edit an existing Workspace.

    Parameters
    ----------
    workspace (obj)
        The Workspace to edit.
    name (str)
        The new name of the Workspace.
    deleted_at (str)
        The timestamp at which the Workspace is deleted/archived.

    Returns
    -------
    workspace
        An object representing the Workspace to edit.
    """
    return workspaceRepository.editWorkspace(workspace, name, deleted_at, extraParams)
