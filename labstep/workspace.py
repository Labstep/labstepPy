#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .entity import getEntity, getEntities, newEntity, editEntity
from .helpers import getTime, update


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
    Retrieve a list of a user's Workspaces on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user whose Workspaces you want to retrieve.
        Must have property 'api_key'. See 'login'.
    count (int)
        The number of Workspaces to retrieve.
    name (str)
        Search for Workspaces with this 'name'.

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
    data = {'name': name,
            'deleted_at': deleted_at}
    return editEntity(workspace, data)


class Workspace:
    __entityName__ = 'group'

    def __init__(self, data, user):
        self.__user__ = user
        update(self, data)

    # functions()
    def edit(self, name=None):
        """
        Edit an existing Workspace.

        Parameters
        ----------
        name (str)
            The new name of the Workspace.

        Returns
        -------
        :class:`~labstep.workspace.Workspace`
            An object representing the edited Workspace.

        Example
        -------
        .. code-block::

            my_workspace = user.getWorkspace(17000)
            my_workspace.edit(name='A New Workspace Name')
        """
        return editWorkspace(self, name)

    def delete(self):
        """
        Delete an existing Workspace.

        Example
        -------
        .. code-block::

            my_workspace = user.getWorkspace(17000)
            my_workspace.delete()
        """
        return editWorkspace(self, deleted_at=getTime())
