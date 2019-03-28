import requests
import json

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