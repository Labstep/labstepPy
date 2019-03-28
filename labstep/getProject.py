import requests
import json

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


