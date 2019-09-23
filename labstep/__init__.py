#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
import json
from datetime import datetime
from time import gmtime, strftime



####################        url_join()
API_ROOT='https://api.labstep.com/'

def url_join(*args):
    '''
    Join a set of args with a slash (/) between them. Instead of
    checking for the presence of a slash, the slashes from both sides
    of each arg will be .strip() and then args .join() together.
    '''
    return "/".join(arg.strip("/") for arg in args)

####################        getTime(), keepGetting()
timezone = strftime('%z', gmtime())
timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S{}:{}'.format(timezone[:3],timezone[3:]))
# def getTime(timestamp):
#     timezone = strftime('%z', gmtime())
#     timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S{}:{}'.format(timezone[:3],timezone[3:]))
#     return timestamp

def keepGetting(headers, count, url, extraParams):
    n = min(count,1000)
    params= {'search':1,
             'cursor':-1,
             'count':n}
    r = requests.get(url, params=params, headers=headers)
    resp = json.loads(r.content)
    items = resp['items']
    expected_results = min(resp['total'],count)
    while len(items) < expected_results:
        params= {'search':1,
                 'cursor':resp['next_cursor'],
                 'count':n}
        r = requests.get(url, headers=headers)
        resp = json.loads(r.content)
        items.extend(resp['items'])
    return items

####################        login()
def login(username,password):
    '''
    Returns an authenticated Labstep User object to allow 
    you to interact with the Labstep API.
  
    Parameters
    ----------
    username (str)
        Your Labstep username.
    password (obj)
        Your Labstep password.

    Returns
    -------
    user
        An object representing a user on Labstep.
    '''
    data = {'username': username,
            'password': password}
    url = url_join(API_ROOT,"/public-api/user/login")
    r = requests.post(url, json=data, headers={}) 
    return json.loads(r.content)


####################        getSingle()
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
    params = {'is_deleted': 'both'}
    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"/api/generic/resource/",str(resource_id))
    r = requests.get(url, headers=headers, params=params)
    return json.loads(r.content)

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
    params = {'is_deleted': 'both'}
    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"/api/generic/protocol-collection/",str(protocol_id))
    r = requests.get(url, headers=headers, params=params)
    return json.loads(r.content)

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
    params = {'is_deleted': 'both'}
    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"/api/generic/group/",str(workspace_id))
    r = requests.get(url, headers=headers, params=params)
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
    params = {'is_deleted': 'both'}
    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"/api/generic/experiment-workflow/",str(experiment_id))
    r = requests.get(url, headers=headers, params=params)
    return json.loads(r.content)


####################        getMany()
"""
def getExperiments(user,count=100,created_at):
    '''
    Retrieve a list of a user's Experiments on Labstep.
  
    Parameters
    ----------
    user (obj)
        The Labstep user whose Experiments you want to retrieve.
        Must have property 'api_key'. See 'login'. 
    count (int)
        The number of Experiments to retrieve. 

    Returns
    -------
    experiment
        A list of Experiment objects.
    '''
    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"/api/generic/experiment-workflow")
    extraParams = {'created_at': created_at}
    experiments = keepGetting(headers,count,url,extraParams)
    return experiments
"""
def getResources(user,count=100):
    '''
    Retrieve a list of a user's Resources on Labstep.
  
    Parameters
    ----------
    user (obj)
        The Labstep user whose Resources you want to retrieve.
        Must have property 'api_key'. See 'login'. 
    count (int)
        The number of Resources to retrieve. 

    Returns
    -------
    resources
        A list of Resource objects.
    '''
    headers = {'apikey': user['api_key']}  
    n = min(count,1000)
    url = url_join(API_ROOT,"/api/generic/resource")
    params = {'search': 1,
              'cursor':-1,
              'count':n}
    r = requests.get(url, params=params, headers=headers)
    resp = json.loads(r.content)
    items = resp['items']

    expected_results = min(resp['total'],count)
    while len(items)<expected_results:
        cursor = resp['next_cursor']
        params = {'search':1,
                  'cursor':cursor,
                  'count':n}
        r = requests.get(url, params=params, headers=headers)
        resp = json.loads(r.content)
        items.extend(resp['items'])
    return items

