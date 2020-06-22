import requests
import json
from .helpers import listToClass, url_join, handleError, getHeaders
from .config import API_ROOT


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
    entityName = entity.__entityName__

    headers = getHeaders(entity.__user__)
    url = url_join(API_ROOT, "api/generic/", 'acl')

    params = {
        'id': entity.id,
        'entity_class': entityName.replace('-', '_'),
        'action': 'grant',
        'group_id': workspace_id,
        'permission': permission
    }
    r = requests.post(url, headers=headers, json=params)
    handleError(r)
    return entity


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
    entityName = entity.__entityName__

    headers = getHeaders(entity.__user__)
    url = url_join(API_ROOT, "api/generic/", 'acl')

    params = {
        'id': entity.id,
        'entity_class': entityName.replace('-', '_'),
        'action': 'set',
        'group_id': workspace_id,
        'group_owner_id': workspace_id,
        'permission': permission
    }
    r = requests.post(url, headers=headers, json=params)
    handleError(r)
    return entity


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
    entityName = entity.__entityName__

    headers = getHeaders(entity.__user__)
    url = url_join(API_ROOT, "api/generic/", 'acl')

    params = {
        'id': entity.id,
        'entity_class': entityName.replace('-', '_'),
        'action': 'revoke',
        'group_id': workspace_id
    }
    r = requests.post(url, headers=headers, json=params)
    handleError(r)
    return entity


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
    entityName = entity.__entityName__
    headers = getHeaders(entity.__user__)
    url = url_join(API_ROOT, "api/generic/", 'acl',
                   entityName.replace('-', '_'), str(entity.id))
    r = requests.get(url, headers=headers)
    handleError(r)
    resp = json.loads(r.content)
    return listToClass(resp['group_permissions'], Permission, entity)


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
    entityName = entity.__entityName__
    headers = getHeaders(entity.__user__)
    url = url_join(API_ROOT, "api/generic/", entityName,
                   str(entity.id), 'transfer-ownership')
    params = {'group_id': workspace_id}
    r = requests.post(url, headers=headers, json=params)
    handleError(r)
    return


class Permission:
    def __init__(self, data, entity):
        self.entity = entity
        self.workspace = data['entity']
        self.permission = data['permission']

    def set(self, permission):
        """
        Modify this sharing permission.

        Parameters
        ----------
        permission (str)
            The level of permission to grant. Can be 'view' or 'edit'

        Returns
        -------
        None
        """
        editPermission(self.entity, self.workspace['id'], permission)

    def revoke(self):
        """
        Revoke this sharing permission.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        revokePermission(self.entity, self.workspace['id'])
