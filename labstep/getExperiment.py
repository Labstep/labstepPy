import requests
import json

def getExperiment(user,id):
  headers = {
    'apikey': user['api_key']
  }
  url = f"https://api.labstep.com/api/generic/experiment-workflow/{id}"
  r = requests.get(
      url,
      headers=headers,
  )
  return json.loads(r.content)


