import requests
import json

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
