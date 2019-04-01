import requests
import json

def login(username,password):
  '''
  Returns an authenticated labstep User object to allow you to interact with the labstep API.
  
  Parameters
  ----------
  username : str
    You labstep username
  password : obj
    Your labstep password

  Returns
  -------
  user
    An object representing a user on labstep.
  '''
  data = {
      'username': username,
      'password': password,
  }
  url = 'https://api.labstep.com/public-api/user/login'
  r = requests.post(
      url,
      json=data,
      headers={},
  )
  return json.loads(r.content)

def getResources(user,count=100):
  '''
  Retrieve a list of a users Resources on Labstep.
  
  Parameters
  ----------
  user : obj
    The Labstep user whose Resources you want to retrieve. Must have property 'api_key'. See 'login'. 
  count : int
    The number of Resources to retrieve. 

  Returns
  -------
  resources
    A list of resource objects.
  '''
  headers = {
    'apikey': user['api_key']
  }
  n = min(count,1000)
  playlist_id = user['resource_lists'][0]['id']
  url = f"https://api.labstep.com/api/generic/resource?search=1&cursor=-1&count={n}&resource_list_id={playlist_id}"
  r = requests.get(
      url,
      headers=headers,
  )

  resp = json.loads(r.content)
  items = resp['items']

  expected_results = min(resp['total'],count)

  while len(items)<expected_results:
    cursor = resp['next_cursor']
    url = f"https://api.labstep.com/api/generic/resource?search=1&cursor={cursor}&count={n}&resource_list_id={playlist_id}"
    r = requests.get(
        url,
        headers=headers,
    )

    resp = json.loads(r.content)
    items.extend(resp['items'])

  return items


def getResource(user,id):
  '''
  Retrieve a specific Labstep Resource.
  
  Parameters
  ----------
  user : obj
    The Labstep user. Must have property 'api_key'. See 'login'. 
  id : int
    The id of the Resource to retrieve. 

  Returns
  -------
  resource
    An object representing a Labstep Resource.
  '''
  headers = {
    'apikey': user['api_key']
  }
  url = f"https://api.labstep.com/api/generic/resource/{id}"
  r = requests.get(
      url,
      headers=headers,
  )
  return json.loads(r.content)


def getProtocols(user,count=100):
  '''
  Retrieve a list of a users Protocols on Labstep.
  
  Parameters
  ----------
  user : obj
    The Labstep user whose Protocols you want to retrieve. Must have property 'api_key'. See 'login'. 
  count : int
    The number of Protocols to retrieve. 

  Returns
  -------
  protocols
    A list of Protocol objects.
  '''
  headers = {
    'apikey': user['api_key']
  }
  n = min(count,1000)
  playlist_id = user['protocol_collection_playlists'][0]['id']
  url = f"https://api.labstep.com/api/generic/protocol-collection?search=1&cursor=-1&count={n}&protocol_collection_playlist_id={playlist_id}"
  r = requests.get(
      url,
      headers=headers,
  )

  resp = json.loads(r.content)
  items = resp['items']

  expected_results = min(resp['total'],count)

  while len(items)<expected_results:
    cursor = resp['next_cursor']
    url = f"https://api.labstep.com/api/generic/protocol-collection?search=1&cursor={cursor}&count={n}&protocol_collection_playlist_id={playlist_id}"
    r = requests.get(
        url,
        headers=headers,
    )

    resp = json.loads(r.content)
    items.extend(resp['items'])

  return items


def getProtocol(user,id):
  '''
  Retrieve a specific Labstep Protocol.
  
  Parameters
  ----------
  user : obj
    The Labstep user. Must have property 'api_key'. See 'login'. 
  id : int
    The id of the Protocol to retrieve. 

  Returns
  -------
  protocol
    An object representing a Labstep Protocol.
  '''
  headers = {
    'apikey': user['api_key']
  }
  url = f"https://api.labstep.com/api/generic/protocol/{id}"
  r = requests.get(
      url,
      headers=headers,
  )
  return json.loads(r.content)


def getProject(user,id):
  '''
  Retrieve a specific Labstep Project.
  
  Parameters
  ----------
  user : obj
    The Labstep user. Must have property 'api_key'. See 'login'. 
  id : int
    The id of the Project to retrieve. 

  Returns
  -------
  project
    An object representing a Labstep Project.
  '''
  headers = {
    'apikey': user['api_key']
  }
  url = f"https://api.labstep.com/api/generic/group/{id}"
  r = requests.get(
      url,
      headers=headers,
  )
  return json.loads(r.content)


def getExperiments(user,count=100):
  '''
  Retrieve a list of a users Experiments on Labstep.
  
  Parameters
  ----------
  user : obj
    The Labstep user whose Experiments you want to retrieve. Must have property 'api_key'. See 'login'. 
  count : int
    The number of Experiments to retrieve. 

  Returns
  -------
  experiment
    A list of experiment objects.
  '''
  headers = {
    'apikey': user['api_key']
  }
  n = min(count,1000)
  url = f"https://api.labstep.com/api/generic/experiment-workflow?search=1&cursor=-1&count={n}"
  r = requests.get(
      url,
      headers=headers,
  )

  resp = json.loads(r.content)
  items = resp['items']

  expected_results = min(resp['total'],count)

  while len(items)<expected_results:
    cursor = resp['next_cursor']
    url = f"https://api.labstep.com/api/generic/experiment-workflow?search=1&cursor={cursor}&count={n}"
    r = requests.get(
        url,
        headers=headers,
    )

    resp = json.loads(r.content)
    items.extend(resp['items'])

  return items


