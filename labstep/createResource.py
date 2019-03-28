import requests
import json

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