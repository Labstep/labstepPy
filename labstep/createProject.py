import requests
import json

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