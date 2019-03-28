import requests
import json

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


