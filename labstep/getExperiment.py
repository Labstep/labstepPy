import requests
import json

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