def getExperiment(user,id):
  '''
  Retrieve a specific Labstep Experiment.
  
  Parameters
  ----------
  user : obj
    The Labstep user. Must have property 'api_key'. See 'login'. 
  id : int
    The id of the Experiment to retrieve. 

  Returns
  -------
  experiment
    An object representing a Labstep Experiment.
  '''
  headers = {
    'apikey': user['api_key']
  }
  url = f"https://api.labstep.com/api/generic/experiment-workflow/{id}"
  r = requests.get(
      url,
      headers=headers,
  )
  return json.loads(r.content)



def createResource(user,name):
  '''Create a new Labstep Resource

  Parameters
  ----------
  user : obj
    The Labstep user creating the protocol. Must have property 'api_key'. See 'login'.
  name : str
    Give your resource a name.

  Returns
  -------
  protocol
    An object representing the new Labstep Resource.
  '''
  data = {
    'name':name,
  }
  headers = {
    'apikey': user['api_key']
  }
  url = 'https://api.labstep.com/api/generic/resource'
  r = requests.post(
      url,
      json=data,
      headers=headers,
  )
  return json.loads(r.content)

def createProtocol(user,name):
  '''Create a new Labstep Protocol

  Parameters
  ----------
  user : obj
    The Labstep user creating the protocol. Must have property 'api_key'. See 'login'.
  name : str
    Give your protocol a name.

  Returns
  -------
  protocol
    An object representing the new Labstep Protocol.
  '''
  data = {
    'name':name,
  }
  headers = {
    'apikey': user['api_key']
  }
  url = 'https://api.labstep.com/api/generic/protocol'
  r = requests.post(
      url,
      json=data,
      headers=headers,
  )
  return json.loads(r.content)

def createProject(user,name):
  '''Create a new Labstep Project

  Parameters
  ----------
  user : obj
    The Labstep user creating the project. Must have property 'api_key'. See 'login'.
  name : str
    Give your project a name.

  Returns
  -------
  project
    An object representing the new Labstep project.
  '''
  data = {
    'name':name,
  }
  headers = {
    'apikey': user['api_key']
  }
  url = 'https://api.labstep.com/api/generic/group'
  r = requests.post(
      url,
      json=data,
      headers=headers,
  )
  return json.loads(r.content)

def createExperiment(user,name,description):
  '''Create a new Labstep Experiment

  Parameters
  ----------
  user : obj
    The Labstep user creating the experiment. Must have property 'api_key'. See 'login'.
  name : str
    Give your experiment a name.
  description : 
    Give your experiment a description.

  Returns
  -------
  experiment
    An object representing the new labstep experiment.
  '''
  data = {
    'name':name,
    'description': description,
  }
  headers = {
    'apikey': user['api_key']
  }
  url = 'https://api.labstep.com/api/generic/experiment-workflow'
  r = requests.post(
      url,
      json=data,
      headers=headers,
  )
  return json.loads(r.content)

def attachProtocol(user,experiment,protocol):
  '''Attach a Labstep Protocol to a Labstep Experiment
  
  Parameters
  ----------
  experiment : obj
    The labstep experiment to attach the protocol to. Must have property 'id'.
  protocol : 
    The labstep protocol to attach. Must have property 'id'.

  Returns
  -------
  experiment
    An object representing the updated labstep experiment.
  '''
  data = {
    'experiment_workflow_id':experiment['id'],
    'protocol_id': protocol['id'],
  }
  headers = {
    'apikey': user['api_key']
  }
  url = 'https://api.labstep.com/api/generic/experiment'
  r = requests.post(
      url,
      json=data,
      headers=headers,
  )
  url = f"https://api.labstep.com/api/generic/experiment-workflow/{experiment['id']}"
  r = requests.get(
      url,
      headers=headers,
  )
  return json.loads(r.content)


def attachFile(user,entity,filepath,caption):
  '''Attach a file to a labstep entity such as an experiment or resource. Optionally include a cpation describing the file.

  Parameters
  ----------
  user : obj
    The labstep user to attach as. Must have property 'api_key'. See 'login'.
  entity : obj
    The labstep entity to attach to. Must have 'thread' property with property 'id'.
  filepath : str
    The filepath to the file to attach
  caption : str
    An optional caption for the file.

  Returns
  -------
  comment
    An object representing a comment on labstep.
  '''
  headers = {
    'apikey': user['api_key']
  }
  files = {'file': open(filepath, 'rb')}
  url = 'https://api.labstep.com/api/generic/file/upload'
  r = requests.post(
      url,
      headers=headers,
      files=files,
  )
  lsFile = json.loads(r.content)

  data = {
      'body': caption,
      'thread_id': entity['thread']['id'],
      'file_id': [list(lsFile.keys())[0]]
  }
  url = 'https://api.labstep.com/api/generic/comment'

  r = requests.post(
      url,
      json=data,
      headers=headers,
  )

  return json.loads(r.content)


def addComment(user,entity,comment):
  '''Add a comment to a labstep entity such as an experiment or resource.
  
  Parameters
  ----------
  user : obj
    The labstep user to comment as. Must have property 'api_key'. See 'login'.
  entity : obj
    The labstep entity to comment on. Must have 'thread' property with property 'id'.
  comment : str
    The body of the comment

  Returns
  -------
  comment
    An object representing a comment on labstep.
  '''
  headers = {
    'apikey': user['api_key']
  }
  threadId = entity['thread']['id']
  data = {
      'body': comment,
      'thread_id': threadId,
  }
  url = 'https://api.labstep.com/api/generic/comment'
  r = requests.post(
      url,
      json=data,
      headers=headers,
  )
  return json.loads(r.content)


