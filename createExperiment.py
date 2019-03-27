import requests
import json

def createExperiment(user,name,description):
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