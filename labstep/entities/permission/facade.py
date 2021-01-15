#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.permission.repository import permissionRepository


def newPermission(entity, workspace_id, permission):
    """
    Create a new sharing permission for a Labstep Entity.

    Parameters
    ----------
    entity (obj)
        The Labstep entity to share. Can be Resource,
        Experiment, Protocol, OrderRequest or ResourceCategory.
    workspace_id (int)
        The id of the workspace to share with.
    permission (str)
        The level of permission to grant. Can be 'view' or 'edit'

    Returns
    -------
    entity
        An object representing the entity.
    """
    return permissionRepository.newPermission(entity, workspace_id, permission)


def editPermission(entity, workspace_id, permission):
    """
    Edits a sharing permission on a Labstep Entity.

    Parameters
    ----------
    entity (obj)
        The Labstep entity being shared. Can be Resource,
        Experiment, Protocol, OrderRequest or ResourceCategory.
    workspace_id (int)
        The id of the workspace shared with.
    permission (str)
        The level of permission to grant. Can be 'view' or 'edit'

    Returns
    -------
    entity
        An object representing the entity.
    """
    return permissionRepository.editPermission(entity, workspace_id, permission)


def revokePermission(entity, workspace_id):
    """
    Revoke a sharing permission for a Labstep Entity.

    Parameters
    ----------
    entity (obj)
        The Labstep entity being shared. Can be Resource,
        Experiment, Protocol, OrderRequest or ResourceCategory.
    workspace_id (int)
        The id of the workspace to unshare with.

    Returns
    -------
    entity
        An object representing the entity.
    """
    return permissionRepository.revokePermission(entity, workspace_id)


def getPermissions(entity):
    """
    Get the sharing permissions for a Labstep Entity.

    Parameters
    ----------
    entity (obj)
        The Labstep entity being shared. Can be Resource,
        Experiment, Protocol, OrderRequest or ResourceCategory.

    Returns
    -------
    List[permissions]
        An list of objects representing permissions.
    """
    return permissionRepository.getPermissions(entity)


def transferOwnership(entity, workspace_id):
    """
    Transfer Ownership for a Labstep Entity to a different Workspace.

    Parameters
    ----------
    entity (obj)
        The Labstep entity to be transfered. Can be Resource,
        Experiment, Protocol, OrderRequest or ResourceCategory.

    workspace_id (int)
        The id of the workspace to transfer ownership to

    Returns
    -------
    None
    """
    return permissionRepository.transferOwnership(entity, workspace_id)
