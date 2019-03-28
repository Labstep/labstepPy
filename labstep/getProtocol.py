import requests
import json

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


