#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from .config import *
from .helpers import url_join, handleError, getTime, createdAtFrom, createdAtTo


####################        getSingle()
def getEntity(user,entityName,id):
    """
    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    entityName (str)
        Options for the entity name are:
        'experiment-workflow', 'resource',
        'protocol-collection', 'tag'
    id (obj)
        The id of the entity.

    Returns
    -------
    returns?
        ?.
    """
    params = {'is_deleted': 'both'}
    # headers = {'apikey': user.api_key}
    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"/api/generic/",entityName,str(id))
    r = requests.get(url, headers=headers, params=params)
    handleError(r)
    return json.loads(r.content)

def getExperiment(user,experiment_id):
    """
    Retrieve a specific Labstep Experiment.
  
    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'. 
    experiment_id (obj)
        The id of the Experiment to retrieve. 

    Returns
    -------
    experiment
        An object representing a Labstep Experiment.
    """
    experiment = getEntity(user,'experiment-workflow',id=experiment_id)
    return experiment

def getProtocol(user,protocol_id):
    """
    Retrieve a specific Labstep Protocol.
  
    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    protocol_id (int)
        The id of the Protocol to retrieve. 

    Returns
    -------
    protocol
        An object representing a Labstep Protocol.
    """
    protocol = getEntity(user,'protocol-collection',id=protocol_id)
    return protocol

def getResource(user,resource_id):
    """
    Retrieve a specific Labstep Resource.
    
    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    resource_id (int)
        The id of the Resource to retrieve. 

    Returns
    -------
    resource
        An object representing a Labstep Resource.
    """
    resource = getEntity(user,'resource',id=resource_id)
    return resource

def getWorkspace(user,workspace_id):
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
    workspace = getEntity(user,'group',id=workspace_id)
    return workspace


####################        getMany()
def getEntities(user,entityName,count,metadata=None):
    """
    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    entityName (str)
        Options for entity name are: 'experiment-workflow',
        'resource', 'protocol-collection', 'tag', 'group'
    count
        ??
    metadata
        ??

    Returns
    -------
    returns?
        ?.
    """
    n = min(count,1000)
    search_params = {'search':1,
                     'cursor':-1,
                     'count':n}
    params = {**search_params, **metadata}      # Merging dicts in python3
    
    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"/api/generic/",entityName)
    r = requests.get(url, params=params, headers=headers)
    handleError(r)
    resp = json.loads(r.content)
    items = resp['items']
    expected_results = min(resp['total'],count)
    while len(items) < expected_results:
        params['cursor']= resp['next_cursor']
        r = requests.get(url, headers=headers, params=params)
        resp = json.loads(r.content)
        items.extend(resp['items'])
    return items

def getExperiments(user,count=100,search_query=None,created_at_from=None,created_at_to=None,tag_id=None):
    """
    Retrieve a list of a user's Experiments on Labstep.
  
    Parameters
    ----------
    user (obj)
        The Labstep user whose Experiments you want to retrieve.
        Must have property 'api_key'. See 'login'. 
    count (int)
        The number of Experiments to retrieve.
    created_at_from (str)
        The start date of the search range, must be 
        in the format of YYYY-MM-DD.
    created_at_to (str)
        The end date of the search range, must be 
        in the format of YYYY-MM-DD.

    Returns
    -------
    experiment
        A list of Experiment objects.
    """
    metadata = {'search_query': search_query,
                'created_at_from': createdAtFrom(created_at_from),
                'created_at_to': createdAtTo(created_at_to),
                'tag_id': tag_id,
                }
    experiments = getEntities(user,'experiment-workflow',count,metadata)
    return experiments

def getProtocols(user,count=100,search_query=None,created_at_from=None,created_at_to=None,tag_id=None):
    """
    Retrieve a list of a user's Protocols on Labstep.
  
    Parameters
    ----------
    user (obj)
        The Labstep user whose Protocols you want to retrieve.
        Must have property 'api_key'. See 'login'. 
    count (int)
        The number of Protocols to retrieve. 

    Returns
    -------
    protocols
        A list of Protocol objects.
    """
    metadata = {'search_query': search_query,
                'created_at_from': createdAtFrom(created_at_from),
                'created_at_to': createdAtTo(created_at_to),
                'tag_id': tag_id,
                }
    protocols = getEntities(user,'protocol-collection',count,metadata)
    return protocols

