import requests
import json

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