#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .entity import getEntity, getEntities, newEntity, editEntity
from .helpers import update


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
    return getEntity(user, Workspace, id=workspace_id)


def getWorkspaces(user, count=100, name=None):
    """
    Retrieve a list of a user's Workspaces on Labstep.

    Parameters
    ----------
    user (obj)
        The Labstep user whose Workspaces you want to retrieve.
        Must have property 'api_key'. See 'login'.
    count (int)
        The number of Workspaces to retrieve.

    Returns
    -------
    workspaces
        A list of Workspace objects.
    """
    metadata = {'name': name}
    return getEntities(user, Workspace, count, metadata)


def newWorkspace(user, name):
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
    metadata = {'name': name}
    return newEntity(user, Workspace, metadata)


def editWorkspace(workspace, name=None, deleted_at=None):
    """
    Edit an existing Workspace.

    Parameters
    ----------
    user (obj)
        The labstep user. Must have property 'api_key'. See 'login'.
    workspace (obj)
        The Workspace to edit.
    deleted_at (obj)
        The timestamp at which the Workspace is deleted/archived.

    Returns
    -------
    workspace
        An object representing the Workspace to edit.
    """
    data = {'name': name,
            'deleted_at': deleted_at}

    return editEntity(workspace, data)


class Workspace:
    __entityName__ = 'group'

    def __init__(self, data, user):
        self.__user__ = user
        update(self, data)