def getResources(user,count=100,search_query=None,status=None,tag_id=None):
    """
    Retrieve a list of a user's Resources on Labstep.
  
    Parameters
    ----------
    user (obj)
        The Labstep user whose Resources you want to retrieve.
        Must have property 'api_key'. See 'login'. 
    count (int)
        The number of Resources to retrieve.
    tag_id (obj/int)
        Retrieve Resources that have a specific tag.
    status (str)
        Current options to search the status of Resources are:
        'available', 'unavailable', 'requested', 'ordered'.

    Returns
    -------
    resources
        A list of Resource objects.
    """
    metadata = {'search_query': search_query,
                'tag_id': tag_id,
                'status': status.lower(),
                }
    resources = getEntities(user,'resource',count,metadata)
    return resources

def getTags(user,count=1000,search_query=None):
    """
    Retrieve a list of the user's tags. 
  
    Parameters
    ----------
    user (obj)
        The Labstep user.
        Must have property 'api_key'. See 'login'.
    name (str)
        Search for tags with a specific name.
    count (int)
        Total number of results to return. Defaults to 1000.

    Returns
    -------
    tags
        A list of tags matching the search query.
    """
    metadata = {'search_query': search_query}
    tags = getEntities(user,'tag',count,metadata)
    return tags

def getWorkspaces(user,count=100,name=None):
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
    workspaces = getEntities(user,'group',count,metadata)
    return workspaces


####################        newEntity()
def newEntity(user,entityName,data):
    """
    Parameters
    ----------
    user (str)
        The Labstep user.
    entityName (str)
        Currents options for entity name are: 'experiment-workflow',
        'resource', 'protocol-collection', 'tag', 'group'
    data
        The name of the entity.

    Returns
    -------
    returns?
        ?.
    """
    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"/api/generic/",entityName)
    r = requests.post(url, json=data, headers=headers)
    handleError(r)
    return json.loads(r.content)

def newExperiment(user,name,description=None):
    """
    Create a new Labstep Experiment.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the Experiment.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your Experiment a name.
    description : 
        Give your Experiment a description.

    Returns
    -------
    experiment
        An object representing the new Labstep Experiment.
    """
    data = {'name': name,
            'description': description}
    experiment = newEntity(user,'experimental-workflow',data)
    return experiment

def newProtocol(user,name):
    """
    Create a new Labstep Protocol.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the Protocol.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your Protocol a name.

    Returns
    -------
    protocol
        An object representing the new Labstep Protocol.
    """
    data = {'name':name}
    protocol = newEntity(user,'protocol-collection',data)
    return protocol

def newResource(user,name,status=None): #,location=None):
    """
    Create a new Labstep Resource.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the protocol.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your resource a name.
    status (str)
        Current options of the status to select are:
        'available', 'unavailable', 'requested', 'ordered'.
    location (str)
        The location of the Resource.

    Returns
    -------
    protocol
        An object representing the new Labstep Resource.
    """
    data = {'name': name,
            'status': status.lower(),
            #'resource_location': {'name': location},
            }
    resource = newEntity(user,'resource',data)
    return resource

def newTag(user,name):
    """
    Create a new Tag.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the Tag. Must have property 'api_key'. See 'login'.
    name (str)
        Name of the new Tag.

    Returns
    -------
    tag
        An object representing the new Labstep Tag.
    """
    data = {'name':name}
    tag = newEntity(user,'tag',data)
    return tag

def newWorkspace(user,name):
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
    data = {'name':name} 
    workspace = newEntity(user,'group',data)
    return workspace


####################        addEntity()
def addComment(user,entity,body,file=None):
    """
    Add a comment to a Labstep entity such as an Experiment or Resource.
  
    Parameters
    ----------
    user (obj)
        The Labstep user to comment as. Must have property 'api_key'. See 'login'.
    entity (obj)
        The Labstep entity to comment on. Must have 'thread' property with property 'id'.
    body (str)
        The body of the comment.
    file (obj)
        A Labstep File entity to attach to the comment. Must have 'id'.
    Returns
    -------
    comment
        An object representing a comment on labstep.
    """
    threadId = entity['thread']['id']
    if file != None:
        lsFile = [list(file.keys())[0]]
    else:
        lsFile = None
    data = {'body': body,
            'thread_id': threadId,
            'file_id': lsFile}
    return newEntity(user,'comment',data)

def addProtocol(user,experiment,protocol):
    """
    Add a Labstep Protocol to a Labstep Experiment.
  
    Parameters
    ----------
    experiment (obj)
        The Labstep Experiment to attach the Protocol to. Must have property 'id'.
    protocol (obj) 
        The Labstep Protocol to attach. Must have property 'id'.
    Returns
    -------
    experiment_protocol
        An object representing the Protocol attached to the Experiment.
    """
    data = {'experiment_workflow_id':experiment['id'],
            'protocol_id': protocol['last_version']['id']}  
    return newEntity(user,'experiment',data)

