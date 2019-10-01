#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from .config import *
from .helpers import *


####################        getSingle()
def getEntity(user,entityName,id):
    '''
    Parameters
    ----------
    user (str)
        The Labstep user.
    entityName (str)
        Options for entity name are: 'experiment-workflow',
        'resource', 'protocol-collection', 'tag'
    id (obj)
        The id of the entity.

    Returns
    -------
    returns?
        ?.
    '''
    params = {'is_deleted': 'both'}
    headers = {'apikey': user.api_key}
    url = url_join(API_ROOT,"/api/generic/",entityName,str(id))
    r = requests.get(url, headers=headers, params=params)
    handleError(r)
    return json.loads(r.content)

def getExperiment(user,experiment_id):
    '''
    Retrieve a specific Labstep Experiment.
  
    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property 'api_key'. See 'login'. 
    experiment_id (int)
        The id of the Experiment to retrieve. 

    Returns
    -------
    experiment
        An object representing a Labstep Experiment.
    '''
    experiment = getEntity(user,'experiment-workflow',id=experiment_id)
    return experiment

def getProtocol(user,protocol_id):
    '''
    Retrieve a specific Labstep Protocol.
  
    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property 'api_key'. See 'login'. 
    protocol_id (int)
        The id of the Protocol to retrieve. 

    Returns
    -------
    protocol
        An object representing a Labstep Protocol.
    '''
    protocol = getEntity(user,'protocol-collection',id=protocol_id)
    return protocol

def getResource(user,resource_id):
    '''
    Retrieve a specific Labstep Resource.
    
    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property 'api_key'. See 'login'. 
    resource_id (int)
        The id of the Resource to retrieve. 

    Returns
    -------
    resource
        An object representing a Labstep Resource.
    '''
    resource = getEntity(user,'resource',id=resource_id)
    return resource

def getWorkspace(user,workspace_id):
    '''
    Retrieve a specific Labstep Workspace.
  
    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property 'api_key'. See 'login'. 
    workspace_id (int)
        The id of the Workspace to retrieve. 

    Returns
    -------
    workspace
        An object representing a Labstep Workspace.
    '''
    workspace = getEntity(user,'group',id=workspace_id)
    return workspace


####################        getMany()
def getEntities(user,entityName,count,metadata=None):
    '''
    Parameters
    ----------
    user (str)
        The Labstep user.
    entityName (str)
        Currents options for entity name are: 'experiment-workflow',
        'resource', 'protocol-collection', 'tag', 'group'
    count
        ??
    metadata
        ??

    Returns
    -------
    returns?
        ?.
    '''
    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"/api/generic/",entityName)
    n = min(count,1000)
    search_params = {'search':1,
                     'cursor':-1,
                     'count':n}
    #params = dict(search_params, **metadata)   # Merging dicts in python2
    params = {**search_params, **metadata}      # Merging dicts in python3
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

def getExperiments(user,count=100,search_query=None,
                   created_at_from=None,created_at_to=None,tag_id=None):
    '''
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
    '''
    metadata = {'search_query': search_query,
                'created_at_from': createdAtFrom(created_at_from),
                'created_at_to': createdAtTo(created_at_to),
                'tag_id': tag_id,
                }
    experiments = getEntities(user,'experiment-workflow',count,metadata)
    return experiments

def getProtocols(user,count=100,search_query=None,
                 created_at_from=None,created_at_to=None,tag_id=None):
    '''
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
    '''
    metadata = {'search_query': search_query,
                'created_at_from': createdAtFrom(created_at_from),
                'created_at_to': createdAtTo(created_at_to),
                'tag_id': tag_id,
                }
    protocols = getEntities(user,'protocol-collection',count,metadata)
    return protocols

def getResources(user,count=100,search_query=None,tag_id=None,status=None):
    '''
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
    '''
    metadata = {'search_query': search_query,
                'tag_id': tag_id,
                'status': status,
                }
    resources = getEntities(user,'resource',count,metadata)
    return resources

def getTags(user,count=1000,search_query=None):
    '''
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
    '''
    metadata = {'search_query': search_query}
    tags = getEntities(user,'tag',count,metadata)
    return tags

def getWorkspaces(user,count=100,search_query=None):
    '''
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
    '''
    metadata = {'search_query': search_query}
    workspaces = getEntities(user,'group',count,metadata)
    return workspaces