def getProtocols(user,count=100):
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
    headers = {'apikey': user['api_key']}
    n = min(count,1000)
    url = url_join(API_ROOT,"/api/generic/protocol-collection")
    params = {'search':1,
              'cursor':-1,
              'count':n}
    r = requests.get(url, params=params, headers=headers)
    resp = json.loads(r.content)
    items = resp['items']

    expected_results = min(resp['total'],count)
    while len(items)<expected_results:
        params = {'search':1,
                  'cursor':resp['next_cursor'],
                  'count':n} 
        r = requests.get(url, params=params, headers=headers)
        resp = json.loads(r.content)
        items.extend(resp['items'])
    return items

def getTags(user,name=None,count=1000):
    '''
    Retrieve a list of the user's tags. 
  
    Parameters
    ----------
    user (obj)
        The Labstep user to comment as.
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
    headers = {'apikey': user['api_key']}
    n = min(count,1000)
    url = url_join(API_ROOT,"/api/generic/tag")
    params = {'search': 1,
              'cursor':-1,
              'count':n}

    if name is not None:
        params['search_query']=name

    r = requests.get(url, params=params, headers=headers)
    resp = json.loads(r.content)
    items = resp['items']
  
    expected_results = min(resp['total'],count)
    while len(items)<expected_results:
        cursor = resp['next_cursor']
        params= {'search':1,
             'cursor':cursor,
             'count':n}
        r = requests.get(url, params=params, headers=headers)
        resp = json.loads(r.content)
        items.extend(resp['items'])    
    return items


####################        newEntity()
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
    data = {'name':name}
    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"/api/generic/resource")
    r = requests.post(url, json=data, headers=headers)
    return json.loads(r.content)

def newProtocol(user,name):
    '''
    Create a new Labstep Protocol.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the protocol.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your protocol a name.

    Returns
    -------
    protocol
        An object representing the new Labstep Protocol.
    '''
    data = {'name':name}
    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"/api/generic/protocol-collection")
    r = requests.post(url, json=data, headers=headers)
    return json.loads(r.content)

def newWorkspace(user,name):
    '''
    Create a new Labstep Workspace.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the Workspace.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your workspace a name.

    Returns
    -------
    workspace
        An object representing the new Labstep Workspace.
    '''
    data = {'name':name}
    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"/api/generic/group")
    r = requests.post(url, json=data, headers=headers)
    return json.loads(r.content)

def newExperiment(user,name,description=None):
    '''
    Create a new Labstep Experiment.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the experiment.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your experiment a name.
    description : 
        Give your experiment a description.

    Returns
    -------
    experiment
        An object representing the new Labstep experiment.
    '''
    data = {'name': name,
            'description': description}
    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"/api/generic/experiment-workflow")
    r = requests.post(url, json=data, headers=headers)
    return json.loads(r.content)
    
def newTag(user,name):
    '''
    Create a new tag.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the tag. Must have property 'api_key'. See 'login'.
    name (str)
        Name of the new tag.

    Returns
    -------
    tag
        An object representing the new Labstep tag.
    '''
    data = {'name':name}
    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"/api/generic/tag")
    r = requests.post(url, json=data, headers=headers)
    return json.loads(r.content)


####################        addEntity()
def addProtocol(user,experiment,protocol):
    '''
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
    '''
    data = {'experiment_workflow_id':experiment['id'],
            'protocol_id': protocol['last_version']['id']}
    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"/api/generic/experiment")
    r = requests.post(url, json=data, headers=headers)  
    return json.loads(r.content)

def addComment(user,entity,body,file=None):
    '''
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
    '''
    headers = {'apikey': user['api_key']}
    threadId = entity['thread']['id']
  
    lsFile = [list(file.keys())[0]]      
    data = {'body': body,
            'thread_id': threadId,
            'file_id': lsFile}
  
    url = url_join(API_ROOT,"/api/generic/comment")
    r = requests.post(url, json=data, headers=headers)
    return json.loads(r.content)

def addTagTo(user,entity,tag):
    '''
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
    '''
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

    url = url_join(API_ROOT,"api/generic/",entityType,"/",str(entity['id']),"/tag/",str(tag['id']))
    headers = {'apikey': user['api_key']}
    r = requests.put(url, headers=headers)
    return json.loads(r.content)

def uploadFile(user,filepath):
    '''
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
    ''' 
    headers = {'apikey': user['api_key']}
    files = {'file': open(filepath, 'rb')}
    url = url_join(API_ROOT,"/api/generic/file/upload")
    r = requests.post(url, headers=headers, files=files)  
    return json.loads(r.content)


####################        editEntity()
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
    headers = {'apikey': user['api_key']}
    data = {'body': comment}
    url = url_join(API_ROOT,"/api/generic/comment/",str(comment_id))
    r = requests.put(url, json=data, headers=headers)
    return json.loads(r.content)

def editTag(user,tag,name):
    '''
    Edit the name of an existing tag.
  
    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property 'api_key'. See 'login'. 
    tag (obj)
        The current tag to edit.
    name (str)
        The new name of the tag.

    Returns
    -------
    tag
        An object representing the editted tag.
    '''
    data = {'name': name}
    headers = {'apikey': user['api_key']} 
    url = url_join(API_ROOT,'/api/generic/tag/',str(tag['id']))
    r = requests.put(url, json=data, headers=headers)
    return json.loads(r.content)

def editExperiment(user,experiment,deleted_at=None):
    '''
    Edit an existing Experiment.
  
    Parameters
    ----------
    user (obj)
        The labstep user. Must have property 'api_key'. See 'login'. 
    experiment (obj)
        The Experiment to edit.
    deleted_at (obj)
        The timestamp at which the Experiment is deleted/archived.

    Returns
    -------
    experiment
        An object representing the Experiment to edit.
    '''
    data = {'deleted_at': deleted_at}  
    headers = {'apikey': user['api_key']} 
    url = url_join(API_ROOT,"/api/generic/experiment-workflow/",str(experiment['id']))
    r = requests.put(url, json=data, headers=headers)
    return json.loads(r.content)

def editProtocol(user,protocol,deleted_at=None):
    '''
    Edit an existing Protocol.
  
    Parameters
    ----------
    user (obj)
        The labstep user. Must have property 'api_key'. See 'login'. 
    protocol (obj)
        The Protocol to edit.
    deleted_at (obj)
        The timestamp at which the Protocol is deleted/archived.

    Returns
    -------
    protocol
        An object representing the Protocol to edit.
    '''
    data = {'deleted_at': deleted_at}
    headers = {'apikey': user['api_key']} 
    url = url_join(API_ROOT,"/api/generic/protocol-collection/",str(protocol['id']))
    r = requests.put(url, json=data, headers=headers)
    return json.loads(r.content)

def editResource(user,resource,deleted_at=None):
    '''
    Edit an existing Resource.
  
    Parameters
    ----------
    user (obj)
        The labstep user. Must have property 'api_key'. See 'login'. 
    resource (obj)
        The Resource to edit.
    deleted_at (obj)
        The timestamp at which the Resource is deleted/archived.

    Returns
    -------
    resource
        An object representing the Resource to edit.
    '''
    data = {'deleted_at': deleted_at}
    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"/api/generic/resource/",str(resource['id']))
    r = requests.put(url, json=data, headers=headers)
    return json.loads(r.content)

def editWorkspace(user,workspace,deleted_at=None):
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
    data = {'deleted_at': deleted_at}
    headers = {'apikey': user['api_key']}
    url = url_join(API_ROOT,"/api/generic/group/",str(workspace['id']))
    r = requests.put(url, json=data, headers=headers)
    return json.loads(r.content)


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
    experiment = editExperiment(user,experiment,deleted_at=timestamp)
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
    protocol = editProtocol(user,protocol,deleted_at=timestamp)
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
    resource = editResource(user,resource,deleted_at=timestamp)
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
    workspace = editWorkspace(user,workspace,deleted_at=timestamp)
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
    Simple tagging of a Labstep entity (creates a new tag if none exists).
  
    Parameters
    ----------
    user (obj)
        The Labstep user to comment as. Must have property 'api_key'. See 'login'.
    entity (obj)
        The Labstep entity to tag. Can be Resource, Experiment, or Protocol. Must have 'id'.
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
        The Labstep user to attach as. Must have property 'api_key'. See 'login'.
    entity (obj)
        The Labstep entity to attach to. Must have 'thread' property with property 'id'.
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