def addTagTo(user,entity,tag):
    """
    Attach an existing tag to a Labstep entity. (See 'tag' for simplified tagging).
    Parameters
    ----------
    user (obj)
    The Labstep user adding a tag. Must have property 'api_key'. See 'login'.
    entity (obj)
    The Labstep entity to tag. Can be Resource, Experiment, or Protocol. Must have 'id'.
    tag (str)
    The tag to attach. Must have an 'id' property.
    Returns
    -------
    entity
        Returns the tagged entity.
    """
    if 'experiments' in entity:
        entityType = 'experiment-workflow'
    elif 'parent_protocol' in entity:
        entityType = 'protocol-collection'
    elif 'resource_location' in entity:
        entityType = 'resource'
    elif 'collection' in entity:
        entityType = 'protocol-collection'
        entity = entity['collection']
    else:
        raise Exception('Entities of this type cannot be tagged')

    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"api/generic/",entityType,"/",str(entity['id']),"/tag/",str(tag['id']))
    r = requests.put(url, headers=headers)
    return json.loads(r.content)

def uploadFile(user,filepath):
    """
    Upload a file to the Labstep entity Data.
    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property 'api_key'. See 'login'.
    filepath (str)
        The filepath to the file to attach.
    Returns
    -------
    file
        An object to upload a file on Labstep.
    """ 
    files = {'file': open(filepath, 'rb')}
    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"/api/generic/file/upload")
    r = requests.post(url, headers=headers, files=files)
    handleError(r)
    return json.loads(r.content)


####################        editEntity()
def editEntity(user,entityName,id,metadata):
    """
    Parameters
    ----------
    user (obj)
        The Labstep user.
    entityName (str)
        Currents options for entity name are: 'experiment-workflow',
        'resource', 'protocol-collection', 'tag', 'group', 'comment'
    id
        The id of the entity.
    metadata (dict)
        The metadata being editted.

    Returns
    -------
    returns?
        ?.
    """
    # Filter the 'metadata' dictionary by removing {'fields': None}
    # to preserve the existing data in the 'fields', otherwise
    # the 'fields' will be overwritten to 'None'.
    new_metadata = dict(filter(lambda field: field[1] != None, metadata.items()))
    headers = {'apikey': user['api_key']} 
    url = url_join(API_ROOT,'/api/generic/',entityName,str(id))  
    r = requests.put(url, json=new_metadata, headers=headers)
    handleError(r)
    return json.loads(r.content)

def editComment(user,comment_id,comment):
    """
    Edit an existing comment/caption.
  
    Parameters
    ----------
    user (obj)
        The labstep user. Must have property 'api_key'. See 'login'.
    comment_id (obj)
        The id of the comment/caption to edit.
    comment (str)
        The body of the new comment.

    Returns
    -------
    comment
        An object representing the editted comment.
    """
    metadata = {'body': comment}
    comment = editEntity(user,'comment',comment_id,metadata)
    return comment

def editExperiment(user,experiment,name=None,description=None,deleted_at=None):
    """
    Edit an existing Experiment.
  
    Parameters
    ----------
    user (obj)
        The labstep user. Must have property 'api_key'. See 'login'. 
    experiment (obj)
        The Experiment to edit.
    name (str)
        The new name of the Experiment.
    description (str)
        The new description for the Experiment.
    deleted_at (obj)
        The timestamp at which the Experiment is deleted/archived.

    Returns
    -------
    experiment
        An object representing the Experiment to edit.
    """
    metadata = {'name': name,
                'description': description,
                'deleted_at': deleted_at}
    experiment = editEntity(user,'experiment-workflow',experiment['id'],metadata)
    return experiment

def editProtocol(user,protocol,name=None,deleted_at=None):
    """
    Edit an existing Protocol.
  
    Parameters
    ----------
    user (obj)
        The labstep user. Must have property 'api_key'. See 'login'. 
    protocol (obj)
        The Protocol to edit.
    name (str)
        The new name of the Experiment.
    deleted_at (obj)
        The timestamp at which the Protocol is deleted/archived.

    Returns
    -------
    protocol
        An object representing the Protocol to edit.
    """
    metadata = {'name': name,
                'deleted_at': deleted_at}
    protocol = editEntity(user,'protocol-collection',protocol['id'],metadata)
    return protocol