####################        newEntity()
def newEntity(user,entityName,data):
    '''
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
    '''
    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"/api/generic/",entityName)
    r = requests.post(url, json=data, headers=headers)
    handleError(r)
    return json.loads(r.content)

def newExperiment(user,name,description=None):
    '''
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
    '''
    data = {'name': name,
            'description': description}
    experiment = newEntity(user,'experimental-workflow',data)
    return experiment

def newProtocol(user,name):
    '''
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
    '''
    data = {'name':name}
    protocol = newEntity(user,'protocol-collection',data)
    return protocol

def newResource(user,name):
    '''
    Create a new Labstep Resource.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the protocol.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your resource a name.

    Returns
    -------
    protocol
        An object representing the new Labstep Resource.
    '''
    data = {'name': name}
    resource = newEntity(user,'resource',data)
    return resource

def newTag(user,name):
    '''
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
    '''
    data = {'name':name}
    tag = newEntity(user,'tag',data)
    return tag

def newWorkspace(user,name):
    '''
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
    '''
    data = {'name':name} 
    workspace = newEntity(user,'group',data)
    return workspace


####################        editEntity()
def editEntity(user,entityName,id,metadata):
    '''
    Parameters
    ----------
    user (str)
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
    '''
    headers = {'apikey': user['api_key']} 
    url = url_join(API_ROOT,'/api/generic/',entityName,str(id))  
    # Filter the 'metadata' dictionary by removing {'field':None} 
    new_metadata = dict(filter(lambda field: field[1] != None, metadata.items()))
    r = requests.put(url, json=new_metadata, headers=headers)
    #handleError(r)
    return json.loads(r.content)

def editComment(user,comment_id,comment):
    '''
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
    '''
    metadata = {'body': comment}
    comment = editEntity(user,'comment',comment_id,metadata)
    return comment

def editExperiment(user,experiment,name=None,description=None,deleted_at=None):
    '''
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
    '''
    metadata = {'name': name,
                'description': description,
                'deleted_at': deleted_at}
    experiment = editEntity(user,'experiment-workflow',experiment['id'],metadata)
    return experiment

def editProtocol(user,protocol,name=None,deleted_at=None):
    '''
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
    '''
    metadata = {'name': name,
                'deleted_at': deleted_at}
    protocol = editEntity(user,'protocol-collection',protocol['id'],metadata)
    return protocol

def editResource(user,resource,name=None,status=None,deleted_at=None,location=None):
    '''
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
    '''
    metadata = {'name': name,
                'status': status,
                'deleted_at': deleted_at,
                'resource_location': {'name': location},
                }
    resource = editEntity(user,'resource',resource['id'],metadata)
    return resource

def editTag(user,tag,name):
    '''
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
    '''
    data = {'name': name}
    tag = editEntity(user,'tag',(tag['id']),metadata)
    return tag

def editWorkspace(user,workspace,name=None,deleted_at=None):
    '''
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
    '''
    metadata = {'name':name,
                'deleted_at': deleted_at}
    workspace = editEntity(user,'group',workspace['id'],metadata)
    return workspace


####################        deleteEntity()
def deleteExperiment(user,experiment):
    '''
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
    '''
    experiment = editExperiment(user,experiment,deleted_at=getTime())
    return experiment

def deleteProtocol(user,protocol):
    '''
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
    '''
    protocol = editProtocol(user,protocol,deleted_at=getTime())
    return protocol

def deleteResource(user,resource):
    '''
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
    '''
    resource = editResource(user,resource,deleted_at=getTime())
    return resource

def deleteWorkspace(user,workspace):
    '''
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
    '''
    workspace = editWorkspace(user,workspace,deleted_at=getTime())
    return workspace

def deleteTag(user,tag):
    '''
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
    '''
    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"/api/generic/tag/",str(tag['id']))
    r = requests.delete(url, headers=headers)
    return json.loads(r.content)


####################        Compound functions
def tag(user,entity,name):
    '''
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
    '''
    tags = getTags(user,name)
    matchingTags = list(filter(lambda x: x['name']==name,tags))

    if len(matchingTags)== 0:
        tag = newTag(user,name)
    else: 
        tag = matchingTags[0]

    entity = addTagTo(user,entity,tag)
    return entity

def addFile(user,entity,filepath,caption):
    '''
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
    '''
    lsFile = uploadFile(user,filepath)
    caption = addComment(user,caption,lsFile)  
    return caption
