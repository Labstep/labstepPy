from .helpers import getTime, url_join, handleError
from .config import API_ROOT


def newPermssion(entity, workspace_id, permission):
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

    headers = {'apikey': entity.__user__.api_key}
    url = url_join(API_ROOT, "api/generic/", 'acl')

    fields = {
        'id': entity.id,
        'entity_class': entityName.replace('-', '_'),
        'action': 'grant',
        'group_id': workspace_id,
        'permission': permission
    }
    r = requests.post(url, headers=headers, json=fields)
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

    headers = {'apikey': entity.__user__.api_key}
    url = url_join(API_ROOT, "api/generic/", 'acl')

    fields = {
        'id': entity.id,
        'entity_class': entityName.replace('-', '_'),
        'action': 'set',
        'group_id': workspace_id,
        'permission': permission
    }
    r = requests.post(url, headers=headers, json=fields)
    handleError(r)
    return entity


def revokePermission(entity):
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

    headers = {'apikey': entity.__user__.api_key}
    url = url_join(API_ROOT, "api/generic/", 'acl')

    fields = {
        'id': entity.id,
        'entity_class': entityName.replace('-', '_'),
        'action': 'revoke',
        'group_id': workspace_id,
        'permission': permission
    }
    r = requests.post(url, headers=headers, json=fields)
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
    headers = {'apikey': entity.__user__.api_key}
    url = url_join(API_ROOT, "api/generic/", 'acl',
                   entityName.replace('-', '_'), entity.id)
    r = requests.get(url, headers=headers)
    handleError(r)
    resp = json.loads(r.content)
    return 


def transferOwnership(entity, workspace_id):