def editResource(user,resource,name=None,status=None,location=None,deleted_at=None,):
    """
    Edit an existing Resource.
  
    Parameters
    ----------
    user (obj)
        The labstep user. Must have property 'api_key'. See 'login'. 
    resource (obj)
        The Resource to edit.
    name (str)
        The new name of the Experiment.
    status (str)
        Current options to change the status to are:
        'available', 'unavailable', 'requested', 'ordered'.
    location (str)
        The location of the Resource.
    deleted_at (obj)
        The timestamp at which the Resource is deleted/archived.

    Returns
    -------
    resource
        An object representing the Resource to edit.
    """
    metadata = {'name': name,
                'status': status.lower(),
                'deleted_at': deleted_at,
                'resource_location': {'name': location},
                }
    resource = editEntity(user,'resource',resource['id'],metadata)
    return resource

def editTag(user,tag,name):
    """
    Edit the name of an existing Tag.
  
    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property 'api_key'. See 'login'. 
    tag (obj)
        The current Tag to edit.
    name (str)
        The new name of the Tag.

    Returns
    -------
    tag
        An object representing the editted Tag.
    """
    data = {'name': name}
    tag = editEntity(user,'tag',(tag['id']),metadata)
    return tag

def editWorkspace(user,workspace,name=None,deleted_at=None):
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
    metadata = {'name':name,
                'deleted_at': deleted_at}
    workspace = editEntity(user,'group',workspace['id'],metadata)
    return workspace


####################        deleteEntity()
def deleteExperiment(user,experiment):
    """
    Delete an existing Experiment.
  
    Parameters
    ----------
    user (obj)
        The labstep user. Must have property 'api_key'. See 'login'. 
    experiment (obj)
        The Experiment to delete.

    Returns
    -------
    experiment
        An object representing the Experiment to delete.
    """
    experiment = editExperiment(user,experiment,deleted_at=getTime())
    return experiment

def deleteProtocol(user,protocol):
    """
    Delete an existing Protocol.
  
    Parameters
    ----------
    user (obj)
        The labstep user. Must have property 'api_key'. See 'login'. 
    protocol (obj)
        The Protocol to delete.

    Returns
    -------
    protocol
        An object representing the Protocol to delete.
    """
    protocol = editProtocol(user,protocol,deleted_at=getTime())
    return protocol

def deleteResource(user,resource):
    """
    Delete an existing Resource.
  
    Parameters
    ----------
    user (obj)
        The labstep user. Must have property 'api_key'. See 'login'. 
    resource (obj)
        The Resource to delete.

    Returns
    -------
    resource
        An object representing the Resource to delete.
    """
    resource = editResource(user,resource,deleted_at=getTime())
    return resource

def deleteTag(user,tag):
    """
    Delete an existing tag.
  
    Parameters
    ----------
    user (obj)
        The labstep user. Must have property 'api_key'. See 'login'. 
    tag (obj)
        The tag to delete.

    Returns
    -------
    tag
        An object representing the tag to delete.
    """
    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"/api/generic/tag/",str(tag['id']))
    r = requests.delete(url, headers=headers)
    handleError(r)
    return json.loads(r.content)

def deleteWorkspace(user,workspace):
    """
    Delete an existing Workspace.
  
    Parameters
    ----------
    user (obj)
        The labstep user. Must have property 'api_key'. See 'login'. 
    workspace (obj)
        The Workspace to delete.

    Returns
    -------
    workspace
        An object representing the Workspace to delete.
    """
    workspace = editWorkspace(user,workspace,deleted_at=getTime())
    return workspace


####################        Compound functions
def tag(user,entity,name):
    """
    Simple tagging of a Labstep entity (creates a 
    new tag if none exists).
  
    Parameters
    ----------
    user (obj)
        The Labstep user to comment as. Must have 
        property 'api_key'. See 'login'.
    entity (obj)
        The Labstep entity to tag. Can be Resource, 
        Experiment, or Protocol. Must have 'id'.
    name (str)
        The name of the tag to create.

    Returns
    -------
    entity
        Returns the tagged entity.
    """
    tags = getTags(user,name)
    matchingTags = list(filter(lambda x: x['name']==name,tags))

    if len(matchingTags)== 0:
        tag = newTag(user,name)
    else: 
        tag = matchingTags[0]

    entity = addTagTo(user,entity,tag)
    return entity

def addFile(user,entity,filepath,caption):
    """
    Upload a file to a Labstep entity such as an Experiment
    or Resource, and add a caption to the uploading file.

    Parameters
    ----------
    user (obj)
        The Labstep user to attach as. Must have 
        property 'api_key'. See 'login'.
    entity (obj)
        The Labstep entity to attach to. Must have 
        'thread' property with property 'id'.
    filepath (str)
        The path to the file to attach.
    caption (str)
        A caption for the file.

    Returns
    -------
    caption
        Returns an uploaded file with a caption.
    """
    lsFile = uploadFile(user,filepath)
    caption = addComment(user,caption,lsFile)  
    return caption
