import requests
import json

def attachProtocol(user,experiment,protocol):
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
